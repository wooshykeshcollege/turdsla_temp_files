import tx_data
import random
import pandas as pd
print(">>>>>Pandas_store successfully imported")
#count, "frame%d.jpg" %count, throttle, steering, ping


def store_data(count, img_src, throttle, steering, ping):
    file = open("data.csv", "a")
    file.write(str(count)+","+str(img_src)+","+str(throttle)+"," +
               str(steering)+","+str(ping)+"\n")
    file.close()
