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
            pyautogui.click(button_location)
            return True
        else:
            return False
    except Exception as e:
        return False

# Specify the path to your image
button_image = 'slow_download.png'

# Run the function in a loop until Esc key is pressed
while True:
    if keyboard.is_pressed('esc'):
        print("Esc key pressed. Exiting.")
        break
    found = click_button(button_image)
    if found:
        print("Button clicked!")
    time.sleep(0.5)  # Wait before trying again