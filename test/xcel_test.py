import requests
from bs4 import BeautifulSoup
import xlsxwriter
from datetime import date
import re


title_tag = [[1,2,3],[4,5,6],[7,8,9,10]]
print(type(title_tag))
print(len(title_tag))
print(len(title_tag[2]))


for item in title_tag:  
    for butts in item:  
        print(butts)
        # if type(item) == list:
        #     print('yeah')
        # else:
        #     print('no')

today = date.today()
today_date_title = today.strftime("%B %d, %Y")
print(today_date_title)
### creation of xlsx file
workbook = xlsxwriter.Workbook('LEGO search results ' + today_date_title + '.xlsx')
worksheet = workbook.add_worksheet(today_date_title)

cell_format = workbook.add_format({'bold': True})
worksheet.write('A1' , 'LEGO Set Name', cell_format)
worksheet.write('B1' , 'Price', cell_format)
worksheet.write('C1' , 'Availability', cell_format)

row = 1
column = 0
for item in title_tag:    
    for butts in item:  
        worksheet.write(row, column, butts)        
        row += 1




# row = 1
# column = 1
# for item in price_tag:
    
#     worksheet.write(row, column, item)
#     row += 1

# row = 1
# column = 2
# for item in date_tag:
    
#     worksheet.write(row, column, item)
#     row += 1

workbook.close()