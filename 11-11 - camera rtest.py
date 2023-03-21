import cv2

for i in range(10):
    cam = cv2.VideoCapture(i)#0 - номер камеры
    read_ok, image = cam.read()
    print(i,read_ok)

