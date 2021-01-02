import time
import keyboard
from PIL import ImageGrab


def screenshot():
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time))  # ex) image_20210102_134030.png


keyboard.add_hotkey("enter", screenshot)

keyboard.wait("esc")