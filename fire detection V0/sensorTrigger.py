import time
import random

def read_sensor():
    """
    Simulate a fire sensor reading.
    Returns True when fire is detected.
    """
    return random.random() > 0.9

if __name__ == "__main__":
    print("[Sensor] Monitoring for fire...")
    try:
        while True:
            if read_sensor():
                print("[Sensor] FIRE DETECTED!")
                # Write trigger flag to file
                with open("fire_trigger.txt", "w") as f:
                    f.write("1")
                break
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Stopping sensor monitor.")
