import cv2
import os
import time

cv2.namedWindow("preview")
cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)#0 - номер камеры
cam.set(3,1920)
cam.set(4,1080)

if cam.isOpened():
    read_ok, image = cam.read()
    if not os.path.isdir('images'):#проверяем наличие папки
        os.mkdir ('images')# если нет, создаем
else:
    read_ok = False

while read_ok:
    cv2.imshow("preview", image)
    read_ok, image = cam.read()
    key = cv2.waitKey(20)
    if key == 32:
        cv2.imwrite(f"images/{time.time()}.jpg", image)
        print(f"File: images/{time.time()}.jpg saved")
    if key == 27: # exit on ESC
        break

cam.release()
cv2.destroyWindow("preview")
