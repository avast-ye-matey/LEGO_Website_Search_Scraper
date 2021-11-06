import requests
from bs4 import BeautifulSoup
import xlsxwriter
from datetime import date


today = date.today()
today_date_title = today.strftime("%B %d, %Y")
print(today_date_title)

print('What LEGO set/theme would you like to search?')

user_input = input()


url_cont_list = []

user_input_without_spaces = user_input.replace(' ','%20')
url_lego = 'https://www.lego.com'
url = "https://www.lego.com/en-us/search?q="+ user_input_without_spaces
url_cont = "https://www.lego.com/en-us/search?q="+ user_input_without_spaces
# url_cont_list.append(url_cont)


product_grid = []


# x=url
# y = url_cont
link_href_a = ''    
def find_next_page(x, url_cont):
    #global link_href_a
    #global url_cont    
    page = requests.get(url_cont)
    soup = BeautifulSoup(page.content, "html.parser")    
    results_a = soup.find("a", class_="Paginationstyles__NextLink-npbsev-10 gwMJmA")
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
        #url_cont_list.append(url_cont)
        return url_cont
        find_next_page()
    else:
        pass
        ### print("All done searching! No items left\n")     

# find_next_page(url_cont, link_href_a)        
#     if url_cont_list != None:
#         find_next_page().append(url_cont)
#     else

# url

print(1)
print(url_cont)
url_cont_list.append(find_next_page(url, url_cont))
print(find_next_page(url, url_cont))
print(2)
print(url_cont)
print(url_cont_list)
