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
thisweek = PER_DAY_DIR + "/" + "7days_log_achieve.json"

#先週の平均

data=[]
with open(lastweek, "r") as fl:
    for l in fl:
        data.append(json.loads(l))
last_week = data[-1].get("sumW")
last_week_ave = last_week / 7 
n=2
last_week_ave_cut = math.floor(last_week_ave*10**n) / (10**n)
print(last_week_ave_cut)

#先々週の平均

data=[]
with open(lastweek, "r") as fl:
    for l in fl:
        data.append(json.loads(l))
last_week2 = data[-2].get("sumW")
last_week2_ave = last_week2 / 7 
n=2
last_week2_ave_cut = math.floor(last_week2_ave*10**n) / (10**n)
print(last_week2_ave_cut)



#今週の平均
data=[]
with open(thisweek, "r") as f:
    for l in f:
        data.append(json.loads(l))
this_week = [d.get("sumW") for d in data]
this_week_ave = sum(this_week) / len(this_week)

n=2
this_week_ave_cut = math.floor(this_week_ave*10**n) / (10**n)
print(this_week_ave_cut)

#先週との差と節約した金額

difference = last_week_ave_cut - this_week_ave_cut
save_money = difference * 0.00859 * 7
n=2
save_money_cut = math.floor(save_money*10**n) / (10**n)
print(save_money_cut)

if last_week2_ave_cut  > last_week_ave_cut > this_week_ave_cut:

    url = "https://notify-api.line.me/api/notify" 
    token = "rMK2tpGpCcN7j93I4xVurPwXINyjkGZIW4Zr61dPNgX"
    headers = {"Authorization" : "Bearer "+ token}
    message = [ "2週連続で前週の平均値を下回っています！"+ "\n"+ "この調子でいけば、先週と比べて"+ str(save_money_cut)+ "円を節約できます。引き続き、節電を頑張りましょう！" ]
    payload = {"message" :  message} 
    r = requests.post(url, headers = headers, params=payload)
    
    with open(thisweek, '+a') as f:
        f.write('Notify Done' )