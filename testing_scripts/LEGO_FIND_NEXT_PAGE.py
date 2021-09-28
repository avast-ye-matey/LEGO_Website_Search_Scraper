import requests
from bs4 import BeautifulSoup
import xlsxwriter
from datetime import date


print('What would you like to search?')

user_input = input()

user_input_without_spaces = user_input.replace(' ','%20')
url_lego = 'https://www.lego.com'
url = "https://www.lego.com/en-us/search?q="+ user_input_without_spaces
url_cont = "https://www.lego.com/en-us/search?q="+ user_input_without_spaces








url_cont_list = []
link_href_a = ''    
def find_next_page():
    global link_href_a
    global url_cont
    page = requests.get(url_cont)
    soup = BeautifulSoup(page.content, "html.parser")
    #print(page.text)
    results_a = soup.find("a", class_="Paginationstyles__NextLink-npbsev-10 gwMJmA")
    print(results_a)
    #****print(results_a, file=f)
    #sys.stdout.write(results_a)
    #f.write(results_a + '\n')
    #results = results_div.find_all("span", class_="Markup__StyledMarkup-ar1l9g-0 hlipzx") 
    if results_a != None:
        link_href_a = results_a['href']
        print(link_href_a) #/en-us/search?page=2
        link_href_a = link_href_a.removeprefix('/en-us/search?')
        print(link_href_a) #page=2        
        url_cont = url + '&' + link_href_a
        print('inside')
        print(link_href_a) #page=2
        #print(link_href_a, file=f) #page=2
        #sys.stdout.write(link_href_a)
        #f.write(link_href_a + '\n')
        print('inside2')
        print(url_cont) #https://www.lego.com/en-us/search?q=harry%20potterpage=2
        #parse_this_page(url_cont)
        #title()
        #price()
        #date_function()
        url_cont_list.append(url_cont)
        find_next_page()

    else:
        print("All done searching! No items left\n")
        #print("All done searching!\n", file=f)
        #sys.stdout.write('done')
        #f.write('done\n')

find_next_page()

print(url_cont_list)