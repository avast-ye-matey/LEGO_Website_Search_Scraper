import requests
from bs4 import BeautifulSoup
import xlsxwriter
from datetime import date
import re


html = 'https://www.lego.com/en-us/search?q=santa'
page = requests.get(html)
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.find("div", class_='ProductLeafSharedstyles__PriceRow-sc-1epu2xb-10 fEzYBd')
toots = soup.find_all("span", class_='Text__BaseText-sc-178efqu-0 cVmQPV ProductPricestyles__StyledText-vmt0i4-0 eGdbAY')
hotdog = soup.find("div", class_="SearchPagestyles__MainContainer-sc-1d2gqze-5 jFRDvz")
squirt = hotdog.find_all("span", class_='Markup__StyledMarkup-ar1l9g-0 hlipzx')
#gil = toots.text
#print(gil)
#print(toots)

list = []
# htmldata = getdata("https://www.geeksforgeeks.org/how-to-automate-an-excel-sheet-in-python/?ref=feed") 
# soup = BeautifulSoup(htmldata, 'html.parser') 
# data = '' 
for data in toots: 
    i = data.get_text()
    x = i.removeprefix('Price')
    list.append(x)
    #print(x) 

#print(list)

list2 = []
for data in squirt: 
    i = data.get_text()
    print(i)
    x = i.removeprefix('Price')
    if x == '':
        x = 'N/A'
        list2.append(x)
    else:
        list2.append(x)
    #print(x) 

print(list2)

# if no_space_suff == '\n':
#             no_space_suff = 'N/A'
#             price_tag.append(no_space_suff)
#         else:
#             price_tag.append(no_space_suff)