# import the necessary packages
import numpy as np
import cv2
from mss import mss

bounding_box = {'top': 100, 'left': 0, 'width': 1920, 'height': 1080}

screen_shotter = mss()

while True:
    screenshot_raw = screen_shotter.grab(bounding_box)
    screenshot_rgb = np.array(screenshot_raw)
    screenshot_gray = cv2.cvtColor(screenshot_rgb, cv2.COLOR_BGR2GRAY)

    template = cv2.imread('green_spider_down_1_64x64.png', 0)
    width, height = template.shape[::-1]

    resolution = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.5
    locations = np.where(resolution >= threshold)

    for point in zip(*locations[::-1]):
        cv2.rectangle(screenshot_rgb, point, (point[0] + width, point[1] + height), (0, 255, 255), 2)

    cv2.imshow('Detected', screenshot_rgb)

    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break
