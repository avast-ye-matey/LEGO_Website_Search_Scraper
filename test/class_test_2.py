import requests
from bs4 import BeautifulSoup
import xlsxwriter
from datetime import date
import re


class Item:

    # def __init__(self, title, price, date):
    #     self.title = title_tag.append(Item.title(html))
    #     self.price = price_tag.append(Item.price(html))
    #     self.date =              

    def title(self):                          
        page = requests.get(self)
        soup = BeautifulSoup(page.content, 'html.parser')
        title_item_div = soup.find("div", class_="SearchPagestyles__MainContainer-sc-1d2gqze-5 jFRDvz")
        title = title_item_div.find_all("span", class_="Markup__StyledMarkup-ar1l9g-0 hlipzx")
        
        title_list = []
        for data in title: 
            i = data.get_text()            
            print(i)
            if i == '':
                i = 'N/A'
                title_list.append(i)
            else:
                title_list.append(i)
        return title_list
        

    def price(self):                         
        #html = 'https://www.lego.com/en-us/search?q=santa'
        page = requests.get(self)
        soup = BeautifulSoup(page.content, 'html.parser')    
        squirt = soup.find_all("div", class_='ProductLeafSharedstyles__PriceRow-sc-1epu2xb-10 fEzYBd')       
               
        price_list = []
        for data in squirt: 
            i = data.get_text()
            x = i.removeprefix('Price')
            print(i)
            if x == '':
                x = 'N/A'
                price_list.append(x)
            else:
                price_list.append(x)
        return price_list


    def date(self):                
        
        grid = []
        x = 'https://www.lego.com/en-us/search?q=santa'
        page = requests.get(self)
        soup = BeautifulSoup(page.content, "html.parser")
        
        results_div = soup.find("ul", class_="ProductGridstyles__Grid-lc2zkx-0 gxucff") 
        if results_div != None:
            results = results_div.find_all("li", class_="ProductGridstyles__Item-lc2zkx-1 dDUIzA") 
            for li_results in results:            
                grid.append(li_results)              
        else:  
            print('No results found. Please try another search.') 
            exit()    

        date_tag = []
        index = 0
        for html in grid:        
            html = grid[index].prettify()            
            soup = BeautifulSoup(html, 'html.parser')
            title = soup.find("a")
            date_title = title['href']            
            url_lego = 'https://www.lego.com'            
            page = requests.get(url_lego + date_title)
            soup = BeautifulSoup(page.content, "html.parser")        

            results_div2 = soup.find("div", class_="ProductOverviewstyles__Container-sc-1a1az6h-2 cIoioK")
            results2 = results_div2.find_all("span", class_="Markup__StyledMarkup-ar1l9g-0 hlipzx")[1]
                          
            index += 1     
            #return results2.text    ##########
            date_tag.append(results2.text)  ###################
            print(results2.text)
        return date_tag
            

class URL:  

    html = 'https://www.lego.com/en-us/search?q=santa'
    page = requests.get(html)
    soup = BeautifulSoup(page.content, 'html.parser')    
    squirt = soup.find_all("div", class_='ProductLeafSharedstyles__PriceRow-sc-1epu2xb-10 fEzYBd')   
    
    def current_page(self):
        current_url = self.replace(' ','%20')
        url_full = "https://www.lego.com/en-us/search?q=" + current_url
        return url_full

    def find_next_page(self):        
        link_href_a = ''        
        page = requests.get(self)
        soup = BeautifulSoup(page.content, "html.parser")    
        results_a = soup.find("a", class_="Paginationstyles__NextLink-npbsev-10 gwMJmA")
        print(results_a)  
        print('howdy')
        print(results_a)    
        if results_a != None:
            link_href_a = results_a['href']
            print(link_href_a) ### /en-us/search?page=2
            link_href_a = link_href_a.removeprefix('/en-us/search?')
            print(link_href_a) ### page=2      
            return link_href_a  
            url_cont = self + '&' + link_href_a
            print('inside')
            print(link_href_a) ### page=2        
            print('inside2')
            print(url_cont) ### https://www.lego.com/en-us/search?q=harry%20potter&page=2
            #url_cont_list.append(url_cont)
            #find_next_page()
            return url_cont
        else:
            x = 'none' #done = print("done!")
            return x
            #pass
            ### print("All done searching! No items left\n")   
            # 
            # 
    #find_next_page()     
    def parse_page(x):
        title_tag.append(Item.title(x))
        price_tag.append(Item.price(x))
        date_tag.append(Item.date(x))     

print('What LEGO set/theme would you like to search?')
user_input = input()
url_full = URL.current_page(user_input)
print(url_full)

product_grid = []
title_tag = []
price_tag = []
date_tag = []

html = 'https://www.lego.com/en-us/search?q=santa'

# def parse_page(x, y):
#     title_tag.append(Item.title(x))
#     price_tag.append(Item.price(x))
#     date_tag.append(Item.date(y))

URL.parse_page(url_full)

link_href_a = URL.find_next_page(url_full)
#url_cont = URL.find_next_page(url_full)
url_cont = url_full + '&' + link_href_a
if url_cont != (url_full + '&' + 'none'):
    print('wha')
    print(url_cont)
    print('whaddup')
    URL.parse_page(url_cont)
    #title_tag.append(Item.title(url_cont))
    #price_tag.append(Item.price(url_cont))
    #date_tag.append(Item.date(url_full))
    link_href_a = URL.find_next_page(url_cont) #######    
    print(price_tag)
    print(title_tag)
    print(date_tag)
    print(url_cont)
    url_cont = url_full + '&' + link_href_a
    print(url_cont)
    print('whaddup2')
else:
    print('done')
    
    

print('done!')
print(price_tag)
print(title_tag)
print(url_cont)
    



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
    for sub_items in item:  
        worksheet.write(row, column, sub_items)        
        row += 1

row = 1
column = 1
for item in price_tag:
    for sub_items in item:  
        worksheet.write(row, column, sub_items)
        row += 1

row = 1
column = 2
for item in date_tag:
    for sub_items in item:  
        worksheet.write(row, column, sub_items)
        row += 1

workbook.close()