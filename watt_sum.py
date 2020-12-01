#from datetime import datetime, date, timedelta
#import time
import json
res = []
decoder = json.JSONDecoder()

with open ('/home/pi/Documents/btwattch2_test/log/20201125.json') as file:
    for line in file:
        data = json.load(line)
        lists =[]
        lists.append(data["W"])
        print(sum(lists))
        