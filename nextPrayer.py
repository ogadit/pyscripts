#!/data/data/com.termux/files/usr/bin/python

import requests
import json
import sys
import time
import datetime as dt

try:
    tjson = requests.get("http://api.aladhan.com/v1/timingsByCity?city=Karachi&country=Pakistan&method=1&school=1").json()["data"]["timings"]
except:
    print("Couldnt get Timings")
    exit()

ct = dt.datetime.strptime(dt.datetime.strftime(dt.datetime.now(), "%H:%M"), "%H:%M")

currentprayer = ""
ind = 0

prayers= [
        ("Fajr", tjson["Fajr"]),
        ("Dhuhr", tjson["Dhuhr"]),
        ("Asr", tjson["Asr"]),
        ("Maghrib", tjson["Maghrib"]),
        ("Isha", tjson["Isha"])
        ]
for x in range(len(prayers)):
    t = dt.datetime.strptime(prayers[x][1], "%H:%M")
    if ct > t:
        currentprayer = prayers[x][0]
        ind = x
if ind is 4:
    ind = 0
else:
    ind += 1

print(currentprayer)
print(prayers[ind][0])
