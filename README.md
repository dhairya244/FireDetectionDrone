# 🔥 FireDetectionDrone

> A Python-based fire detection system using a drone’s live video feed and computer vision.

This project processes video frames to detect fire/smoke in real time — ideal for drone deployment in forest surveillance, industrial safety, and emergency monitoring.

---

## 🧠 Project Overview

Wildfires and industrial fires cause massive damage every year. Detecting fire early can save lives, property, and natural resources. This repository uses computer vision techniques to analyze video frames and trigger alerts when fire is identified in the scene.

The core detection logic identifies fire based on visual cues (color, motion, contours), and raises alarms when fire is present in the input feed.

---

## 📁 Repository Structure

FireDetectionDrone/
├── fireDetection.py # Main detection script
├── settings.json # Configurable parameters
├── Visual Demo.mp4 # Demo video showing fire detection
├── Alarm Sound.mp3 # Notification audio when fire is detected
└── README.md # Project documentation

yaml
Copy code

---

## 🛠️ Features

- 🎥 Detects fire from live or prerecorded video input  
- 🔔 Alarm sound plays on detection  
- ⚙️ Adjustable settings via JSON config  
- 📹 Includes demo video to showcase functionality  

---

## 🚀 Installation

1. **Clone the repository**

```bash
git clone https://github.com/dhairya244/FireDetectionDrone.git
cd FireDetectionDrone
Create virtual environment (recommended)

bash
Copy code
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
Install dependencies

bash
Copy code
pip install -r requirements.txt
▶️ How to Use
bash
Copy code
python fireDetection.py --input <path_to_video_or_live_feed>
Example:

bash
Copy code
python fireDetection.py --input Visual\ Demo.mp4
If fire is detected, the script will:

Highlight the fire region

Show live feed with detection

Play Alarm Sound.mp3

⚙️ Modify thresholds in settings.json for sensitivity.

⚙️ Configuration
settings.json contains all the parameters:

json
Copy code
{
  "min_fire_area": 500,
  "alert_threshold": 0.3,
  "color_filter": {
    "min_hue": 0,
    "max_hue": 50
  }
}
Adjust these to tune accuracy and performance.

🎯 Use Cases
🚁 Drones for forest fire surveillance

🏭 Industrial fire alarms

🏘️ Smart safety systems

📈 Research in environmental detection systems

🧩 Limitations
Relies on visible fire patterns — may not work in heavy smoke

Needs proper lighting conditions

🛠️ Future Improvements
Add Deep Learning-based detection (like YOLO)

Integrate thermal camera support

Deploy on real UAV systems with telemetry

🤝 Contributing
Pull requests and issues are welcome!

📜 License
MIT License

👤 Author
Dhairya Joshi
GitHub: https://github.com/dhairya244
