import requests
from bs4 import BeautifulSoup
import xlsxwriter
from datetime import date


# For some reason this code wouldn't work sitting before the xlsx workbook
# so I tried it here and it worked. So I left it. But it doesn't get used 
# till very end of code. 
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
url_cont_list.append(url_cont)

# product_grid[] add the parsed html to a list. Each list item in the html li for each 
# LEGO set. It was an easy way to parse the html since the items didn't have id's and only classes. 
product_grid = []



link_href_a = ''    
def find_next_page():
    global link_href_a
    global url_cont
    page = requests.get(url_cont)
    soup = BeautifulSoup(page.content, "html.parser")    
    results_a = soup.find("a", class_="Paginationstyles__NextLink-npbsev-10 gwMJmA")
    print(results_a)    
    if results_a != None:
        link_href_a = results_a['href']
        print(link_href_a) #/en-us/search?page=2
        link_href_a = link_href_a.removeprefix('/en-us/search?')
        print(link_href_a) #page=2        
        url_cont = url + '&' + link_href_a
        print('inside')
        print(link_href_a) #page=2        
        print('inside2')
        print(url_cont) #https://www.lego.com/en-us/search?q=harry%20potterpage=2
        url_cont_list.append(url_cont)
        find_next_page()
    else:
        pass
        #print("All done searching! No items left\n")     
            

find_next_page()


def parse_this_page():
        #global results
        global product_grid
        page = requests.get(url_cont)
        soup = BeautifulSoup(page.content, "html.parser")
        
        results_div = soup.find("ul", class_="ProductGridstyles__Grid-lc2zkx-0 gxucff") 
        if results_div != None:
            results = results_div.find_all("li", class_="ProductGridstyles__Item-lc2zkx-1 dDUIzA") 
            for li_results in results:            
                product_grid.append(li_results)              
        else:  
            print('No results found. Please try another search.') 
            exit()                              

                         
#parse_this_page(url_cont)

title_tag = []
def title():
    index = 0
    for html in product_grid:        
        html = product_grid[index].prettify()
        soup = BeautifulSoup(html, 'html.parser')

        title = soup.find("span", class_='Markup__StyledMarkup-ar1l9g-0 hlipzx')
        no_space_pre = title.text.removeprefix('\n       ')
        no_space_suff = no_space_pre.removesuffix('\n      ')
        title_tag.append(no_space_suff) 
        if len(product_grid) != 1:
            index += 1
            print(index)
        else:
            pass
        

#title()

price_tag = []
def price():
    index = 0
    for html in product_grid:        
        html = product_grid[index].prettify()
        soup = BeautifulSoup(html, 'html.parser')

        title = soup.find("div", class_='ProductLeafSharedstyles__PriceRow-sc-1epu2xb-10 fEzYBd')
        no_space_pre = title.text.removeprefix('\n\n\n\n        Price\n       \n       ')
        no_space_suff = no_space_pre.removesuffix('\n      \n\n')

        index += 1
        print(index)       
        if no_space_suff == '\n':
            no_space_suff = 'N/A'
            price_tag.append(no_space_suff)
        else:
            price_tag.append(no_space_suff)

#price()

# 'oct[]' May be used for future use. I decided to keep in for now but it was to 
# add all the sets releasing Oct 1 to a special list to call upon after 
# program ran. The initial idea for this project was to collect upcoming sets for
# Oct 1 under a specific search query. I left the if else satement in the code too
# in case I want to activate this feature on a later date. 
oct = []

date_tag = []
def date_function():
    index = 0
    for html in product_grid:        
        html = product_grid[index].prettify()
        soup = BeautifulSoup(html, 'html.parser')

        title = soup.find("a")
        date_title = title['href']
        
        url_lego = 'https://www.lego.com'
        page = requests.get(url_lego + date_title)
        soup = BeautifulSoup(page.content, "html.parser")        

        results_div2 = soup.find("div", class_="ProductOverviewstyles__Container-sc-1a1az6h-2 cIoioK")
        results2 = results_div2.find_all("span", class_="Markup__StyledMarkup-ar1l9g-0 hlipzx")[1]

        # for title2 in results2:            
        #     print(title2.text, end="\n"*2)            
        #     oct_release = 'Coming Soon on October 1, 2021'
        #     if title2.text == oct_release:
        #         oct.append(title2.text)
        #         date_tag.append(title2.text)
        #     else:
        #         date_tag.append(title2.text)                
        index += 1        
        date_tag.append(results2.text)  
        

#date_function()  


print(title_tag)
print(price_tag)
print(date_tag)


for this_page in url_cont_list:    
    url_cont = this_page
    print('howdy!!!' + url_cont)
    print('howdy!!!' + this_page)
    parse_this_page()    
    title()
    price()
    date_function()
    print(product_grid[0])
    product_grid = []
    print(product_grid)
    print(title_tag)
    print(price_tag)
    print(date_tag)


# Extra list items were being created for the date list. Haven't looked into it yet.
# So to match the other lists I had to delete those items. Luckily they all included '\n'
for duplicate in date_tag:
    if '\n' in duplicate:    
        date_tag.remove(duplicate)
    else:
        pass


print(title_tag)
print(price_tag)
print(date_tag)

print(url_cont_list)


# creation of xlsx file
workbook = xlsxwriter.Workbook('LEGO search results ' + today_date_title + '.xlsx')
worksheet = workbook.add_worksheet(today_date_title)

cell_format = workbook.add_format({'bold': True})
worksheet.write('A1' , 'LEGO Set Name', cell_format)
worksheet.write('B1' , 'Price', cell_format)
worksheet.write('C1' , 'Availability', cell_format)

row = 1
column = 0
for item in title_tag:
    
    worksheet.write(row, column, item)
    row += 1

row = 1
column = 1
for item in price_tag:
    
    worksheet.write(row, column, item)
    row += 1

row = 1
column = 2
for item in date_tag:
    
    worksheet.write(row, column, item)
    row += 1

workbook.close()