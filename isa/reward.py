import json
import cozmo
import pygame
import random
import requests
from math import ceil
from time import sleep
from motor import Motor
from sensor import Sensor
from datetime import datetime
from view import view_run, view_object_status
from cozmo.util import degrees, distance_mm, speed_mmps


pygame.mixer.init()

url_log = "http://ec2-54-152-248-85.compute-1.amazonaws.com:3033/api/log"
log = {
    'type': 'warning',
    'text': None,
    'datetime': datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f%z")
}

def handle_object(robot):
    ''' visualizando a imagem ? '''

    view_run(robot)
    sleep(2)

    global log
    log['text'] = "handle_object: esta vendo a imagem" if view_object_status() else "handle_object: nao esta vendo a imagem"
    requests.post(url_log, data=json.dumps(log))
    print("esta vendo a imagem" if view_object_status() else "nao esta vendo a imagem")
    return view_object_status()


def get_the_candy(robot):
    ''' pegar o bombom '''
    
    global log

    robot.drive_straight(distance_mm(5000), speed_mmps(220)).wait_for_completed()
    robot.drive_straight(distance_mm(4800), speed_mmps(220)).wait_for_completed()

    sn = Sensor()
    while sn.notComplete('machine'):
        log['text'] = "get_the_candy: nao chegou no sensor"
        print(log)
        requests.post(url_log, data=json.dumps(log))
        robot.drive_straight(distance_mm(20), speed_mmps(100)).wait_for_completed()

    mt = Motor()
    mt.motor_run()
    
    while True:
        if not handle_object(robot):
            break
        else:
            log['text'] = "get_the_candy: Nao saiu o bombom"
            requests.post(url_log, data=json.dumps(log))
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


def valid_got_the_candy(robot, side, deliver):
    ''' persistir até a retirada do bombom do cesto '''

    global log

    while True:
        robot.turn_in_place(degrees(90*(side*-1)), False, 0, degrees(30)).wait_for_completed() # girar
        robot.move_lift(-1)
        if handle_object(robot):
            log['type'] = 'success'
            log['text'] = "valid_got_the_candy: pegou o bombom"
            requests.post(url_log, data=json.dumps(log))

            '''
            try:
                deliver.update({'received': 1})
                requests.post("http://ec2-54-152-248-85.compute-1.amazonaws.com:3033/api/pride", data=json.dumps(deliver))
            except requests.exceptions.Timeout:
                log['type'] = 'error'
                log['text'] = 'post pride: Timeout'
                requests.post(url_log, data=json.dumps(log))
            except requests.exceptions.TooManyRedirects:
                log['type'] = 'error'
                log['text'] = 'post pride: Too Many Redirects'
                requests.post(url_log, data=json.dumps(log))
            except requests.exceptions.RequestException:
                log['type'] = 'error'
                log['text'] = 'post pride: Request Exception'
                requests.post(url_log, data=json.dumps(log))
            '''
            
            robot.move_lift(1)
            sleep(2)
            break
        else:
            log['text'] = "valid_got_the_candy: nao pegou o bombom"
            requests.post(url_log, data=json.dumps(log))
            robot.move_lift(1)
            sleep(2)
            robot.turn_in_place(degrees(90*(side)), False, 0, degrees(30)).wait_for_completed() # girar
            robot.say_text("peghe o prehmio").wait_for_completed()
            sleep(5)
            

def back_to_base(robot, distance, side):
    ''' voltar para a base '''

    global log

    robot.drive_straight(distance_mm(2700 - distance), speed_mmps(220)).wait_for_completed()

    sn = Sensor()
    while sn.notComplete('base'):
        log['text'] = "back_to_base: nao chegou no sensor"
        requests.post(url_log, data=json.dumps(log))
        robot.drive_straight(distance_mm(20), speed_mmps(100)).wait_for_completed()

    robot.turn_in_place(degrees(180), False, 0, degrees(30)).wait_for_completed()
    robot.move_lift(-1)
    sleep(2)
    robot.drive_straight(distance_mm(-150), speed_mmps(220)).wait_for_completed()


def reward_run(robot, position, deliver):
    ''' centralizador do processo '''

    sound = random.randint(0, 3)
    side = 1 if position % 2 == 0 else -1

    if position >= 2:
        distance = 400
    distance = (1000 * ((ceil(position / 2)) -1)) + 400

    if not robot.is_lift_in_pos > 45:
        robot.move_lift(-5)
    
    pygame.mixer.music.load(f'./isa/audio/goal/{sound}.mp3')
    pygame.mixer.music.play()

    get_the_candy(robot)
    deliver_the_candy(robot, distance, side)
    valid_got_the_candy(robot, side, deliver)
    back_to_base(robot, distance, side)

    # if robot.is_on_charger:
    #     if robot.is_charging:
    #         print('carregando')
    #         robot.say_text("charging")
