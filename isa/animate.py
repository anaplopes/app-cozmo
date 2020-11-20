import cozmo
import pygame
import random
from time import sleep
from sensor import Sensor
from cozmo.anim import Triggers
from cozmo.util import degrees, distance_mm, speed_mmps


pygame.mixer.init()

class Animate:

    def procedure_00(self, robot, sound):
        ''' padrão '''
        sn = Sensor()
        pygame.mixer.music.load(f'./isa/audio/message/{sound}.mp3')
        pygame.mixer.music.play()
        robot.drive_straight(distance_mm(2850), speed_mmps(220)).wait_for_completed()
        while sn.notComplete('machine'):
            robot.drive_straight(distance_mm(20), speed_mmps(100)).wait_for_completed()
        robot.move_lift(1)
        sleep(2)
        robot.turn_in_place(degrees(180), False, 0, degrees(30)).wait_for_completed()
        robot.move_lift(-1)
        robot.drive_straight(distance_mm(2700), speed_mmps(220)).wait_for_completed()
        while sn.notComplete('base'):
            robot.drive_straight(distance_mm(20), speed_mmps(100)).wait_for_completed()
        robot.move_lift(1)
        sleep(2)
        robot.turn_in_place(degrees(180), False, 0, degrees(30)).wait_for_completed()
        robot.move_lift(-1)
        robot.drive_straight(distance_mm(-150), speed_mmps(220)).wait_for_completed()

    
    def procedure_01(self, robot, sound):
        ''' Relógio de espera | tédio '''

        pygame.mixer.music.load(f'./isa/audio/message/{sound}.mp3')
        pygame.mixer.music.play()
        robot.drive_straight(distance_mm(300), speed_mmps(100)).wait_for_completed()
        robot.play_anim(name="anim_bored_event_02").wait_for_completed()
        robot.drive_straight(distance_mm(300), speed_mmps(100)).wait_for_completed()
        robot.move_lift(1)
        sleep(2)
        robot.turn_in_place(degrees(180)).wait_for_completed()
        robot.turn_in_place(degrees(180)).wait_for_completed()
        robot.turn_in_place(degrees(360)).wait_for_completed()
        robot.move_lift(-1)
        robot.drive_straight(distance_mm(300), speed_mmps(100)).wait_for_completed()
        robot.play_anim(name="anim_bored_event_02").wait_for_completed()
        robot.move_lift(1)
        sleep(2)
        robot.turn_in_place(degrees(360)).wait_for_completed()
        robot.turn_in_place(degrees(180)).wait_for_completed()
        robot.drive_straight(distance_mm(500), speed_mmps(100)).wait_for_completed()
        robot.turn_in_place(degrees(90)).wait_for_completed()
        robot.turn_in_place(degrees(90)).wait_for_completed()
        robot.move_lift(-1)
        robot.drive_straight(distance_mm(-100), speed_mmps(100)).wait_for_completed()


    def procedure_02(self, robot, sound):
        ''' Ataque de sucesso '''

        pygame.mixer.music.load(f'./isa/audio/message/{sound}.mp3')
        pygame.mixer.music.play()
        robot.drive_straight(distance_mm(600), speed_mmps(100)).wait_for_completed()
        robot.move_lift(1)
        sleep(2)
        robot.turn_in_place(degrees(180)).wait_for_completed()
        robot.move_lift(-1)
        robot.drive_straight(distance_mm(300), speed_mmps(100)).wait_for_completed()
        robot.play_anim(name="anim_pounce_success_02").wait_for_completed()
        robot.move_lift(1)
        sleep(2)
        robot.turn_in_place(degrees(180)).wait_for_completed()
        robot.move_lift(-1)
        robot.drive_straight(distance_mm(600), speed_mmps(100)).wait_for_completed()
        robot.play_anim(name="anim_pounce_success_02").wait_for_completed()
        robot.move_lift(1)
        sleep(2)
        robot.turn_in_place(degrees(180)).wait_for_completed()
        robot.drive_straight(distance_mm(300), speed_mmps(100)).wait_for_completed()
        robot.turn_in_place(degrees(360)).wait_for_completed()
        robot.drive_straight(distance_mm(500), speed_mmps(100)).wait_for_completed()
        robot.turn_in_place(degrees(90)).wait_for_completed()
        robot.turn_in_place(degrees(90)).wait_for_completed()
        robot.move_lift(-1)
        robot.drive_straight(distance_mm(-100), speed_mmps(100)).wait_for_completed()


    def procedure_03(self, robot, sound):
        ''' levanta o braço e espera '''

        pygame.mixer.music.load(f'./isa/audio/message/{sound}.mp3')
        pygame.mixer.music.play()
        robot.drive_straight(distance_mm(300), speed_mmps(100)).wait_for_completed()
        robot.play_anim_trigger(cozmo.anim.Triggers.OnSpeedtapTap).wait_for_completed()
        robot.drive_straight(distance_mm(300), speed_mmps(100)).wait_for_completed()
        robot.drive_straight(distance_mm(300), speed_mmps(100)).wait_for_completed()
        robot.move_lift(1)
        sleep(2)
        robot.turn_in_place(degrees(360)).wait_for_completed()
        robot.turn_in_place(degrees(180)).wait_for_completed()
        robot.play_anim_trigger(cozmo.anim.Triggers.CubePouncePounceNormal).wait_for_completed()
        robot.play_anim(name="anim_bored_01").wait_for_completed()
        robot.drive_straight(distance_mm(800), speed_mmps(100)).wait_for_completed()
        robot.move_lift(1)
        sleep(2)
        robot.turn_in_place(degrees(90)).wait_for_completed()
        robot.turn_in_place(degrees(90)).wait_for_completed()
        robot.move_lift(-1)
        robot.drive_straight(distance_mm(-100), speed_mmps(100)).wait_for_completed()


    def procedure_04(self, robot, sound):
        ''' Ataque de sucesso, cachorrinho '''
        
        pygame.mixer.music.load(f'./isa/audio/message/{sound}.mp3')
        pygame.mixer.music.play()
        robot.drive_straight(distance_mm(600), speed_mmps(100)).wait_for_completed()
        robot.move_lift(1)
        sleep(2)
        robot.turn_in_place(degrees(360)).wait_for_completed()
        robot.turn_in_place(degrees(180)).wait_for_completed()
        robot.move_lift(-1)
        robot.drive_straight(distance_mm(300), speed_mmps(100)).wait_for_completed()
        robot.play_anim(name="anim_pounce_success_02").wait_for_completed()
        robot.play_anim(name="anim_petdetection_dog_03").wait_for_completed()
        robot.move_lift(1)
        sleep(2)
        robot.turn_in_place(degrees(180)).wait_for_completed()
        robot.move_lift(-1)
        robot.drive_straight(distance_mm(600), speed_mmps(100)).wait_for_completed()
        robot.play_anim(name="anim_pounce_success_02").wait_for_completed()
        robot.play_anim(name="anim_petdetection_dog_03").wait_for_completed()
        robot.move_lift(1)
        sleep(2)
        robot.turn_in_place(degrees(180)).wait_for_completed()
        robot.move_lift(-1)
        robot.drive_straight(distance_mm(900), speed_mmps(100)).wait_for_completed()
        robot.move_lift(1)
        sleep(2)
        robot.turn_in_place(degrees(90)).wait_for_completed()
        robot.turn_in_place(degrees(90)).wait_for_completed()
        robot.move_lift(-1)
        robot.drive_straight(distance_mm(-100), speed_mmps(100)).wait_for_completed()


    def procedure_05(self, robot, sound):
        ''' gatinho '''

        pygame.mixer.music.load(f'./isa/audio/message/{sound}.mp3')
        pygame.mixer.music.play()
        robot.drive_straight(distance_mm(300), speed_mmps(100)).wait_for_completed()
        robot.play_anim(name="anim_petdetection_cat_01").wait_for_completed()
        robot.drive_straight(distance_mm(300), speed_mmps(100)).wait_for_completed()
        robot.move_lift(1)
        sleep(2)
        robot.turn_in_place(degrees(180)).wait_for_completed()
        robot.turn_in_place(degrees(180)).wait_for_completed()
        robot.turn_in_place(degrees(360)).wait_for_completed()
        robot.move_lift(-1)
        robot.drive_straight(distance_mm(300), speed_mmps(100)).wait_for_completed()
        robot.play_anim(name="anim_petdetection_cat_01").wait_for_completed()
        robot.move_lift(1)
        sleep(2)
        robot.turn_in_place(degrees(360)).wait_for_completed()
        robot.turn_in_place(degrees(180)).wait_for_completed()
        robot.move_lift(-1)
        robot.drive_straight(distance_mm(500), speed_mmps(100)).wait_for_completed()
        robot.move_lift(1)
        sleep(2)
        robot.turn_in_place(degrees(90)).wait_for_completed()
        robot.turn_in_place(degrees(90)).wait_for_completed()
        robot.move_lift(-1)
        robot.drive_straight(distance_mm(-100), speed_mmps(100)).wait_for_completed()


    def procedure_06(self, robot, sound):
        ''' Ataque de sucesso, levanta o braço e espera '''

        pygame.mixer.music.load(f'./isa/audio/message/{sound}.mp3')
        pygame.mixer.music.play()
        robot.drive_straight(distance_mm(600), speed_mmps(100)).wait_for_completed()
        robot.move_lift(1)
        sleep(2)
        robot.turn_in_place(degrees(360)).wait_for_completed()
        robot.turn_in_place(degrees(180)).wait_for_completed()
        robot.move_lift(-1)
        robot.drive_straight(distance_mm(300), speed_mmps(100)).wait_for_completed()
        robot.play_anim(name="anim_pounce_success_02").wait_for_completed()
        robot.play_anim_trigger(cozmo.anim.Triggers.OnSpeedtapTap).wait_for_completed()
        robot.drive_straight(distance_mm(600), speed_mmps(100)).wait_for_completed()
        robot.play_anim(name="anim_pounce_success_02").wait_for_completed()
        robot.play_anim_trigger(cozmo.anim.Triggers.OnSpeedtapTap).wait_for_completed()
        robot.move_lift(1)
        sleep(2)
        robot.turn_in_place(degrees(180)).wait_for_completed()
        robot.drive_straight(distance_mm(800), speed_mmps(100)).wait_for_completed()
        robot.move_lift(1)
        sleep(2)
        robot.turn_in_place(degrees(90)).wait_for_completed()
        robot.turn_in_place(degrees(90)).wait_for_completed()
        robot.move_lift(-1)
        robot.drive_straight(distance_mm(-100), speed_mmps(100)).wait_for_completed()


    def procedure_07(self, robot, sound):
        ''' , Ataque de sucesso '''

        pygame.mixer.music.load(f'./isa/audio/message/{sound}.mp3')
        pygame.mixer.music.play()
        robot.drive_straight(distance_mm(600), speed_mmps(100)).wait_for_completed()
        robot.play_anim(name="anim_bored_event_03").wait_for_completed()
        robot.move_lift(1)
        sleep(2)
        robot.turn_in_place(degrees(180)).wait_for_completed()
        robot.drive_straight(distance_mm(300), speed_mmps(100)).wait_for_completed()
        robot.play_anim(name="anim_pounce_success_02").wait_for_completed()
        robot.move_lift(1)
        sleep(2)
        robot.turn_in_place(degrees(180)).wait_for_completed()
        robot.drive_straight(distance_mm(600), speed_mmps(100)).wait_for_completed()
        robot.play_anim(name="anim_bored_event_03").wait_for_completed()
        robot.drive_straight(distance_mm(200), speed_mmps(100)).wait_for_completed()
        robot.play_anim(name="anim_pounce_success_02").wait_for_completed()
        robot.move_lift(1)
        sleep(2)
        robot.turn_in_place(degrees(180)).wait_for_completed()
        robot.drive_straight(distance_mm(1000), speed_mmps(100)).wait_for_completed()
        robot.move_lift(1)
        sleep(2)
        robot.turn_in_place(degrees(90)).wait_for_completed()
        robot.turn_in_place(degrees(90)).wait_for_completed()
        robot.move_lift(-1)
        robot.drive_straight(distance_mm(-100), speed_mmps(100)).wait_for_completed()


    def anim_run(self, robot):
        
        trigger = [self.procedure_00]
        msn = random.randint(0, 20)
        
        trigger[0](robot, msn)
