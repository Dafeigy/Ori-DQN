# -*- coding: utf-8 -*-
import win32process#进程模块
from win32con import PROCESS_ALL_ACCESS #Opencress 权限
import win32api#调用系统模块
import ctypes#C语言类型
from win32gui import FindWindow#界面
import time
from ctypes import *
#内存访问需寻找，现在凑合用着
def GetProcssID(address,bufflength):
    pid = ctypes.c_ulong()
    kernel32 = ctypes.windll.LoadLibrary("kernel32.dll")
    hwnd = FindWindow(None,u"OriAndTheWilloftheWisps")
    ReadProcessMemory = kernel32.ReadProcessMemory
    hpid, pid = win32process.GetWindowThreadProcessId(hwnd)
    hProcess = win32api.OpenProcess(PROCESS_ALL_ACCESS, False, pid)
    addr = ctypes.c_ulong()
    Data=float(0)
    ReadProcessMemory(int(hProcess), ctypes.c_void_p(address), ctypes.byref(addr), bufflength, None)
    win32api.CloseHandle(hProcess)
    return addr.value

def convert(s):
    i = int(s, 10)                   # convert from hex to a Python int
    cp = pointer(c_int(i))           # make this into a c integer
    fp = cast(cp, POINTER(c_float))  # cast the int pointer to a float pointer
    return fp.contents.value
def main():
    sun = str(GetProcssID(0x1D5344BB6C4,4))
    print ("Hp:%d" % convert(sun))
if __name__ == '__main__':
    while(1):
        main()
        time.sleep(0.5)


