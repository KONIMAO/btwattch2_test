import json
import os
from datetime import datetime, timedelta

in_file = "/home/pi/Documents/btwattch2_test/per_day/7days_log.json"
in_file_line = "/home/pi/Documents/btwattch2_test/per_day/7days_log_line.json"
in_file_max = "/home/pi/Documents/btwattch2_test/per_day/7days_log_max.json"
out_file = "/home/pi/Documents/btwattch2_test/per_day/watt_per_day.json"
week_file= "/home/pi/Documents/btwattch2_test/per_day/weekly_sum.json"

#一週間のログをコピー＆バックアップファイルにペースト
with open(in_file, "r") as f:
    data = f.readlines()
        
with open(out_file, "a+") as f:
    f.writelines(data)

#一週間のW合計値をファイルに書き込み 
today = datetime.today()
last_week = today - timedelta(weeks=1)
print(last_week)

data = []
with open(in_file, "r") as file:
    for l in file:
        data.append(json.loads(l))

wats = [d.get("sumW") for d in data]

wat_total = sum(wats)
print(wat_total)

with open(week_file, '+a') as f:
     f.write('{"Date": "' +  str(last_week) + ' ~ '+ str(today)+ '", "sumW": ' + json.dumps(wat_total) + '}' + "\n")

#一週間のログファイルを削除
os.remove(in_file)
os.remove(in_file_line)
os.remove(in_file_max)