from datetime import datetime
import json

#BASE_DIR = "/home/pi/Documents/btwattch2_test"
#PER_DAY_DIR = BASE_DIR + "/per_day"

in_file = "/home/pi/Documents/btwattch2_test/per_day/a.json"
#out_file = "/home/pi/Documents/btwattch2_test/per_day/a.json"

data = []
with open(in_file, "r") as f:
    for l in f:
        data.append(json.loads(l))
        
date = [d.get("Date-maxtime") for d in data]
maxW = [d.get("maxW") for d in data]
sumW = [d.get("sumW") for d in data]
aveW = [d.get("aveW") for d in data]
log = (date + maxW + sumW +aveW)
print(log)
