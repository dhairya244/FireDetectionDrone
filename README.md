🚁 Fire Detection & Suppression Drone

> An end-to-end autonomous fire detection and suppression system using computer vision, embedded hardware, and UAV navigation.

This project demonstrates a fully integrated proof-of-concept system where a fire sensor triggers a drone launch, the drone navigates autonomously to the target location using a Pixhawk autopilot, detects fire visually using YOLO + OpenCV, and activates a fire-extinguisher actuator to suppress the fire.

---

## 🧠 System Overview

Wildfires and industrial fires are among the most dangerous hazards affecting safety, property, and environment. This project builds a **smart drone system** that:

1. **Monitors fire sensors**
2. **Initiates drone deployment when fire is detected**
3. **Uses onboard vision (YOLO + OpenCV) to confirm fire**
4. **Controls mechanical fire suppression (extinguisher ball / spray)**
5. **Performs autonomous navigation using Pixhawk + MAVSDK**

---
## **FlOW**

<img width="1024" height="1536" alt="image" src="https://github.com/user-attachments/assets/25bcfbf3-575c-40f1-8969-32a031c52041" />


---
## 📹 Demo Summary

The included demo video shows the complete flow:

- A fire sensor detects a fire event.
- Raspberry Pi commands the drone to take off.
- The drone flies toward the fire coordinates using Pixhawk autopilot.
- Onboard camera feed is analyzed using YOLO and OpenCV in real time.
- Fire regions are detected and highlighted.
- The suppressor mechanism (extinguisher actuator or fire-ball release) is triggered.

---

## 🗂️ Repository Structure

FireDetectionDrone/
├── fire_detector.py # Modular YOLO + OpenCV fire detection
├── sensor_trigger.py # Fire sensor simulation / trigger
├── drone_nav.py # Autonomous drone navigation (MAVSDK)
├── extinguisher_control.py # Actuator control for extinguisher
├── main_controller.py # Master script to glue everything
├── models/ # YOLO weights & config files
├── Visual Demo.mp4 # Demonstration video of system
├── requirements.txt # Dependencies
└── README.md

yaml
Copy code

---

## 🛠️ Features

- 🔥 **Real-time fire detection** using YOLO and OpenCV  
- 🚁 **Autonomous UAV navigation** using PIXHAWK + MAVSDK  
- 📡 **Sensor trigger** to initiate mission  
- 🧯 **Actuator control** to deploy fire suppression  
- 🔧 Modular POC code for each major component

---

## 📦 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
🚀 Setup and Usage
1. Monitor Sensor (Simulated)
bash
Copy code
python sensor_trigger.py
This script simulates a fire sensor. In a real system you can replace this with GPIO input from a flame or temperature sensor on Raspberry Pi.

2. Launch the System
Start the master controller which listens for a fire trigger, navigates the drone, and performs vision detection and actuation:

bash
Copy code
python main_controller.py
3. Drone Navigation (MAVSDK)
Drone navigation is controlled using drone_nav.py, which connects to a Pixhawk autopilot via MAVSDK over UDP. Example usage:

bash
Copy code
python drone_nav.py
Modify fire location coordinates to match the detected fire position (real GPS in live systems).

4. Fire Detection Vision
The YOLO + OpenCV based detector is modularized in fire_detector.py. It processes video frames from a camera stream to detect fire in real time.

5. Extinguisher Actuation
Run the actuator control script to trigger the fire suppression mechanism (such as a servo releasing a fire-extinguishing ball or activating a sprayer):

bash
Copy code
python extinguisher_control.py
🔧 How It Works — Component Flow
css
Copy code
[Fire Sensor] → trigger → [Pi Master Controller]
          ↓
 [Drone Launch / Pixhawk Navigation]
          ↓
 [Camera Feed] → [YOLO + OpenCV Detection]
          ↓
    Fire Confirmed → [Extinguisher Actuation]
          ↓
   Return / Next Mission
🧠 Technologies Used
Python for core control and vision logic

OpenCV for real-time frame capture and preprocessing

YOLO deep learning model for fire detection

MAVSDK to control UAV navigation and mission planning

RPi.GPIO to control actuators on Raspberry Pi

📌 Supported Hardware
Component	Role
Raspberry Pi	Onboard compute & vision
Pixhawk	Flight control and autopilot
Camera module	Real-time video input
Fire sensor	Mission trigger
Servo / Actuator	Fire suppression mechanism

🛠️ Future Enhancements
🔁 Real GPS feedback for dynamic waypoint navigation

📊 Telemetry dashboard for real-time monitoring

📡 Remote command and control

🧠 Deep learning model training on larger dataset

🔥 Smoke detection and thermal camera integration

🤝 Contributing
Contributions and feature enhancements are welcome! Fork the repo and open a pull request.

📄 License
This project is released under the MIT License.

👤 Author
Dhairya Joshi
GitHub: https://github.com/dhairya244
