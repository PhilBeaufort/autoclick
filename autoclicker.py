from pynput.mouse import Button, Controller
import pyautogui
import keyboard
import time
import cv2

def click_button(image_path, confidence=0.8):
    try:
        # Locate the button on the screen
        button_location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
        if button_location:
            # Click the button
            secondary_mouse.position = button_location
            secondary_mouse.click(Button.left, 1)
            return True
        else:
            return False
    except Exception as e:
        return False

# Specify the path to your image
button_image = 'slow_download.png'

# Create a secondary mouse controller
secondary_mouse = Controller()

# Run the function in a loop until Esc key is pressed
while True:
    if keyboard.is_pressed('esc'):
        print("Esc key pressed. Exiting.")
        break
    found = click_button(button_image)
    if found:
        print("Button clicked!")
    time.sleep(0.5)  # Wait before trying again