import cv2
import numpy as np


def get_coords(image,x_size_mm,y_size_mm):
    contours, hierarchy = cv2.findContours(image,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    centers = []
    frames = []
    height, width = image.shape
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        frames.append((x, y, w, h))
        x_center = x + w // 2
        y_center = y + h // 2
        x_mm = x_size_mm*x_center//width
        y_mm = y_size_mm - (y_size_mm*y_center//height)
        centers.append((x_mm,y_mm))
    return centers, frames
