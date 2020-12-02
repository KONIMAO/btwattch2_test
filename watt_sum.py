from datetime import datetime, date, timedelta
#import time
import json
decoder = json.JSONDecoder()

lists =[]

with open ('/home/pi/Documents/btwattch2_test/log/20201125.json') as file:
    for line in file:
        data = json.load(line)
        lists.append(data["W"])
    total = sum(lists)

    f = open ('watt_per_day.json', '+a')
    f.write(json.dumps(total) + "\n")
    f.close()
    print (total)