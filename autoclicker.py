
import pyautogui
import time
import keyboard

def click_button(image_path, confidence=0.8):
    # Locate the button on the screen
    button_location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
    if button_location:
        # Click the button
        pyautogui.click(button_location)
        return True
    return False

# Specify the path to your image
button_image = 'slow_download.png'

# Run the function
while not keyboard.is_pressed('esc'):
    found = click_button(button_image)
    if found:
        print("Button clicked!")
        break
    time.sleep(0.5)  # Wait before trying again