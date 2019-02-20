#!/bin/python

import requests
from bs4 import BeautifulSoup

print(" "*20 + "CAR REGISTRATION CHECKER (SINDH)\n\n")

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
print("Number Plate: %s" % num_plate)
print("Owner Name: %s" % owner)
print("Make: %s" % make)
print("Horsepower: %s" % hp)
print("\n\n" + " "*20 + "THANKYOU FOR USING THIS SOFTWARE\nMade by osama")
