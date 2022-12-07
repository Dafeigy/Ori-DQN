from config import *
from utils import ActionInfo
import keys
import time

controller = keys.Keys()





# move action
@ActionInfo
def move_left(controller):
    controller.directKey(LEFT)
    time.sleep(0.5)
    controller.directKey(LEFT,controller.key_release)

@ActionInfo
def move_right(controller):
    controller.directKey(RIGHT)
    time.sleep(0.5)
    controller.directKey(RIGHT,controller.key_release)

@ActionInfo
def move_up(controller):
    controller.directKey(UP)
    time.sleep(0.5)
    controller.directKey(UP,controller.key_release)

@ActionInfo
def move_down(controller):
    controller.directKey(DOWN)
    time.sleep(0.5)
    controller.directKey(DOWN,controller.key_release)

# basic action
@ActionInfo
def _Attack(controller):
    controller.directKey(ATTACK)
    time.sleep(0.005)
    controller.directKey(ATTACK,controller.key_release)




class Actor():
    def __init__(self, actionlist:list) -> None:
        self.actionlist = actionlist
        self.model = None
    
    def take_action(self,id:int):
        return self.actionlist[id]


class Ori():
    def __init__(self,) -> None:
        self.name = 'Filia'
        self.moveActor = Actor(move_list)
        self.basicActor = Actor(basic_list)







