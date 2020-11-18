import time
import cozmo
from cozmo.objects import CustomObject, CustomObjectMarkers, CustomObjectTypes


status = None

class View:

    def __init__(self):
        self.status = status


    def view_object_status(self):
        return self.status


    def handle_object_appeared(self, evt, **kw):
        # EvtObjectAppeared is dispatched

        if isinstance(evt.obj, CustomObject):
            global status
            status = True
            #print("Cozmo started seeing a %s" % str(evt.obj.object_type))


    def handle_object_disappeared(self, evt, **kw):
        # EvtObjectDisappeared is dispatched
        
        if isinstance(evt.obj, CustomObject):
            global status 
            status = False
            #print("Cozmo stopped seeing a %s" % str(evt.obj.object_type))


    def view_run(self, robot):
        robot.add_event_handler(cozmo.objects.EvtObjectAppeared, self.handle_object_appeared)
        robot.add_event_handler(cozmo.objects.EvtObjectDisappeared, self.handle_object_disappeared)

        cube_obj = robot.world.define_custom_cube(CustomObjectTypes.CustomType00,
                                                CustomObjectMarkers.Diamonds2,
                                                16, 15, 15, True)

        if cube_obj is not None:
            print("All objects defined successfully!")
        else:
            print("One or more object definitions failed!")

        time.sleep(1)
