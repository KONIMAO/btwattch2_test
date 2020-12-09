import shutil
from datetime import datetime, date, timedelta
import os
import json

os.chdir('/home/pi/Documents/btwattch2_test/per_day')
shutil.copytree('watt_weekly.json','watt_per_day.json')