import cv2
import numpy as np
import os
import time

from hsv_mod import balls
from findContours import find_coun
from get_bin import clear

file_name = "fotos/7.jpg"
image = cv2.imread(file_name)

img_bin, image = balls(image)

img_bin, image = clear(img_bin, image)

img_bin, image = find_coun(img_bin, image)

cv2.imshow('res',img_bin)
cv2.imshow('image',image)
cv2.waitKey()