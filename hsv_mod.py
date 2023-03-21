import cv2
import numpy as np
import os
import time

def balls(image,save:bool = False):
    img = image
    h,w,_=img.shape
    img=cv2.resize(img,(w,h))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )

    h1 = 0
    s1 = 158
    v1 = 109
    h2 = 180
    s2 = 255
    v2 = 255

    h_min = np.array((h1, s1, v1), np.uint8)
    h_max = np.array((h2, s2, v2), np.uint8)
    img_bin = cv2.inRange(hsv, h_min, h_max)

    #ch = cv2.waitKey(5)
    if save:
        t = time.time()
        cv2.imwrite(f"images/{t}.jpg", img_bin)
        res = []
        res.append(t, img_bin)
        return res

    return img_bin, image