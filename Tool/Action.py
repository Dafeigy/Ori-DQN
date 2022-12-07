# Define the actions we may need during training
# You can define your actions here

from Tool.SendKey import PressKey, ReleaseKey
from Tool.WindowsAPI import grab_screen
import time
import cv2
import threading

# Hash code for key we may use: https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes?redirectedfrom=MSDN
UP_ARROW = 0x57
DOWN_ARROW = 0x53
LEFT_ARROW = 0x41
RIGHT_ARROW = 0x44

L_SHIFT = 0xA0
L_CTRL=0xA2
SPACE=0x20
LCLICK = 0x01


# move actions
# 0
def Nothing():
    ReleaseKey(LEFT_ARROW)
    ReleaseKey(RIGHT_ARROW)
    time.sleep(0.01)
    pass


# Move
# 0
def Move_Left():
    ReleaseKey(RIGHT_ARROW)
    PressKey(LEFT_ARROW)
    time.sleep(0.01)


# 1
def Move_Right():
    ReleaseKey(LEFT_ARROW)
    PressKey(RIGHT_ARROW)
    time.sleep(0.01)


# 2
def Turn_Left():
    ReleaseKey(RIGHT_ARROW)
    PressKey(LEFT_ARROW)
    time.sleep(0.01)
    ReleaseKey(LEFT_ARROW)


# 3
def Turn_Right():
    ReleaseKey(LEFT_ARROW)
    PressKey(RIGHT_ARROW)
    time.sleep(0.01)
    ReleaseKey(RIGHT_ARROW)


# ----------------------------------------------------------------------

# other actions
# Attack
# 0
def Attack():
    PressKey(LCLICK)
    time.sleep(0.05)
    ReleaseKey(LCLICK)
    time.sleep(0.01)


# 1
def Attack_Down():
    PressKey(DOWN_ARROW)
    PressKey(LCLICK)
    time.sleep(0.05)
    ReleaseKey(LCLICK)
    ReleaseKey(DOWN_ARROW)
    time.sleep(0.01)

def Attack_Up():
    # print("Attack up--->")
    PressKey(UP_ARROW)
    PressKey(LCLICK)
    time.sleep(0.05)
    ReleaseKey(LCLICK)
    ReleaseKey(UP_ARROW)
    time.sleep(0.01)
# JUMP
# 3
def Jump():
    PressKey(SPACE)
    time.sleep(0.05)
    ReleaseKey(SPACE)

def Dash():
    PressKey(L_CTRL)
    time.sleep(0.2)
    ReleaseKey(L_CTRL)
#############################


# List for action functions
Actions = [Attack, Attack_Down, Attack_Up,
           Short_Jump, Mid_Jump, Skill, Skill_Up,
           Skill_Down, Rush, Cure]
Directions = [Move_Left, Move_Right, Turn_Left, Turn_Right]


# Run the action
def take_action(action):
    Actions[action]()


def take_direction(direc):
    Directions[direc]()


class TackAction(threading.Thread):
    def __init__(self, threadID, name, direction, action):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.direction = direction
        self.action = action

    def run(self):
        take_direction(self.direction)
        take_action(self.action)