import RPi.GPIO as GPIO
import time

SERVO_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(0)

def spray(duration=2):
    print("[Action] Spraying extinguisher")
    pwm.ChangeDutyCycle(7)  
    time.sleep(duration)
    pwm.ChangeDutyCycle(2)
    pwm.stop()
    GPIO.cleanup()

if __name__ == "__main__":
    spray()
