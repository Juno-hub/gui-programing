import os
import time
import keyboard
from PIL import ImageGrab

i = 1


def screenshot():
    current_time = time.strftime("%Y-%m-%d")
    image = ImageGrab.grab()
    folder = "스크린샷"
    file_name = "./{0}/{1}.png".format(folder, current_time)

    if os.path.exists(folder):
        pass
    else:
        os.makedirs(folder)

    if os.path.exists(file_name):
        global i
        image.save("./{0}/{1} ({2}).png".format(folder, current_time, i))
        i += 1
    else:
        image.save(file_name)


keyboard.add_hotkey("enter", screenshot)
keyboard.wait("esc")