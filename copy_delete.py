from datetime import datetime
import json

lists = []
in_file = "/home/pi/Documents/btwattch2_test/per_day/a.json"
out_file = "/home/pi/Documents/btwattch2_test/per_day/a.json"

with open (in_file, "r") as file:
    for line in file:
        data = json.loads(line)
        lists.append(data.items())
        
print(lists)

f = open(out_file, '+a')
f.write(json.dumps(lists) + "\n")
f.close