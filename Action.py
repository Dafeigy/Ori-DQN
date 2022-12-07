# Define the actions we may need during training
# You can define your actions here

from Tool.SendKey import PressKey, ReleaseKey
from Tool.WindowsAPI import grab_screen
import time
import cv2
import threading

# Hash code for key we may use: https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes?redirectedfrom=MSDN
W = 0x57
A = 0x41
S = 0x53
D = 0x44
Space = 0x20
L_SHIFT = 0xA0
L_CTRL= 0xA2
E = 0x45
Left_Click= 0x01


# move actions
# 0
def Nothing():
    ReleaseKey(A)
    ReleaseKey(D)
    pass
# Move
# 0
def Move_Left():
    PressKey(A)
    time.sleep(0.01)


# 1
def Move_Right():
    PressKey(D)
    time.sleep(0.01)


# 2
def Turn_Left():
    PressKey(A)
    time.sleep(0.01)
    ReleaseKey(A)


# 3
def Turn_Right():
    PressKey(D)
    time.sleep(0.01)
    ReleaseKey(D)


# ----------------------------------------------------------------------

# other actions
# Attack
# 0
def Attack():
    PressKey(Left_Click)
    time.sleep(0.15)
    ReleaseKey(Left_Click)
    Nothing()
    time.sleep(0.01)


# 1
# def Attack_Down():
#     PressKey(DOWN_ARROW)
#     PressKey(X)
#     time.sleep(0.05)
#     ReleaseKey(X)
#     ReleaseKey(DOWN_ARROW)
#     time.sleep(0.01)
# 1
def Attack_Up():
    # print("Attack up--->")
    PressKey(W)
    PressKey(Left_Click)
    time.sleep(0.11)
    ReleaseKey(Left_Click)
    ReleaseKey(W)
    Nothing()
    time.sleep(0.01)


# JUMP
# 2
def Short_Jump_left():
    PressKey(Space)
    PressKey(A)
    time.sleep(0.5)
    ReleaseKey(Space)
    ReleaseKey(A)
def Short_Jump_Right():
    PressKey(Space)
    PressKey(D)
    time.sleep(0.5)
    ReleaseKey(Space)
    ReleaseKey(D)
# 3
def Long_Jump_Left():
    PressKey(A)
    PressKey(Space)
    time.sleep(0.56)
    ReleaseKey(Space)
    time.sleep()
    PressKey(Space)
    time.sleep(0.2)
    ReleaseKey(X)
    ReleaseKey(C)
    Nothing()


# Skill
# 4
# def Skill():
#     PressKey(Z)
#     PressKey(X)
#     time.sleep(0.1)
#     ReleaseKey(Z)
#     ReleaseKey(X)
#     time.sleep(0.01)
# 4
def Skill_Up():
    PressKey(UP_ARROW)
    PressKey(Z)
    PressKey(X)
    time.sleep(0.15)
    ReleaseKey(UP_ARROW)
    ReleaseKey(Z)
    ReleaseKey(X)
    Nothing()
    time.sleep(0.15)


# 5
def Skill_Down():
    PressKey(DOWN_ARROW)
    PressKey(Z)
    PressKey(X)
    time.sleep(0.2)
    ReleaseKey(X)
    ReleaseKey(DOWN_ARROW)
    ReleaseKey(Z)
    Nothing()
    time.sleep(0.3)


# Rush
# 6
def Rush():
    PressKey(L_CTRL)
    time.sleep(0.1)
    ReleaseKey(L_CTRL)

# Cure
def Cure():
    PressKey(E)
    time.sleep(1.4)
    ReleaseKey(A)
    time.sleep(0.1)


# Restart function
# it restart a new game
# it is not in actions space
def Look_up():
    PressKey(UP_ARROW)
    time.sleep(0.1)
    ReleaseKey(UP_ARROW)


def restart():
    station_size = (230, 230, 1670, 930)
    while True:
        station = cv2.resize(cv2.cvtColor(grab_screen(station_size), cv2.COLOR_RGBA2RGB), (1000, 500))
        if station[187][300][0] != 0:
            time.sleep(1)
        else:
            break
    time.sleep(1)
    Look_up()
    time.sleep(1.5)
    Look_up()
    time.sleep(1)
    while True:
        station = cv2.resize(cv2.cvtColor(grab_screen(station_size), cv2.COLOR_RGBA2RGB), (1000, 500))
        if station[187][612][0] > 200:
            # PressKey(DOWN_ARROW)
            # time.sleep(0.1)
            # ReleaseKey(DOWN_ARROW)
            PressKey(C)
            time.sleep(0.1)
            ReleaseKey(C)
            break
        else:
            Look_up()
            time.sleep(0.2)


# List for action functions
Actions = [Attack, Attack_Up,Short_Jump, Mid_Jump, Skill_Up,Skill_Down, Rush, Cure]

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