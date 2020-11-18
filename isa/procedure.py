import cozmo
import random
from cozmo.util import degrees, distance_mm, speed_mmps



class Procedures:
    def go_ahead_and_return(self, robot):
        robot.drive_straight(distance_mm(250), speed_mmps(75)).wait_for_completed()
        # robot.play_anim(name="anim_bored_event_02").wait_for_completed()
        if not robot.is_lift_in_pos > 45:
            robot.move_lift(1) # abaixar os braços
        else :
            robot.move_lift(-1) # levantar os braços

        robot.turn_in_place(degrees(360)).wait_for_completed()

        robot.drive_straight(distance_mm(-250), speed_mmps(75)).wait_for_completed()

    def one(self, robot):
        robot.drive_straight(distance_mm(500), speed_mmps(100)).wait_for_completed()
        # robot.play_anim_trigger(cozmo.anim.Triggers.BuildPyramidSuccess).wait_for_completed()
        # robot.play_anim(name="anim_upgrade_reaction_lift_01").wait_for_completed()

        if not robot.is_lift_in_pos > 45:
            robot.move_lift(1) # abaixar os braços
        else :
            robot.move_lift(-1) # levantar os braços

        robot.turn_in_place(degrees(180)).wait_for_completed() # voltar para trás
        robot.drive_straight(distance_mm(500), speed_mmps(100)).wait_for_completed()

    def exec(self, robot):
        trigger = [self.go_ahead_and_return]
        trigger[0](robot)
        