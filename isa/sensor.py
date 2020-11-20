import time
import RPi.GPIO as GPIO

class Sensor:

    def __init__(self):
        GPIO.setwarnings = False
        GPIO.setmode(GPIO.BCM)
        self.PinBase = 17
        self.PinMachine = 18
        GPIO.setup(self.PinBase, GPIO.IN, GPIO.PUD_DOWN)
        GPIO.setup(self.PinMachine, GPIO.IN, GPIO.PUD_DOWN)
    
    def notComplete(self, local):
        time.sleep(0.5)
        if local == 'base':
            return not GPIO.input(self.PinBase)
        else:
            return not GPIO.input(self.PinMachine)

            