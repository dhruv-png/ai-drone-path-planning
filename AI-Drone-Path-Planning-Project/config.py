# config.py - Configuration file for AI Drone Path Planning Project

# Environment Configuration
ENV_CONFIG = {
    'gui': True,                    # Show 3D visualization
    'record': False,                # Record video
    'aggregate_phy_steps': 5,       # Physics steps per control step
    'freq': 240,                    # Simulation frequency (Hz)
    'target_position': [3.0, 3.0, 1.0],  # Goal position [x, y, z]
    'initial_position': [0.0, 0.0, 0.3], # Start position [x, y, z]
}

# Obstacle Configuration
OBSTACLES = [
    {'position': [1.5, 1.5, 0.5], 'radius': 0.3},  # Obstacle 1
    {'position': [2.5, 0.5, 1.0], 'radius': 0.25}, # Obstacle 2
    {'position': [0.8, 2.8, 0.8], 'radius': 0.35}, # Obstacle 3
]

# Reward Function Weights
REWARD_CONFIG = {
    'goal_reached_bonus': 200.0,     # Bonus for reaching goal
    'collision_penalty': -100.0,      # Penalty for collision
    'distance_weight': -1.0,          # Weight for distance to goal
    'time_penalty': -0.1,             # Small penalty per step
    'goal_threshold': 0.3,            # Distance to consider goal reached (meters)
    'collision_threshold': 0.4,       # Distance to consider collision (meters)
}

# Training Configuration
TRAIN_CONFIG = {
    'algorithm': 'PPO',               # RL Algorithm (PPO, SAC, TD3)
    'total_timesteps': 150000,        # Total training steps
    'learning_rate': 3e-4,            # Learning rate
    'n_steps': 2048,                  # Steps per update (for PPO)
    'batch_size': 64,                 # Minibatch size
    'gamma': 0.99,                    # Discount factor
    'gae_lambda': 0.95,               # GAE lambda
    'clip_range': 0.2,                # PPO clip range
    'ent_coef': 0.01,                 # Entropy coefficient
    'verbose': 1,                     # Print training info
    'tensorboard_log': './logs/',     # TensorBoard log directory
    'save_freq': 10000,               # Save model every N steps
    'model_save_path': './models/',   # Directory to save models
}

# Test Configuration
TEST_CONFIG = {
    'num_episodes': 5,                # Number of test episodes
    'max_steps': 500,                 # Max steps per episode
    'render': True,                   # Show visualization
    'record_video': True,             # Record test videos
    'model_path': './models/best_model.zip',  # Path to trained model
}
