import os
from matplotlib import pyplot as plt
from matplotlib import dates
import datetime

IP = '217.15.20.194'
M = 1000000

def get_date(row):
    time = row[0] + '-' + row[1][0:8]
    return datetime.datetime.strptime(time, "%Y-%m-%d-%H:%M:%S")

os.system("nfdump -r nf_data > data")
f = open('data', 'r')
lines = f.read().splitlines()
f.close()

table = []
ox = []
oy = []

fmt = dates.DateFormatter('%d-%H:%M:%S')

for line in lines:
    s = ' '.join(line.split())
    table.append(s.split())

fig, ax = plt.subplots()
for i in range(1, len(table) - 4): # 4 last strings are rubbish
    if table[i][5][0:13] == IP or table[i][7][0:13] == IP:
        if table[i][12] == 'M':
            table[i][11] = float(table[i][11]) * M # million exception

        ox.append(get_date(table[i]))

        if len(oy) == 0:
            oy.append(int(table[i][11]))
        else:
            oy.append(int(table[i][11]) + oy[-1])

ax.plot(sorted(ox), sorted(oy), "-o")
ax.xaxis.set_major_formatter(fmt)

fig.autofmt_xdate()
fig.savefig('graph.png')

f = open('bill.txt', 'w')
value = int(oy[-1])
money = value / 1024 / 1024 * 0.5
f.write(str(money))
f.close()
