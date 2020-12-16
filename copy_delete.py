import json
import os

in_file = "/home/pi/Documents/btwattch2_test/per_day/watt_weekly.json"
out_file = "/home/pi/Documents/btwattch2_test/per_day/watt_per_day.json"
with open(in_file, "r") as f:
    data = f.readlines()
        
with open(out_file, "a+") as f:
    f.writelines(data)
    
os.remove(in_file)