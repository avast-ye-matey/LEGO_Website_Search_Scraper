import requests
from bs4 import BeautifulSoup
import xlsxwriter
from datetime import date
import re

link_href_a = ''
url_cont = 'https://www.lego.com/en-us/search?q=star%20wars'
url_cont_list = []

def find_next_page():
    global link_href_a
    global url_cont
    global url_cont_list
    
    x = 'https://www.lego.com/en-us/search?q=star%20wars'
    #url_cont = 'https://www.lego.com/en-us/search?q=star%20wars'
    #url = 'https://www.lego.com/'
    # ***feature list item 4 from readme. (First scrape)***
    # scrapes page to find next page through HREF <a> links.
    page = requests.get(url_cont)
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
        url_cont = x + '&' + link_href_a
        print('inside')
        print(link_href_a) ### page=2        
        print('inside2')
        print(url_cont) ### https://www.lego.com/en-us/search?q=harry%20potter&page=2
        url_cont_list.append(url_cont)
        find_next_page()
    else:
        pass
        ### print("All done searching! No items left\n")   
        # 
        # 
find_next_page()  
            