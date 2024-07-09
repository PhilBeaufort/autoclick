
import pyautogui
import time
import keyboard

def click(): 
    time.sleep(0.1)     
    pyautogui.click()

while not keyboard.is_pressed('esc'):
    click()