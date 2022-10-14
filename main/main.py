import last_line
import os
import time
import cv2
import pandas_store
import tx_data
import check_perif
import driver_module
import cleanup

cleanup.cleanem()

last_time = time.time()
C_cam = cv2.VideoCapture(0)
L_cam = cv2.VideoCapture(1)
R_cam = cv2.VideoCapture(2)

os.chdir("frames")

try:
    count = last_line.get_last_line()
    count += 1
except:
    count = 1

while(C_cam.isOpened() and L_cam.isOpened() and R_cam.isOpened()):  # 1
    _, C_frame = C_cam.read()
    cv2.imshow("Center Frame", C_frame)  # 2
    cv2.imshow("Left Frame", L_frame)
    cv2.imshow("Right Frame", R_frame)
    key = cv2.waitKey(1)

    throttle, steering, ping = tx_data.get_data()

    print(count, " fps: ", fps, " throttle: ", throttle,
          " steering: ", steering, " ping: ", ping)

    cv2.imwrite("frame_C_%d.jpg" % count, C_frame)
    cv2.imwrite("frame_L_%d.jpg" % count, L_frame)
    cv2.imwrite("frame_R_%d.jpg" % count, R_frame)

    driver_module.drive(throttle, steering)

    pandas_store.store_data(count, "frame_srd_%d.jpg" %
                            count, throttle, steering, ping)
    count += 1

    if key == 27 & 0xFF:
        break

    if key == 80 & 0xFF:
        response = input("<<<<<<<: Resume training?")
        if(response == "N" or response == "n"):
            break

    fps = 1/(time.time()-last_time)
    last_time = time.time()

driver_module.stop()
cleanup.cleanem()
os.chdir("..")
C_cam.release()
L_cam.release()
R_cam.release()
cv2.destroyAllWindows()
