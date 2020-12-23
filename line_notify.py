#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from datetime import datetime
import json


#今日の合計
BASE_DIR = "/home/pi/Documents/btwattch2_test"
LOG_DIR = BASE_DIR + "/log"
PER_DAY_DIR = BASE_DIR + "/per_day"

today = datetime.strftime(datetime.today(), "%Y%m%d")
day= datetime.strftime(datetime.today(), "%a")

today_file = LOG_DIR + "/" + today + ".json"
thisweek = PER_DAY_DIR + "/" + "7days_log.json"
lastweek = PER_DAY_DIR + "/" + "weekly_sum.json"
data = []
with open(today_file, "r") as f:
    for l in f:
        data.append(json.loads(l))

wats = [d.get("W") for d in data]
wat_today= sum(wats)

#今週の昨日までの合計
data=[]
with open(thisweek, "r") as file:
    for l in file:
        data.append(json.loads(l))

watt = [d.get("sumW") for d in data]
total_yesterday = sum(watt)


#今週の合計値（今日と昨日までの合計）
this_week = wat_today + total_yesterday
print(this_week)

#先週の合計
data=[]
with open(lastweek, "r") as fl:
    for l in fl:
        data.append(json.loads(l))
last_week = data[-1].get("sumW")
print(last_week)

if this_week > last_week:

    url = "https://notify-api.line.me/api/notify" 
    token = "rMK2tpGpCcN7j93I4xVurPwXINyjkGZIW4Zr61dPNgX"
    headers = {"Authorization" : "Bearer "+ token}
    message =  " 先週より使いすぎ！" 
    payload = {"message" :  message} 
    r = requests.post(url, headers = headers, params=payload) 
