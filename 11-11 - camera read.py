import cv2

cv2.namedWindow("preview")
cam = cv2.VideoCapture(0)#0 - номер камеры

if cam.isOpened():
    read_ok, image = cam.read()
else:
    read_ok = False

while read_ok:
    cv2.imshow("preview", image)
    read_ok, image = cam.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

cam.release()
cv2.destroyWindow("preview")
