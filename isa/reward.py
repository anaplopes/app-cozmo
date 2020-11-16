import random
from math import ceil
from time import sleep
from cozmo.util import degrees, distance_mm, speed_mmps
from motor import Motor


def reward(robot, position=0):

    frase = ['pahrahbans', 'otimo trahbalio', 'formidahvel', 'obrigado']
    idx = random.randint(0, 3)
    distance = 400 * (ceil(position / 2))
    side = 1 if position % 2 == 0 else -1

    if position == 0:
        robot.say_text("position error").wait_for_completed()
        robot.abort_all_actions(log_abort_messages=False)

    else:
        if not robot.is_lift_in_pos > 45:
            robot.move_lift(1)
        
        # PEGAR O BOMBOM
        robot.drive_straight(distance_mm(900), speed_mmps(100)).wait_for_completed()
        #Motor().motor_run()
        sleep(3)
        robot.turn_in_place(degrees(90)).wait_for_completed() # girar a esquerda
        robot.turn_in_place(degrees(90)).wait_for_completed() # girar a esquerda
        
        # ENTREGAR O BOMBOM
        robot.drive_straight(distance_mm(distance), speed_mmps(100)).wait_for_completed()
        robot.turn_in_place(degrees(90*side)).wait_for_completed() # girar
        robot.say_text(f"{frase[idx]}").wait_for_completed()

        # VOLTAR PARA A BASE
        robot.turn_in_place(degrees(90*(side*-1))).wait_for_completed() # girar
        robot.drive_straight(distance_mm(800 - distance), speed_mmps(100)).wait_for_completed()

        # ENTRAR NA BASE
        robot.turn_in_place(degrees(90)).wait_for_completed() # girar a esquerda
        robot.turn_in_place(degrees(90)).wait_for_completed() # girar a esquerda
        robot.drive_straight(distance_mm(-200), speed_mmps(100)).wait_for_completed()
        robot.drive_straight(distance_mm(2), speed_mmps(100)).wait_for_completed()

        if robot.is_on_charger:
            if robot.is_charging:
                print('carregando')
                robot.say_text("charging")
