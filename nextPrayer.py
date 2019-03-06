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

ct = dt.datetime.strftime(dt.datetime.now(), "%H:%M")

currentprayer = ""
ind = 0

prayers= [
        ("Fajr", tjson["Fajr"]),
        ("Dhuhr", tjson["Dhuhr"]),
        ("Asr", tsjon["Asr"]),
        ("Maghrib", tjson["Maghrib"]),
        ("Isha", tjson["Isha"])
        ]
for x in len(prayers):
    t = dt.datetime.strp
