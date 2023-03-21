import cv2
import numpy as np
dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
from hsv_mod import balls
cv2.namedWindow("res")
cv2.namedWindow("image")

def get_img():
    image = cv2.imread('fotos/7.jpg')
    return balls(image), image
    
def find_coun(img_bin, image):
    img_bin,image = img_bin,image

    
    coords=[]
    # height, width, _ = img.shape
    # input_pt = np.array(coords)
    # output_pt = np.array([[0, 0], [width, 0],[width, height],[0, height]])
    # h, _ = cv2.findHomography(input_pt, output_pt)
    # res_img = cv2.warpPerspective(img, h, (width, height))
    # hsv = cv2.cvtColor(res_img, cv2.COLOR_BGR2HSV)
    # cv2.imshow('h',hsv[:,:,0])
    # cv2.imshow('s',hsv[:,:,1])
    cv2.imshow('bin',img_bin)
    _, contours, hierarchy= cv2.findContours(img_bin,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours( image, contours, -1, (255,0,0),
                      3, cv2.LINE_AA, hierarchy, 1 )
    return img_bin, image
