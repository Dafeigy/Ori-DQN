import keyboard
import time
while 1:
    keyboard.wait(hotkey='space')
    a=time.time()
    keyboard.wait(hotkey='space')
    b=time.time()
    print(b-a)
