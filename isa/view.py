import time
import cozmo
from cozmo.objects import CustomObject, CustomObjectMarkers, CustomObjectTypes


status = None

def view_object_status():
    return status


def handle_object_appeared(evt, **kw):
    # EvtObjectAppeared is dispatched

    if isinstance(evt.obj, CustomObject):
        global status
        status = True
        #print("Cozmo started seeing a %s" % str(evt.obj.object_type))


def handle_object_disappeared(evt, **kw):
    # EvtObjectDisappeared is dispatched
    
    if isinstance(evt.obj, CustomObject):
        global status
        status = False
        #print("Cozmo stopped seeing a %s" % str(evt.obj.object_type))


def view_run(robot):
    robot.add_event_handler(cozmo.objects.EvtObjectAppeared, handle_object_appeared)
    robot.add_event_handler(cozmo.objects.EvtObjectDisappeared, handle_object_disappeared)

    cube_obj = robot.world.define_custom_cube(CustomObjectTypes.CustomType00,
                                            CustomObjectMarkers.Diamonds2,
                                            15, 15, 15, True)

    if cube_obj is not None:
        print("All objects defined successfully!")
    else:
        print("One or more object definitions failed!")

    time.sleep(1)
