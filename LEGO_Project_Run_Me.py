import requests
from bs4 import BeautifulSoup
import xlsxwriter
from datetime import date
import re


#########################################
### Classes and independent Functions ###
#########################################

# Class Item holds the methods for finding the different values (title, price, and date) for each lego item on current web page.
# Each method returns a list of all the item's values that are correlating to the methods label (i.e. method labeled title returns 
# a list of all the titles from the current page) by using the Pages class to parse the page for all the matching HTML elements.
class Item:               

    def title(self): 
        titles = Pages.title_parse(self)                                     
        title_list = []
        if titles != None:
            for data in titles: 
                i = data.get_text()            
                print(i)
                if i == '':
                    i = 'N/A'
                    title_list.append(i)
                else:
                    title_list.append(i)
            return title_list
        else:
            return None
        

    def price(self):              
        prices = Pages.price_parse(self)                          
        price_list = []
        for data in prices: 
            i = data.get_text()
            x = i.removeprefix('Price')
            print(i)
            if x == '':
                x = 'N/A'
                price_list.append(x)
            else:
                price_list.append(x)
        return price_list

    # Method date has to find the date on each item's main product page because it isn't listed on the search result page. 
    # So there is a little more code than the other two methods. The program first builds a list of all the items on the 
    # current result page. Once that's done it iterates through that list and builds an URL based on each products HREF. 
    # Then the program goes to that page and parses it for the items date. It throws those dates into a list and uses that 
    # list as the return value. 
    def date(self):                
        dates = Pages.date_parse(self)
        grid = []       
        if dates != None:
            results = dates.find_all("li", class_="ProductGridstyles__Item-lc2zkx-1 dDUIzA") 
            for li_results in results:            
                grid.append(li_results)                 
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
            date_tag.append(results2.text) 
            print(results2.text)
        return date_tag
            

# Class Pages holds all the methods pertaining to URL's and for parsing the web page for HTML elements.
class Pages:  

    lego_search_url = "https://www.lego.com/en-us/search?q="   

    # Builds and returns current page's URL.
    def current_page(self):
        current_url = self.replace(' ','%20')
        url_full = Pages.lego_search_url + current_url
        return url_full

    # Builds and returns next page's URL. If next page doesn't exist, returns None.
    def find_next_page(self):        
        link_href_a = ''        
        page = requests.get(self)
        soup = BeautifulSoup(page.content, "html.parser")    
        results_a = soup.find("a", class_="Paginationstyles__NextLink-npbsev-10 gwMJmA")
        #print(results_a)  
        #print('howdy')
        #print(results_a)    
        if results_a != None:
            link_href_a = results_a['href']
            #print(link_href_a) ### /en-us/search?page=2
            link_href_a = link_href_a.removeprefix('/en-us/search?')
            #print(link_href_a) ### page=2      
            return link_href_a              
        else:
            x = 'none'
            return x            

    # Parses the page by calling all the methods in the class Item using the current page's URL as the argument. Either returns True or None.
    # Returns True if values exist or None if no values exist. 
    def parse_page(self):
        if (Item.title(self)) != None:
            title_tag.append(Item.title(self))
            price_tag.append(Item.price(self))
            date_tag.append(Item.date(self)) 
            return True
              
        else:
            #print('***')
            return None

    # Parses current web page and returns all the item's titles or None if there aren't any found titles. 
    def title_parse(self):
        page = requests.get(self)
        soup = BeautifulSoup(page.content, 'html.parser')
        title_item_div = soup.find("div", class_="SearchPagestyles__MainContainer-sc-1d2gqze-5 jFRDvz")
        if title_item_div != None:
            titles = title_item_div.find_all("span", class_="Markup__StyledMarkup-ar1l9g-0 hlipzx")
            return titles
        else:
            return None

    # Parses current web page and returns all the item's prices or None if there aren't any found prices. 
    def price_parse(self):
        page = requests.get(self)
        soup = BeautifulSoup(page.content, 'html.parser')    
        prices = soup.find_all("div", class_='ProductLeafSharedstyles__PriceRow-sc-1epu2xb-10 fEzYBd')  
        return prices 
    
    # Parses current web page and returns all the item's dates or None if there aren't any found dates. 
    def date_parse(self):
        page = requests.get(self)
        soup = BeautifulSoup(page.content, "html.parser")        
        dates = soup.find("ul", class_="ProductGridstyles__Grid-lc2zkx-0 gxucff") 
        return dates

# Intro function to prompt user what set/theme they would like to use to search. Uses user input to create a URL and returns the URL. 
def intro():    
    user_input = input('What LEGO set/theme would you like to search?\n')
    url_full = Pages.current_page(user_input)
    print(url_full)
    return url_full

# This function is to prompt an error message if the user's input didn't return any results then calls the intro function to keep program looping. 
def intro_loop():
    print("No results found. Let's try another search")    
    url_full = intro()
    return url_full



################################
### Main program starts here ###
################################



# All the different lists being used for the programs output.
product_grid = []
title_tag = []
price_tag = []
date_tag = []

url_full = intro()
while Pages.parse_page(url_full) is None:
    #print('1')
    url_full = intro_loop()
    #print('3')
#print('2')
user_input = url_full.removeprefix('https://www.lego.com/en-us/search?q=')
user_input = user_input.replace('%20','_')
link_href_a = Pages.find_next_page(url_full)
url_cont = url_full + '&' + link_href_a
print(url_cont)
while url_cont != (url_full + '&' + 'none'):
    # print('wha')
    # print(url_cont)
    # print('whaddup')
    Pages.parse_page(url_cont)    
    link_href_a = Pages.find_next_page(url_cont) #######    
    #print(price_tag)
    #print(title_tag)
    #print(date_tag)    
    # print(url_cont)
    url_cont = url_full + '&' + link_href_a
    print(url_cont)
    # print(url_cont)
    # print('whaddup2')
else:
    #print('done')
    pass
        

# print(price_tag)
# print(title_tag)
# print(url_cont)
print('Done searching!')  
print('Now Creating XLSX results file...')


### Today's date
today = date.today()
today_date_title = today.strftime("%B_%d_%Y")
#print(today_date_title)


### Creation of xlsx file
workbook = xlsxwriter.Workbook('LEGO.com_search_results_for_' + user_input.upper() + '_on_' + today_date_title + '.xlsx')
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

print('File Ready!')