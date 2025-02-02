import pyautogui
import keyboard
import time
import cv2

def click_button(image_path, confidence=0.8):
    try:
        # Locate the button on the screen
        button_location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
        if button_location:
            # Save the current position of the primary mouse
            current_position = pyautogui.position()
            # Move to the button location and click
            pyautogui.click(button_location)
            # Move the primary mouse back to its original position
            pyautogui.moveTo(current_position)
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