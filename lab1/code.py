import csv

def csvread():
    file = open('data.csv')
    reader = csv.reader(file)
    for row in reader:
        if row[1] == '915783624':
            outcall = row
        if row[2] == '915783624':
            incall = row
    return outcall, incall

def tariff(outcall, incall, koutcall, kincall, k):
    minuteout = float(outcall[3])
    minutein = float(incall[3])
    sms = int(outcall[4])
    sms -= 10
    if sms < 0: sms = 0
    bill = minuteout*koutcall + minutein*kincall + sms*k
    return bill
    
outcall, incall = csvread()
koutcall = 2               # Выставим
kincall = 0                # параметры 
ksms = 1                   # тарифа
bill = tariff(outcall, incall, koutcall, kincall, ksms)
f = open('bill.txt', 'w')
f.write(str(bill))
f.close()
