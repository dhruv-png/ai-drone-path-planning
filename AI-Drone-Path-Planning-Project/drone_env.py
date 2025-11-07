import numpy as np
import gymnasium as gym
from gymnasium import spaces
import pybullet as p
import pybullet_data
from config import ENV_CONFIG, OBSTACLES, REWARD_CONFIG

class DronePathPlanningEnv(gym.Env):
    metadata = {'render_modes': ['human'], 'render_fps': 30}

    def __init__(self, gui=True):
        super(DronePathPlanningEnv, self).__init__()
        self.gui = gui
        self.target_pos = np.array(ENV_CONFIG['target_position'])
        self.initial_pos = np.array(ENV_CONFIG['initial_position'])
        self.obstacles = OBSTACLES
        
        self.goal_bonus = REWARD_CONFIG['goal_reached_bonus']
        self.collision_penalty = REWARD_CONFIG['collision_penalty']
        self.distance_weight = REWARD_CONFIG['distance_weight']
        self.time_penalty = REWARD_CONFIG['time_penalty']
        self.goal_threshold = REWARD_CONFIG['goal_threshold']
        self.collision_threshold = REWARD_CONFIG['collision_threshold']
        
        self.action_space = spaces.Box(low=-1, high=1, shape=(4,), dtype=np.float32)
        self.observation_space = spaces.Box(low=-np.inf, high=np.inf, shape=(11,), dtype=np.float32)
        
        if self.gui:
            self.physics_client = p.connect(p.GUI)
        else:
            self.physics_client = p.connect(p.DIRECT)
        
        self.drone_id = None
        self.obstacle_ids = []
        self.step_count = 0
        self.max_steps = 500

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        p.resetSimulation(self.physics_client)
        p.setGravity(0, 0, -9.81)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        p.loadURDF("plane.urdf")
        p.resetDebugVisualizerCamera(cameraDistance=6, cameraYaw=45, cameraPitch=-35, cameraTargetPosition=[1.5, 1.5, 0.5])

        # BLUE SPHERE DRONE (simplified, always works)
        drone_collision = p.createCollisionShape(p.GEOM_SPHERE, radius=0.25)
        drone_visual = p.createVisualShape(p.GEOM_SPHERE, radius=0.25, rgbaColor=[0, 0, 1, 1])
        self.drone_id = p.createMultiBody(baseMass=1.0, baseCollisionShapeIndex=drone_collision, baseVisualShapeIndex=drone_visual, basePosition=self.initial_pos)

        # RED OBSTACLE CUBES
        self.obstacle_ids = []
        for obs in self.obstacles:
            obs_collision = p.createCollisionShape(p.GEOM_BOX, halfExtents=[obs['radius']]*3)
            obs_visual = p.createVisualShape(p.GEOM_BOX, halfExtents=[obs['radius']]*3, rgbaColor=[1, 0, 0, 1])
            obs_id = p.createMultiBody(baseMass=0, baseCollisionShapeIndex=obs_collision, baseVisualShapeIndex=obs_visual, basePosition=obs['position'])
            self.obstacle_ids.append(obs_id)

        # GREEN GOAL CUBE
        goal_visual = p.createVisualShape(p.GEOM_BOX, halfExtents=[0.2,0.2,0.2], rgbaColor=[0,1,0,1])
        p.createMultiBody(baseMass=0, baseVisualShapeIndex=goal_visual, basePosition=self.target_pos)

        self.step_count = 0
        self.previous_distance = np.linalg.norm(self.target_pos - self.initial_pos)
        return self._get_obs(), {}

    def step(self, action):
        self.step_count += 1
        velocity = action[:3] * 2.0
        p.resetBaseVelocity(self.drone_id, linearVelocity=velocity.tolist())
        p.stepSimulation()
        
        pos, orn = p.getBasePositionAndOrientation(self.drone_id)
        reward, done, info = self._compute_reward(np.array(pos))
        
        if self.step_count >= self.max_steps:
            done = True
            info['timeout'] = True
        
        obs = self._get_obs()
        return obs, reward, done, False, info

    def _get_obs(self):
        pos, orn = p.getBasePositionAndOrientation(self.drone_id)
        vel, ang_vel = p.getBaseVelocity(self.drone_id)
        pos = np.array(pos)
        vel = np.array(vel)
        
        to_goal = self.target_pos - pos
        dist_to_goal = np.linalg.norm(to_goal)
        dir_to_goal = to_goal / (dist_to_goal + 1e-6)
        
        min_obs_dist = float('inf')
        for obs in self.obstacles:
            obs_pos = np.array(obs['position'])
            dist = np.linalg.norm(pos - obs_pos) - obs['radius']
            min_obs_dist = min(min_obs_dist, dist)
        
        obs = np.concatenate([pos, vel, [dist_to_goal], dir_to_goal, [min_obs_dist]]).astype(np.float32)
        return obs

    def _compute_reward(self, pos):
        done = False
        info = {}
        dist_to_goal = np.linalg.norm(self.target_pos - pos)
        
        if dist_to_goal < self.goal_threshold:
            return self.goal_bonus, True, {'goal_reached': True}
        
        for obs in self.obstacles:
            obs_pos = np.array(obs['position'])
            if np.linalg.norm(pos - obs_pos) < (obs['radius'] + self.collision_threshold):
                return self.collision_penalty, True, {'collision': True}
        
        if pos[2] < 0.05 or pos[2] > 10.0:
            return self.collision_penalty, True, {'out_of_bounds': True}
        
        distance_improvement = self.previous_distance - dist_to_goal
        reward = distance_improvement * 10.0 - 0.05
        self.previous_distance = dist_to_goal
        
        return reward, False, {}

    def render(self):
        pass

    def close(self):
        p.disconnect(self.physics_client)
