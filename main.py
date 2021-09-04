# import the necessary packages
import numpy as np
import cv2
from mss import mss
import time
from pynput.mouse import Controller, Button

mouse = Controller()

bounding_box = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}

screen_shotter = mss()

while True:
    screenshot_raw = screen_shotter.grab(bounding_box)
    screenshot_rgb = np.array(screenshot_raw)
    screenshot_gray = cv2.cvtColor(screenshot_rgb, cv2.COLOR_BGR2GRAY)

    template = cv2.imread('spider_title.png', 0)
    # template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    width, height = template.shape[::-1]

    resolution = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.7
    locations = np.where(resolution >= threshold)

    for point in zip(*locations[::-1]):
        cv2.rectangle(screenshot_rgb, point, (point[0] + width, point[1] + height), (0, 255, 255), 2)

        print(f'x1 {point[0]}, x2 {point[0] + width}, y1 {point[1]}, y2 {point[1] + height}')

        print('The current pointer position is {0}'.format(mouse.position))
        mouse.position = (point[0] + 20, point[1] + 42)
        print('The current pointer position is {0}'.format(mouse.position))
        time.sleep(0.5)
        mouse.press(Button.left)
        time.sleep(0.2)
        mouse.release(Button.left)
        time.sleep(5)

    # cv2.imshow('Detected', screenshot_rgb)
    #
    # if (cv2.waitKey(1) & 0xFF) == ord('q'):
    #     cv2.destroyAllWindows()
    #     break
