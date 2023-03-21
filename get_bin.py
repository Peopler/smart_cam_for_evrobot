import cv2
import numpy as np


def clear(img_bin, image):
    kernel = np.ones((5, 5), 'uint8')
    img_bin = cv2.erode(img_bin, kernel, iterations=3)
    img_bin = cv2.dilate(img_bin, kernel, iterations=3)
    return img_bin, image
    
