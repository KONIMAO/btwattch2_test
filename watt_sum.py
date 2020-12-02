from datetime import datetime, date, timedelta
import os
import json
decoder = json.JSONDecoder()

today = datetime.today()
todaysdate = (datetime.strftime(today, '%Y%m%d'))
print(todaysdate)

filename = (datetime.strftime(today,'%Y%m%d') + '.json')
os.chdir('/home/pi/Documents/btwattch2_test/log')

lists =[]
with open (filename, 'r') as file:
    for line in file:
        data = json.load(line)
        lists.append(data["W"])
    total = sum(lists)
os.chdir('/home/pi/Documents/btwattch2_test')
f = open ('watt_per_day.json', '+a')
f.write('{"Date":' + str(todaysdate) + ', "W":' + json.dumps(total) + '}' + "\n")
print (total)
f.close()