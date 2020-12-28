#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from datetime import datetime
import json
import math

BASE_DIR = "/home/pi/Documents/btwattch2_test"
LOG_DIR = BASE_DIR + "/log"
PER_DAY_DIR = BASE_DIR + "/per_day"

lastweek = PER_DAY_DIR + "/" + "weekly_sum.json"
yesterday = PER_DAY_DIR + "/" + "7days_log.json"

#先週中の最大使用日

data=[]
with open(lastweek, "r") as fl:
    for l in fl:
        data.append(json.loads(l))
last_week = data[-1].get("MaxDay")
n=2
last_week_cut = math.floor(last_week*10**n) / (10**n)
print(last_week_cut)


#昨日の合計使用量
data=[]
with open(yesterday, "r") as f:
    for l in f:
        data.append(json.loads(l))
sum_yesterday = data[-1].get("sumW")
n=2
sum_yesterday_cut = math.floor(sum_yesterday*10**n) / (10**n)
print(sum_yesterday_cut)

#差
difference = sum_yesterday - last_week
n=2
difference_cut = math.floor(difference*10**n) / (10**n)
print(difference_cut)

#co2排出量とスギ
co2= difference*0.523
co2_cut = math.floor(co2*10**n) / (10**n)
sugi = co2 / 54.6
sugi_cut =math.floor(sugi*10**n) / (10**n)

#Line
if last_week  > sum_yesterday:

    url = "https://notify-api.line.me/api/notify" 
    token = "rMK2tpGpCcN7j93I4xVurPwXINyjkGZIW4Zr61dPNgX"
    headers = {"Authorization" : "Bearer "+ token}
    message = [ "昨日の電気使用量が先週の最大使用量を"+ str(difference_cut)+ "W上回りました！" + "\n" + str(difference_cut)+"Wは" +str(co2_cut) +"kgのCO2排出量であり、これはスギの木"+ str(sugi_cut) + "本分が吸収するCO2量にあたります。"]
    payload = {"message" :  message} 
    r = requests.post(url, headers = headers, params=payload) 