import cv2
import time

last_time=time.time()
capture=cv2.VideoCapture(0);

while(capture.isOpened()):

        _, frame=capture.read()
        print("fps:",1/(time.time()-last_time))
        last_time=time.time()
        cv2.imshow(" frame",frame)
        key=cv2.waitKey(1)
        if key== 27 & 0xFF:
                break
capture.release()
cv2.destroyAllWindows()

