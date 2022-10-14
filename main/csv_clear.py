import pandas as pd
import os

os.chdir("frames")
df = pd.DataFrame(columns=["counter", "img_src",
                  "throttle", "steering", "ping"])
df.to_csv("data.csv", index=False)
