import cv2 

capture=cv2.VideoCapture(0)
#0 is for default camera 1 is for the external camera

while True:
    ret,frame=capture.read()
    if not ret:
        break
    cv2.imshow("video",frame)
    keys=cv2.waitKey(10)
    if keys== 27:
        break
