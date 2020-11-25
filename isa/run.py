import json
import cozmo
import requests
from time import sleep
from animate import Animate
from datetime import datetime
from reward import reward_run


count = 0

def cozmo_run(robot, position=None, deliver=None):
    global count

    if robot.is_ready:
        if not robot.has_in_progress_actions:
            if robot.is_on_charger:
                robot.drive_off_charger_contacts().wait_for_completed()

            print("Count: %s" % count)
            if position:
                reward_run(robot, position=position, deliver=deliver)
                count = 0
            else:
                if count == 90:
                    anim = Animate()
                    anim.anim_run(robot)
                    count = 0
                else:
                    count += 1


def cozmo_ready(robot: cozmo.robot.Robot):

    url_log = "http://ec2-54-152-248-85.compute-1.amazonaws.com:3033/api/log"
    log = {
        'type': 'error',
        'text': None,
        'datetime': datetime.now()
    }

    while True:
        try:
            resp_deliver = requests.get("http://ec2-54-152-248-85.compute-1.amazonaws.com:3033/api/pride", timeout=8)

            if resp_deliver.status_code == 200:
                deliver = json.loads(resp_deliver.content)
                print(deliver)

                try:
                    resp_pos = requests.get(f"http://ec2-54-152-248-85.compute-1.amazonaws.com:3033/api/position?sigla={deliver['sigla']}", timeout=8)

                    if resp_pos.status_code == 200:
                        position = json.loads(resp_pos.content)
                        print(position)
                        
                        sleep(10)
                        cozmo_run(robot, position['position'], deliver)

                    else:
                        cozmo_run(robot)

                
                except ValueError:
                    log['text'] = 'get position: Value Error'
                    requests.post(url_log, data=json.dumps(log))
                    cozmo_run(robot)
                except requests.exceptions.Timeout:
                    log['text'] = 'get position: Timeout'
                    requests.post(url_log, data=json.dumps(log))
                    cozmo_run(robot)
                except requests.exceptions.TooManyRedirects:
                    log['text'] = 'get position: Too Many Redirects'
                    requests.post(url_log, data=json.dumps(log))
                    cozmo_run(robot)
                except requests.exceptions.RequestException:
                    log['text'] = 'get position: Request Exception'
                    requests.post(url_log, data=json.dumps(log))
                    cozmo_run(robot)
                        
            else:
                cozmo_run(robot)

        except ValueError:
            log['text'] = 'get goal: Value Error'
            requests.post(url_log, data=json.dumps(log))
            cozmo_run(robot)
        except requests.exceptions.Timeout:
            log['text'] = 'get goal: Timeout'
            requests.post(url_log, data=json.dumps(log))
            cozmo_run(robot)
        except requests.exceptions.TooManyRedirects:
            log['text'] = 'get goal: Too Many Redirects'
            requests.post(url_log, data=json.dumps(log))
            cozmo_run(robot)
        except requests.exceptions.RequestException:
            log['text'] = 'get goal: Request Exception'
            requests.post(url_log, data=json.dumps(log))
            cozmo_run(robot)

        sleep(10)


cozmo.run_program(cozmo_ready)
