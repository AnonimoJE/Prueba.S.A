#!/usr/bin/python

import pyautogui
import os
from time import sleep

sleep(2)

pyautogui.hotkey( "shift", "ctrl", "Q")
pyautogui.press( "enter")
sleep(2)

pyautogui.hotkey( "win", "l")

sleep(2)

pyautogui.press( "enter")
sleep(1)
pyautogui.write( "klausmikaelson25")
sleep(1)
pyautogui.press( "enter")

sleep(2)

pyautogui.hotkey( "win", "t")
sleep(2)
pyautogui.write( "sudo su")
sleep(2)
pyautogui.press( "enter")
sleep(1)
pyautogui.write( "klausmikaelson25")
sleep(1)
pyautogui.press( "enter")
sleep(1)
pyautogui.write( "ls")
sleep(1)
pyautogui.press( "enter")











