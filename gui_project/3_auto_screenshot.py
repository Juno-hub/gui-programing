import time
from PIL import ImageGrab

time.sleep(5)  # Waiting 5 sec : User waiting time

for i in range(1, 11):  # Save 10 images every 2 seconds
    img = ImageGrab.grab()  # Screenshot
    img.save(
        "image{}.png".format(i))  # Save to file (image1.png ~ image10.png)
    time.sleep(2)
