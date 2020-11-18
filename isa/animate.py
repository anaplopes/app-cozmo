import random
from cozmo.util import degrees, distance_mm, speed_mmps
from cozmo.anim import Triggers


class Animate:
    
    # Muito animado, mas muda muito sua posição
    def anim_speedtap_wingame_intensity02_01(self, robot):
        print("anim_speedtap_wingame_intensity02_01")
        robot.play_anim(name="anim_speedtap_wingame_intensity02_01").wait_for_completed()

    # Entediado e mostra o "joguinho", mas muda a angulação
    def anim_bored_event_03(self, robot):
        print("anim_bored_event_03")
        robot.play_anim(name="anim_bored_event_03").wait_for_completed()

    # Sentimento de perda, mas vira
    def CubePounceLoseSession(self, robot):
        print("CubePounceLoseSession")
        robot.play_anim_trigger(cozmo.anim.Triggers.CubePounceLoseSession).wait_for_completed()

    # Dança e movimento - Mas move bastante de posição
    def OnSpeedtapGameCozmoWinHighIntensity(self, robot):
        print("OnSpeedtapGameCozmoWinHighIntensity")
        robot.play_anim_trigger(cozmo.anim.Triggers.OnSpeedtapGameCozmoWinHighIntensity).wait_for_completed()

    # Fica um pouco bravo, chacoalha os braços e se move de posição
    def OnSpeedtapGamePlayerWinHighIntensity(self, robot): # Este fica batendo um pouco aos lados
        print("OnSpeedtapGamePlayerWinHighIntensity")
        robot.play_anim_trigger(cozmo.anim.Triggers.OnSpeedtapGamePlayerWinHighIntensity).wait_for_completed()

    # Imita um gato
    def anim_petdetection_cat_01(self, robot):
        print("anim_petdetection_cat_01")
        robot.play_anim(name="anim_petdetection_cat_01").wait_for_completed()
        
    # Imita um cachorro
    def anim_petdetection_dog_03(self, robot):
        print("anim_petdetection_dog_03")
        robot.play_anim(name="anim_petdetection_dog_03").wait_for_completed()

    # Entediado, sem ação
    def anim_bored_01(self, robot):
        print("anim_bored_01")
        robot.play_anim(name="anim_bored_01").wait_for_completed()
    
    # Parece estar esperando uma ação
    def anim_poked_giggle(self, robot):
        print("anim_poked_giggle")
        robot.play_anim(name="anim_poked_giggle").wait_for_completed()

    # Ataque de sucesso
    def anim_pounce_success_02(self, robot):
        print("anim_pounce_success_02")
        robot.play_anim(name="anim_pounce_success_02").wait_for_completed()

    # Relógio de espera | tédio
    def anim_bored_event_02(self, robot):
        print("anim_bored_event_02")
        robot.play_anim(name="anim_bored_event_02").wait_for_completed()

    # Face não identificada
    def anim_reacttoface_unidentified_02(self, robot):
        print("anim_reacttoface_unidentified_02")
        robot.play_anim(name="anim_reacttoface_unidentified_02").wait_for_completed()

    # Fica surpreso e levanta o rostoanim_pounce_success_02
    def anim_upgrade_reaction_lift_01(self, robot):
        print("anim_upgrade_reaction_lift_01")
        robot.play_anim(name="anim_upgrade_reaction_lift_01").wait_for_completed()

    # Após falha, ele fica esperando 
    def KnockOverFailure(self, robot):
        print("KnockOverFailure")
        robot.play_anim_trigger(cozmo.anim.Triggers.KnockOverFailure).wait_for_completed()

    # Ânimo com os braços pra baixo
    def FailedToRightFromFace(self, robot):
        print("FailedToRightFromFace")
        robot.play_anim_trigger(cozmo.anim.Triggers.FailedToRightFromFace).wait_for_completed()

    # Reação um pouco neutra
    def ReactToBlockPickupSuccess(self, robot):
        print("ReactToBlockPickupSuccess")
        robot.play_anim_trigger(cozmo.anim.Triggers.ReactToBlockPickupSuccess).wait_for_completed()

    # Dança do sucesso - Levanta os braços e anda um pouco
    def BuildPyramidSuccess(self, robot):
        print("BuildPyramidSuccess")
        robot.drive_straight(distance_mm(200), speed_mmps(100)).wait_for_completed()
        robot.play_anim_trigger(cozmo.anim.Triggers.BuildPyramidSuccess).wait_for_completed()
        # robot.drive_straight(distance_mm(200), speed_mmps(100)).wait_for_completed()

    # Levanta os braços e espera por algum objeto sobre ele
    def OnSpeedtapHandCozmoWin(self, robot):
        print("OnSpeedtapHandCozmoWin")
        robot.play_anim_trigger(cozmo.anim.Triggers.OnSpeedtapHandCozmoWin).wait_for_completed()

    # Levanta os braços e espera por algum objeto sobre ele
    def OnSpeedtapHandPlayerWin(self, robot):
        print("OnSpeedtapHandPlayerWin")
        robot.play_anim_trigger(cozmo.anim.Triggers.OnSpeedtapHandPlayerWin).wait_for_completed()

    # Fica esperando com o braço levantado
    def OnSpeedtapTap(self, robot):
        print("OnSpeedtapTap")
        robot.play_anim_trigger(cozmo.anim.Triggers.OnSpeedtapTap).wait_for_completed()

    # Fica esperando com o braço levantado
    def OnSpeedtapFakeout(self, robot):
        print("OnSpeedtapFakeout")
        robot.play_anim_trigger(cozmo.anim.Triggers.OnSpeedtapFakeout).wait_for_completed()

    # Fica esperando com o braço levantado
    def OnSpeedtapIdle(self, robot):
        print("OnSpeedtapIdle")
        robot.play_anim_trigger(cozmo.anim.Triggers.OnSpeedtapIdle).wait_for_completed()

    # Irritado
    def NamedFaceInitialGreeting(self, robot):
        print("NamedFaceInitialGreeting")
        robot.play_anim_trigger(cozmo.anim.Triggers.NamedFaceInitialGreeting).wait_for_completed()

    # Ação suscinta de surpresa
    def HikingInterestingEdgeThought(self, robot):
        print("HikingInterestingEdgeThought")
        robot.play_anim_trigger(cozmo.anim.Triggers.HikingInterestingEdgeThought).wait_for_completed()
        
    # Esperando algo com ansiedade
    def CubePouncePounceNormal(self, robot):
        print("CubePouncePounceNormal")
        robot.play_anim_trigger(cozmo.anim.Triggers.CubePouncePounceNormal).wait_for_completed()

    def anim_run(self, robot):
        trigger = [self.FailedToRightFromFace]
        trigger[0](robot)
