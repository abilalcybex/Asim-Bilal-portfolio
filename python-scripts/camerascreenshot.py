import cv2
import numpy as np
from PIL import ImageGrab
import time

def open_camera():
    cap = cv2.VideoCapture(0)

    start_time = time.time()
    while True:
        ret, frame = cap.read()
        cv2.imshow('Camera', frame)

        if cv2.waitKey(1) & 0xFF == ord('q') or time.time() - start_time >= 5:
            break

    cap.release()
    cv2.destroyAllWindows()

def take_screenshot():
    screenshot = ImageGrab.grab()
    screenshot.save('screenshot.png')  

if __name__ == '__main__':
    open_camera()
    take_screenshot()
