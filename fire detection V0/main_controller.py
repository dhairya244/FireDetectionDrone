import time
import subprocess
from sensor_trigger import read_sensor
from fire_detector import FireDetector

# Initializing detector
detector = FireDetector("yolov3-fire.cfg","yolov3-fire.weights","fire.names")

def launch_drone():
    subprocess.Popen(["python3", "drone_nav.py"])

def handle_extinguish():
    subprocess.Popen(["python3", "extinguisher_control.py"])

print("[System] Starting fire monitoring system...")

while True:
    if read_sensor():
        print("[System] Sensor fire trigger detected!")
        launch_drone()
        break
    time.sleep(0.5)

import cv2
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    boxes = detector.detect(frame)
    if boxes:
        print("[Vision] Fire in camera frame!")
        handle_extinguish()
        break
    if cv2.waitKey(1)==27:
        break
