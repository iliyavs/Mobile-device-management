import csv

TEL_NUM = "915783624"
TARIFF_PARAMETERS = {
    'koutcall':2,
    'kincall':0,
    'ksms':1,
    'freesms':10
    }

def csvread():
    outcall = incall = [0, 0, 0, 0, 0]
    file = open('data.csv')
    reader = csv.reader(file)
    for row in reader:
        if row[1] == TEL_NUM:
            outcall = row
        if row[2] == TEL_NUM:
            incall = row
    return outcall, incall

def tariff(outcall, incall, koutcall, kincall, k):
    minuteout = float(outcall[3])
    minutein = float(incall[3])
    sms = int(outcall[4])
    sms = max(0, sms - TARIFF_PARAMETERS["freesms"])
    bill = minuteout * koutcall + minutein * kincall + sms * k
    return bill

outcall, incall = csvread()
if outcall != [0, 0, 0, 0, 0] or incall != [0, 0, 0, 0, 0]:
    bill = tariff(outcall, incall, TARIFF_PARAMETERS["koutcall"], TARIFF_PARAMETERS["kincall"], TARIFF_PARAMETERS["ksms"])
else:
    bill = 0
f = open('bill.txt', 'w')
f.write(str(bill))
f.close()
