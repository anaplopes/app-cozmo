import time
import cozmo
from cozmo.objects import CustomObject, CustomObjectMarkers, CustomObjectTypes


def handle_object_appeared(evt, **kw):
    # This will be called whenever an EvtObjectAppeared is dispatched -
    # whenever an Object comes into view.
    if isinstance(evt.obj, CustomObject):
        print("Cozmo started seeing a %s" % str(evt.obj.object_type))


def handle_object_disappeared(evt, **kw):
    # This will be called whenever an EvtObjectDisappeared is dispatched -
    # whenever an Object goes out of view.
    if isinstance(evt.obj, CustomObject):
        print("Cozmo stopped seeing a %s" % str(evt.obj.object_type))


def custom_objects(robot: cozmo.robot.Robot):
    # Add event handlers for whenever Cozmo sees a new object
    robot.add_event_handler(cozmo.objects.EvtObjectAppeared, handle_object_appeared)
    robot.add_event_handler(cozmo.objects.EvtObjectDisappeared, handle_object_disappeared)

    # define a unique cube (44mm x 44mm x 44mm) (approximately the same size as a light cube)
    # with a 30mm x 30mm Diamonds2 image on every face
    cube_obj = robot.world.define_custom_cube(CustomObjectTypes.CustomType00,
                                              CustomObjectMarkers.Diamonds2,
                                              44,
                                              30, 30, True)


    if cube_obj is not None:
        print("All objects defined successfully!")
    else:
        print("One or more object definitions failed!")
        return

    print("Show the above markers to Cozmo and you will see the related objects "
          "annotated in Cozmo's view window, you will also see print messages "
          "everytime a custom object enters or exits Cozmo's view.")

    print("Press CTRL-C to quit")
    while True:
        time.sleep(0.1)


cozmo.run_program(custom_objects, use_3d_viewer=True, use_viewer=True)
