import pytesseract
from time import perf_counter, sleep
from PIL import ImageGrab
import os
from pynput import mouse,keyboard

from utils.preprocess_image import preprocess_image


def perform_ocr():
    # Create a mouse controller
    controller = mouse.Controller()

    # Get the current position of the mouse cursor
    os.system("say 'Move to first position' &")
    sleep(5)
    x1, y1 = controller.position
    print(x1,y1)
    os.system("say 'move to next position' &")
    sleep(5)


    # Get the current position of the mouse cursor
    x2, y2 = controller.position
    print(x2,y2)
    os.system("say 'Done' &")

    # Calculate the bounding box of the selected region
    x1, y1, x2, y2 = map(int, (x1, y1, x2, y2))
    bbox = (min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))

    # Take a screenshot of the selected region
    screenshot = ImageGrab.grab(bbox=bbox)

    # Save the screenshot to a file
    screenshot_file = os.path.join(os.path.dirname(__file__), "screenshot.png")
    screenshot.save(screenshot_file)
    preprocess_image('screenshot.png', 'screenshot.png')

    # Perform OCR on the screenshot
    text = pytesseract.image_to_string(screenshot_file)
    
    return text

def type_character(char):
    # Create a keyboard controller
    controller = keyboard.Controller()

    # Type the character
    controller.press(char)
    controller.release(char)

# Wait 5 seconds
start_time = perf_counter()
while perf_counter() - start_time < 5:
    pass

# Perform OCR on the selected region of the screen
text = perform_ocr()
print(text)
text =text.replace("\n", " ")


# Type each character of the sentence
for char in text:
    # Wait a short amount of time between each character
    start_time = perf_counter()
    while perf_counter() - start_time < 0.01:
        pass
    type_character(char)