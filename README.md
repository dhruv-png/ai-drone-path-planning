humanize the text

 🚁 AI Drone Path Planning Project

 

Watch an AI drone learn to fly to a goal while avoiding obstacles! Achieved 100% success rate!

 🎯 What This Project Does

I built a drone that learns by itself to fly from a starting point to a green goal cube while dodging red obstacles. It uses **reinforcement learning** (PPO algorithm) and looks super cool in 3D!

Results:
- ✅ 100% success - reaches goal every single time
- ✅ Takes ~400 steps to get there
- ✅ Total reward: ~220 points per flight
- ✅ Trained in 20 minutes on a regular laptop

 🛠️ Tech I Used


• PyBullet = realistic 3D physics
• Gymnasium = RL environment rules
• Stable-Baselines3 = smart AI training
• Python = everything else


 🚀 Super Easy to Run

 Step 1: Setup
bash
conda activate drone_project
pip install -r requirements.txt

 Step 2: Run the Demo
bash
python test.py


You'll see:
- A 3D window with blue drone, red obstacles, green goal
- Terminal shows results like "GOAL REACHED!" 
- Success rate printed at the end

 🧠 How the Drone Learns

1. Blue sphere = my drone (25cm wide)
2. Red cubes = obstacles to avoid
3. Green cube = goal to reach
4. Workspace = 20m x 20m x 10m area

Rewards:
- +200 points = touch the goal! 🎉
- -100 points = hit obstacle 😵
- -0.05 points = every second wasted ⏰

The AI tries thousands of flights, learns from rewards, and gets smarter!

 📊 My Results (Real Output)


Episode 1/5
  ✓ GOAL REACHED in 393 steps! Total Reward: 220.38
Episode 2/5  
  ✓ GOAL REACHED in 393 steps! Total Reward: 220.38
SUCCESS RATE: 5/5 (100%)


 🗂️ What's Inside


drone_env.py     # The drone world & physics
train.py         # Teaches the AI
test.py          # Runs the demo
config.py        # Settings (goals, obstacles)
models/          # My trained AI brain


 ⚙️ Customize It!

Change obstacles in `config.py`:**
python
OBSTACLES = [
    {"position": [1.5, 2.0, 0.3], "radius": 0.3},  # Move this one!
]


Retrain:
bash
python train.py


 🎮 Files You Need

| File | What it does |
|------|-------------|
| `test.py` | Run this first - shows the magic! |
| `drone_env.py` | Physics world + drone |
| `train.py` | AI learning (optional) |

## 📈 Want to See Training Progress?

bash
tensorboard --logdir logs/

Open (http://localhost:6006) in browser.

 🎉 Why This Rocks

✅ Works every time (100% success)  
✅ Real 3D physics (not fake 2D)  
✅ Ready to run (no setup headaches)  
✅ Easy to change (add obstacles, goals)  
✅ Great for learning RL concepts  


Built for my AI class project - works perfectly!
⭐ Star if you like it! Questions? Open an issue.

Made with Python, PyBullet, and a lot of trial & error 😄

Citations:
[1] image.jpg https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/86949195/97744f44-fcd9-448b-8f3e-a96c163b6458/image.jpg
[2] image.jpg https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/86949195/c5169174-7a01-4196-bb88-a29d84a23413/image.jpg
[3] image.jpg https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/86949195/6ea996ef-ea1b-4d61-88f4-b69d24cebe9e/image.jpg
[4] image.jpg https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/86949195/18814dd7-4ef4-4cd8-b851-55c34b3f2f76/image.jpg
[5] drone_env.py https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/86949195/555de919-5a39-4913-b91f-01c8c686b202/drone_env.py
[6] image.jpg https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/86949195/8180ed82-94c1-4262-b32a-13ef5cde23ee/image.jpg
[7] image.jpg https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/86949195/a42c4b95-cd3a-4f00-96a8-2d8c136ade29/image.jpg
[8] image.jpg https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/86949195/7f14567a-7ffe-4dfa-966d-c76d6f598d03/image.jpg
[9] image.jpg https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/86949195/cda13405-0478-4486-a605-5e52a048db9b/image.jpg
[10] image.jpg https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/86949195/02740114-1e39-4aea-8f67-57c40a04d435/image.jpg
[11] image.jpg https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/86949195/fb8600a2-d2bd-49d6-b6d7-4ef1cf23e5a6/image.jpg
