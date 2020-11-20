import json
import cozmo
import requests
from time import sleep
from reward import reward_run
from animate import Animate


count = 0

def cozmo_run(robot, content=None):
    global count

    if robot.is_ready:
        if not robot.has_in_progress_actions:
            if robot.is_on_charger:
                robot.drive_off_charger_contacts().wait_for_completed()

            print("Count: %s" % count)
            if content:
                reward_run(robot, position=content['posicao'])
                count = 0
            else:
                if count == 90:
                    anim = Animate()
                    anim.anim_run(robot)
                    count = 0
                else:
                    count += 1


def cozmo_ready(robot: cozmo.robot.Robot):
    while True:
        try:
            response = requests.get("http://ec2-54-152-248-85.compute-1.amazonaws.com:3033/api/rating?terminal=1", timeout=8)

            try:
                if response.status_code == 200:
                    content = json.loads(response.content)
                    print(content)

                    content = {
                        'terminal': '012345',
                        'posicao': 1
                    }
                    
                    sleep(10)
                    cozmo_run(robot, content)

                else:
                    cozmo_run(robot)
            except ValueError:
                cozmo_run(robot)
        except requests.exceptions.Timeout:
            cozmo_run(robot)
        except requests.exceptions.TooManyRedirects:
            cozmo_run(robot)
        except requests.exceptions.RequestException:
            cozmo_run(robot)

        sleep(10)


cozmo.run_program(cozmo_ready)
