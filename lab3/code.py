#!/usr/bin/python3
import os
from docxtpl import DocxTemplate #pip3 install docxtpl

os.system('cd ../lab1/ && python3 code.py')
f = open('../lab1/bill.txt', 'r')
telephone_bill = float(f.read())
f.close()
os.system('cd ../lab2/ && python3 code.py')
f = open('../lab2/bill.txt', 'r')
internet_bill = float(f.read())
f.close()
bill = round(internet_bill + telephone_bill, 2)

CONTEXT = {'number': '78054852', 
'date': '25.05.2020', 
'bank': 'АО "Альфа-Банк"', 
'bik': '044525225', 
'inn': '7707083893', 
'kpp': '773601001', 
'bill1': '1027700132195', 
'bill2': '1027700132196', 
'supplier': 'АО «ЭР-Телеком Холдинг»', 
'customer': 'Винокуров Илья Сергеевич', 
'base': 'Договор об оказании услуг связи от 02.02.2019', 
'service': 'Интернет и телефония', 
'scount': '1', 
'sed': '1', 
'price': f'{bill}', 
'finsum': f'{bill}', 
'nds': '13%', 
'oplata': f'{bill}', 
'director': 'Винокуров Ильяс Сергеевич', 
'accountant': 'Винокуров Илуа Сергеевич'}

doc = DocxTemplate('template.docx')
doc.render(CONTEXT)
doc.save('final.docx')
os.system('abiword --to=pdf final.docx 2>errors.txt') # sudo apt-get install abiword
os.system('rm final.docx')
