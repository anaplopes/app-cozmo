import cozmo
import pygame
import random
from math import ceil
from time import sleep
from view import view_run, view_object_status
from motor import Motor
from sensor import Sensor
from cozmo.util import degrees, distance_mm, speed_mmps


pygame.mixer.init()

def handle_object(robot):
    ''' visualizando a imagem ? '''

    view_run(robot)
    sleep(2)
    print("Esta vendo" if view_object_status() else "Nao esta vendo")
    return view_object_status()


def get_the_candy(robot):
    ''' pegar o bombom '''
    
    robot.drive_straight(distance_mm(2850), speed_mmps(220)).wait_for_completed()
    sn = Sensor()
    while sn.notComplete('machine'):
        robot.drive_straight(distance_mm(20), speed_mmps(100)).wait_for_completed()
    mt = Motor()
    mt.motor_run()
    
    while True:
        if not handle_object(robot):
            break
        else:
            mt.motor_run()
            sleep(2)

    robot.move_lift(1)
    sleep(2)
    robot.turn_in_place(degrees(180), False, 0, degrees(30)).wait_for_completed()
    

def deliver_the_candy(robot, distance, side):
    ''' entregar o bombom '''

    idx = random.randint(0, 3)
    frase = ['pahrahbans', 'otimo trahbalio', 'formidahvel', 'obrigahdo']

    robot.drive_straight(distance_mm(distance), speed_mmps(220)).wait_for_completed()
    robot.turn_in_place(degrees(90*side), False, 0, degrees(30)).wait_for_completed() # girar
    robot.say_text(f"{frase[idx]}").wait_for_completed()


def valid_got_the_candy(robot, side):
    ''' persistir até a retirada do bombom do cesto '''

    while True:
        robot.turn_in_place(degrees(90*(side*-1)), False, 0, degrees(30)).wait_for_completed() # girar
        robot.move_lift(-1)
        if handle_object(robot):
            robot.move_lift(1)
            sleep(2)
            break
        else:
            robot.move_lift(1)
            sleep(2)
            robot.turn_in_place(degrees(90*(side)), False, 0, degrees(30)).wait_for_completed() # girar
            robot.say_text("peghe o prehmio").wait_for_completed()
            sleep(5)
            

def back_to_base(robot, distance, side):
    ''' voltar para a base '''

    robot.drive_straight(distance_mm(2700 - distance), speed_mmps(220)).wait_for_completed()
    sn = Sensor()
    while sn.notComplete('base'):
        robot.drive_straight(distance_mm(20), speed_mmps(100)).wait_for_completed()
    robot.turn_in_place(degrees(180), False, 0, degrees(30)).wait_for_completed()
    robot.move_lift(-1)
    sleep(2)
    robot.drive_straight(distance_mm(-150), speed_mmps(220)).wait_for_completed()


def reward_run(robot, position=0):

    sound = random.randint(0, 3)
    distance = 450 * (ceil(position / 2))
    side = 1 if position % 2 == 0 else -1

    if position == 0:
        robot.say_text("position error").wait_for_completed()
        robot.abort_all_actions(log_abort_messages=False)
        
    else:
        if not robot.is_lift_in_pos > 45:
            robot.move_lift(-5)
        
        pygame.mixer.music.load(f'./isa/audio/goal/{sound}.mp3')
        pygame.mixer.music.play()

        get_the_candy(robot)
        deliver_the_candy(robot, distance, side)
        valid_got_the_candy(robot, side)
        back_to_base(robot, distance, side)

        # if robot.is_on_charger:
        #     if robot.is_charging:
        #         print('carregando')
        #         robot.say_text("charging")
