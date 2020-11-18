import cozmo
import random
from math import ceil
from time import sleep
from view import View
from motor import Motor
from cozmo.util import degrees, distance_mm, speed_mmps


def handle_object(robot):
    ''' visualizando a imagem ? '''

    View().view_run(robot)
    sleep(2)
    print("Esta vendo" if View().view_object_status() else "Nao esta vendo")
    return View().view_object_status()


def get_the_candy(robot):
    ''' pegar o bombom '''
    
    robot.drive_straight(distance_mm(1000), speed_mmps(100)).wait_for_completed()
    #Motor().motor_run()
    
    while True:
        if not handle_object(robot):
            break
        else:
            sleep(2)

    robot.move_lift(1)
    sleep(2)
    robot.turn_in_place(degrees(90)).wait_for_completed() # girar a esquerda
    robot.turn_in_place(degrees(90)).wait_for_completed() # girar a esquerda
    

def deliver_the_candy(robot, distance, side):
    ''' entregar o bombom '''

    idx = random.randint(0, 3)
    frase = ['pahrahbans', 'otimo trahbalio', 'formidahvel', 'obrigahdo']

    robot.drive_straight(distance_mm(distance), speed_mmps(100)).wait_for_completed()
    robot.turn_in_place(degrees(90*side)).wait_for_completed() # girar
    robot.say_text(f"{frase[idx]}").wait_for_completed()


def valid_got_the_candy(robot, side):
    ''' persistir até a retirada do bombom do cesto '''

    while True:
        robot.turn_in_place(degrees(90*(side*-1))).wait_for_completed() # girar
        robot.move_lift(-1)
        if handle_object(robot):
            robot.move_lift(1)
            sleep(2)
            break
        else:
            robot.move_lift(1)
            sleep(2)
            robot.turn_in_place(degrees(90*(side))).wait_for_completed() # girar
            robot.say_text("peghe o prehmio").wait_for_completed()
            sleep(5)
            

def back_to_base(robot, distance, side):
    ''' voltar para a base '''

    robot.drive_straight(distance_mm(800 - distance), speed_mmps(100)).wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed() # girar a esquerda
    robot.turn_in_place(degrees(90)).wait_for_completed() # girar a esquerda
    robot.move_lift(-1)
    sleep(2)
    robot.drive_straight(distance_mm(-200), speed_mmps(100)).wait_for_completed()


def reward_run(robot, position=0):

    distance = 500 * (ceil(position / 2))
    side = 1 if position % 2 == 0 else -1

    if position == 0:
        robot.say_text("position error").wait_for_completed()
        robot.abort_all_actions(log_abort_messages=False)
        
    else:
        if not robot.is_lift_in_pos > 45:
            robot.move_lift(-5)
        
        get_the_candy(robot)
        deliver_the_candy(robot, distance, side)
        valid_got_the_candy(robot, side)
        back_to_base(robot, distance, side)

        # if robot.is_on_charger:
        #     if robot.is_charging:
        #         print('carregando')
        #         robot.say_text("charging")
