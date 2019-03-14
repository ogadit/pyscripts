import csv
import sys

data = []
with open(sys.argv[1]) as f:
    cr = csv.reader(f, delimiter=',')
    for x in cr:
        data.append(x)
header = f""
for x in data[0]:
    header += f"{x:<10}"

bar = "-"*len(header)
print(bar)
print(header)
print(bar)
for x in range(len(data)):
    if x != 0:
        ps = ""
        for y in data[x]:
            ps += f"{y:<10}"
        print(ps)
