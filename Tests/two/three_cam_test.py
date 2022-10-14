import cv2
import time

last_time = time.time()
C_cam = cv2.VideoCapture(0)
L_cam = cv2.VideoCapture(1)
R_cam = cv2.VideoCapture(2)

while(capture.isOpened()):

    _, C_frame = C_cam.read()
    _, L_frame = L_cam.read()
    _, R_frame = R_cam.read()

    cv2.imshow(" frame", C_frame)
    cv2.imshow(" frame", L_frame)
    cv2.imshow(" frame", R_frame)

    key = cv2.waitKey(1)

    if key == 27 & 0xFF:
        break

    last_time = time.time()
    print("fps:", 1/(time.time()-last_time))

C_cam.release()
L_cam.release()
R_cam.release()

cv2.destroyAllWindows()
