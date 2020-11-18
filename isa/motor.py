import sys
import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
step_pins = [21,20,16,12]

for pin in step_pins:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin, False)


class Motor:
    
    def __init__(self):
        self.seq = [[1,0,0,0],
                    [1,1,0,0],
                    [0,1,0,0],
                    [0,1,1,0],
                    [0,0,1,0],
                    [0,0,1,1],
                    [0,0,0,1],
                    [1,0,0,1]]

        self.step_count = len(self.seq)-1
        self.wait_time = 1/float(800)
        self.switch_up_pin = 14
        self.switch_down_pin = 15

    
    
    def move(self, side):
        ''' Verifica se está na posicao de inicio '''
        
        step_counter = 0
        count_motor = 0

        while (GPIO.input(self.switch_down_pin) == 0 and side == -1) or (GPIO.input(self.switch_up_pin) == 0 and side == 1):
            for pin in range(0, 4):
                xpin = step_pins[pin]
                if self.seq[step_counter][pin]!=0:
                    GPIO.output(xpin, True)
                else:
                    GPIO.output(xpin, False)
            
            step_counter += side
            count_motor += 1
            if (step_counter>=self.step_count):
                step_counter = 0
            if (step_counter<0):
                step_counter = self.step_count
            time.sleep(self.wait_time)


    def motor_run(self):
        self.move(-1)
        self.move(1)