#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import os
from time import sleep

c = os.get_terminal_size().columns
bar = "="*c

def title():
    os.system("clear")
    print(bar)
    print(f"{'CAR REGISTRATION CHECKER':^{c}}")
    print(bar)
    print()
    print()

title()
num = input("Please enter number plate: ")

print("\nGetting Data\n")

page = requests.post("http://excise.gos.pk/vehicle/vehicle_result", data = {"wheelers_type": "1", "reg_no": num})

soup = BeautifulSoup(page.content, 'html.parser')

veh_det = soup.select("div.veh_det_box h6")
num_plate = veh_det[0].get_text()
make = "%s %s %s" % (veh_det[1].get_text(), veh_det[6].get_text(), veh_det[8].get_text())
hp = veh_det[12].get_text()
owner = veh_det[7].get_text()

print("Data Retrieved\n\n")
sleep(1)
title()
print(f"{'Number Plate':<15}{num_plate:<20}")
print(f"{'Owner Name':<15}{owner:<20}")
print(f"{'Make':<15}{make:<20}")
print(f"{'Horsepower':<15}{hp:<20}")
print()
print()
print(bar)
print(f"{'THANKYOU FOR USING THIS SOFTWARE':^{c}}")
print(f"{'MADE BY OSAMA':^{c}}")
print(bar)
input()
os.system('clear')
