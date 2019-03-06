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

ct = dt.datetime.strptime(dt.datetime.strftime(dt.datetime.now(), "%H:%M"), "%H:%M") #This was done to strip the datetime object of milliseconds and the date

currentprayer = ""
ind = 0

prayers= [
        ("Fajr", tjson["Fajr"]),
        ("Dhuhr", tjson["Dhuhr"]),
        ("Asr", tjson["Asr"]),
        ("Maghrib", tjson["Maghrib"]),
        ("Isha", tjson["Isha"])
        ] #Make into list
for x in range(len(prayers)): #Loop through prayer list
    t = dt.datetime.strptime(prayers[x][1], "%H:%M") #Convert string to datetime object
    if ct > t:
        currentprayer = prayers[x][0]
        ind = 0 if x==4 else x+1



nextprayer = prayers[ind][0] #Get the next prayer name
npt = dt.datetime.strptime(prayers[ind][1], "%H:%M") #Get the next Prayers Time

tt = npt - ct #Subtract The Prayer Time From Current Time

print(f"It is time for {currentprayer} \nNext prayer is {prayers[ind][0]} in {tt.seconds//3600} hours and {(tt.seconds//60)%60} minutes")
