from datetime import datetime
import json

BASE_DIR = "/home/pi/Documents/btwattch2_test"
LOG_DIR = BASE_DIR + "/log"
PER_DAY_DIR = BASE_DIR + "/per_day"

today = datetime.strftime(datetime.today(), "%Y%m%d")
day= datetime.strftime(datetime.today(), "%a")
print(today)

in_file = LOG_DIR + "/" + today + ".json"
out_file = PER_DAY_DIR + "/" + "7days_log.json"
out_file_line = PER_DAY_DIR + "/" + "7days_log_line.json"
out_file_max = PER_DAY_DIR + "/" + "7days_log_max.json"

data = []
with open(in_file, "r") as f:
    for l in f:
        data.append(json.loads(l))


wats = [d.get("W") for d in data]
wat_total = sum(wats)
wat_average = sum(wats) / len(wats)
wat_max = max(wats)
wat_max_dt = data[wats.index(wat_max)]["datetime"]

print(wat_total)
#3つのファイルを作る

with open(out_file, '+a') as f:
    f.write('{"Date-maxtime":' +  json.dumps(wat_max_dt) + '(' + str(day) + '), "maxW":' + json.dumps(wat_max) +  ', "sumW":' + json.dumps(wat_total) +  ', "aveW":' + json.dumps(wat_average)+ '}' + "\n")

with open(out_file_line, '+a') as f:
    f.write('{"Date-maxtime":' +  json.dumps(wat_max_dt) + '(' + str(day) + '), "maxW":' + json.dumps(wat_max) +  ', "sumW":' + json.dumps(wat_total) +  ', "aveW":' + json.dumps(wat_average)+ '}' + "\n")

with open(out_file_max, '+a') as f:
    f.write('{"Date-maxtime":' +  json.dumps(wat_max_dt) + '(' + str(day) + '), "maxW":' + json.dumps(wat_max) +  ', "sumW":' + json.dumps(wat_total) +  ', "aveW":' + json.dumps(wat_average)+ '}' + "\n")


