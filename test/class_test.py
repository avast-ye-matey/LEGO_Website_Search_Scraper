import requests
from bs4 import BeautifulSoup
import xlsxwriter
from datetime import date


class Items:
    def __init__(self, title, price, date):
        self.title = title
        self.price = price
        self.date = date

class URL:
    #url = "https://www.lego.com/en-us/search?q="
    # def __init__(self, main, cont):
    #     self.main = main
    #     self.cont = cont
    def current_page(self):
        current_url = self.replace(' ','%20')
        url_full = "https://www.lego.com/en-us/search?q=" + current_url
        return url_full
    
    
    # url = "https://www.lego.com/en-us/search?q="+ self.main

    # user_input_without_spaces = user_input.replace(' ','%20')
    # url_lego = 'https://www.lego.com'
    # url = "https://www.lego.com/en-us/search?q="+ user_input_without_spaces
    # url_cont = "https://www.lego.com/en-us/search?q="+ user_input_without_spaces
    # url_cont_list.append(url_cont)


print('What LEGO set/theme would you like to search?')
user_input = input()
url_full = URL.current_page(user_input)
print(url_full)

product_grid = []
page = requests.get(url_full)
soup = BeautifulSoup(page.content, "html.parser")        
results_div = soup.find("ul", class_="ProductGridstyles__Grid-lc2zkx-0 gxucff") 
if results_div != None:
    results = results_div.find_all("li", class_="ProductGridstyles__Item-lc2zkx-1 dDUIzA") 
    for li_results in results:            
        product_grid.append(li_results)              
else:  
        print('No results found. Please try another search.') 
        exit()   

#print(product_grid)

# for item in product_grid:
title_tag = []
def title():
    index = 0
    for html in product_grid:        
        html = product_grid[index].prettify()
        # ***feature list item 4 from readme.(Third scrape)***
        # scapes each item in list "product_grid = []" to find the items title. 
        soup = BeautifulSoup(html, 'html.parser')

        title = soup.find("span", class_='Markup__StyledMarkup-ar1l9g-0 hlipzx')
        no_space_pre = title.text.removeprefix('\n       ')
        no_space_suff = no_space_pre.removesuffix('\n      ')
        #title_tag.append(no_space_suff) 
        return no_space_suff
        if len(product_grid) != 1:            
            index += 1
            print(index)
            return no_space_suff
            
        else:
            pass
        

title_tag.append(title())
print(title_tag)