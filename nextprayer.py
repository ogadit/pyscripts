#!/usr/bin/python3

import requests
import json
import sys
import time
import datetime as dt

try:
    tjson = requests.get("http://api.aladhan.com/v1/timingsByCity?city=Karachi&country=Pakistan&method=1&school=1", timeout=2).json()["data"]["timings"]
except:
    print("Couldnt get Timings")
    exit()

ct = dt.datetime.strptime(dt.datetime.strftime(dt.datetime.now(), "%H:%M"), "%H:%M") #This was done to strip the datetime object of milliseconds and the date

currentprayer = ""
ind = 0

prayers= [
        ("Fajr", tjson["Fajr"]),
        ("Sunrise", tjson["Sunrise"]),
        ("Dhuhr", tjson["Dhuhr"]),
        ("Asr", tjson["Asr"]),
        ("Maghrib", tjson["Maghrib"]),
        ("Isha", tjson["Isha"])
        ] #Make into list
for x in range(len(prayers)): #Loop through prayer list
    t = dt.datetime.strptime(prayers[x][1], "%H:%M") #Convert string to datetime object
    if ct > t:
        currentprayer = prayers[x][0]
        ind = 0 if x==5 else x+1

if currentprayer == '':
   currentprayer = prayers[5][0]

nextprayer = prayers[ind][0] #Get the next prayer name
npt = dt.datetime.strptime(prayers[ind][1], "%H:%M") #Get the next Prayers Time

tt = npt - ct #Subtract The Prayer Time From Current Time
col = "\033[1;37;42m "
res = "\033[0;40m"
print(f"{col}{currentprayer} Time{res}")
print(f"{col}{prayers[ind][0]} in{res}")
print(f"{col}{tt.seconds//3600} {'hour' if tt.seconds//3600 == 1 else 'hours'} and {(tt.seconds//60)%60} minutes{res}")
