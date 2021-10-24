import requests
from bs4 import BeautifulSoup
import xlsxwriter
from datetime import date


# comment beginning with "#" is for Mentor eyes to check features for the project requirements.
# comment beginning with "###" is for me. Mentor's can read it, but it's either a note to self
# or a feature that I'm currently working on. 
# comment beginning with "***" is current feature list.
# comment beginning with "//" is copy and pasted definition of feature to use as reference. Taken from Python Google Doc. 


# ***feature list item 4 from readme.***
# //  Implement a “scraper” that can be fed a type of file or URL and pull information off of it. // 
# //  For example, a web scraper that lets you provide any website URL and it will find certain keywords on the page. // 
# This whole thing is a web scraper but I'll point out throughout program where it actually runs.


### For some reason this code wouldn't work sitting before the xlsx workbook so I tried it here and it worked. 
### So I left it. But it doesn't get used till very end of code. 
# ***feature list item 3 from readme.***
# // Calculate and display data based on an external factor (ex: get the current date, and display how many days remaining until some event). //
# It doesn't exactly calculate but external data (todays date) is used to create the name of the Excel file. So I'm not just pulling the data
# but I'm using the data later in the program. So I wanted to place this here for Mentor Approval. 
today = date.today()
today_date_title = today.strftime("%B %d, %Y")
print(today_date_title)

print('What LEGO set/theme would you like to search?')

user_input = input()

# ***feature list item 1 from readme. (First list)***
# // Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program. //
# url_cont_list = []
# Starts as an empty list. Once a full URL is made, it appends to this list. Also when a new URL is made for each subsequent list, it is appended to this list. 
# This list isn't as important as the other lists. This is used mainly for debugging. 
url_cont_list = []

user_input_without_spaces = user_input.replace(' ','%20')
url_lego = 'https://www.lego.com'
url = "https://www.lego.com/en-us/search?q="+ user_input_without_spaces
url_cont = "https://www.lego.com/en-us/search?q="+ user_input_without_spaces
url_cont_list.append(url_cont)

# ***feature list item 1 from readme. (Second list)***
# // Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program. // 
# product_grid = [] 
# This list is is used to store the HTML <div> element of each separate Lego item. 
# It was an easy way to parse the HTML since the items didn't have id's and only classes. 
product_grid = []


# ***feature list item 2 from readme. (First function)***
# // Create and call at least 3 functions or methods, at least one of which must return a value that is used somewhere else in your code. 
# // To clarify, at least one function should be called in your code, that function should calculate, retrieve, or otherwise set the value of a variable or data structure, 
# // return a value to where it was called, and use that value somewhere else in your code. // 
# def find_next_page():
# Function finds next next page URL. It has to build the URL because the user input MUST be included in the URL because just finding the HREF doesn't load the proper page. 
# So not only does it update and store a value in global "link_href_a" but that value is used to update and store global "url_cont" so the program knows where to go next. 
# The new value stored in global "url_cont" gets used in other functions.
link_href_a = ''    
def find_next_page():
    global link_href_a
    global url_cont
    # ***feature list item 4 from readme. (First scrape)***
    # scrapes page to find next page through HREF <a> links.
    page = requests.get(url_cont)
    soup = BeautifulSoup(page.content, "html.parser")    
    results_a = soup.find("a", class_="Paginationstyles__NextLink-npbsev-10 gwMJmA")
    print(results_a)    
    if results_a != None:
        link_href_a = results_a['href']
        print(link_href_a) ### /en-us/search?page=2
        link_href_a = link_href_a.removeprefix('/en-us/search?')
        print(link_href_a) ### page=2        
        url_cont = url + '&' + link_href_a
        print('inside')
        print(link_href_a) ### page=2        
        print('inside2')
        print(url_cont) ### https://www.lego.com/en-us/search?q=harry%20potterpage=2
        url_cont_list.append(url_cont)
        find_next_page()
    else:
        pass
        ### print("All done searching! No items left\n")     
            

find_next_page()



# ***feature list item 2 from readme. (Second function)***
# // Create and call at least 3 functions or methods, at least one of which must return a value that is used somewhere else in your code. 
# // To clarify, at least one function should be called in your code, that function should calculate, retrieve, or otherwise set the value of a variable or data structure, 
# // return a value to where it was called, and use that value somewhere else in your code. // 
# def parse_this_page():
# Function parses current HTML page. It uses global variable "url_cont" to know which page to parse. It finds each separate Lego item and 
# puts content into a list "product_grid = []" 
def parse_this_page():
        ### global results
        global product_grid
        # ***feature list item 4 from readme.(Second scrape)***
        # scrapes page to find each Lego item's <ul> and <li> element to create a usable list to iterate to collect title, price, and release date.
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

                         
### parse_this_page(url_cont)


# ***feature list item 1 from readme. (Third list)***
# // Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program. //
# title_tag = []
# Starts as an empty list. This list is used to store the title of each Lego item from the parsed HTML. 
title_tag = []

# ***feature list item 2 from readme. (Third function)***
# // Create and call at least 3 functions or methods, at least one of which must return a value that is used somewhere else in your code.
# // To clarify, at least one function should be called in your code, that function should calculate, retrieve, or otherwise set the value of a variable or data structure,
# // return a value to where it was called, and use that value somewhere else in your code. // 
# def title():
# Function iterates the "product_grid = []" list to find each title of the Lego items then appends it to "title_tag = []" list.
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
        title_tag.append(no_space_suff) 
        if len(product_grid) != 1:
            index += 1
            print(index)
        else:
            pass
        

### title()


# ***feature list item 1 from readme. (Fourth list)***
# // Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program. //
# price_tag = []
# Starts as an empty list. This list is used to store the price of each Lego item from the parsed HTML. 
price_tag = []

# ***feature list item 2 from readme. (Fourth function)***
# // Create and call at least 3 functions or methods, at least one of which must return a value that is used somewhere else in your code. 
# // To clarify, at least one function should be called in your code, that function should calculate, retrieve, or otherwise set the value of a variable or data structure, 
# // return a value to where it was called, and use that value somewhere else in your code. // 
# def price():
# Function iterates the "product_grid = []" list to find each price of the Lego items then appends it to "price_tag = []" list.
def price():
    index = 0
    for html in product_grid:        
        html = product_grid[index].prettify()
        # ***feature list item 4 from readme.(Fourth scrape)***
        # scapes each item in list "product_grid = []" to find the items price. 
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

### price()

### 'oct[]' May be used for future use. I decided to keep in for now but it was to 
### add all the sets releasing Oct 1 to a special list to call upon after 
### program ran. The initial idea for this project was to collect upcoming sets for
### Oct 1 under a specific search query. I left the if else satement in the code too
### in case I want to activate this feature on a later date. 
oct = []



# ***feature list item 1 from readme. (Fifth list)***
# // Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program. //
# date_tag = []
# Starts as an empty list. This list is used to store the release date of each Lego item from the parsed HTML. 
date_tag = []

# ***feature list item 2 from readme. (Fifth function)***
# // Create and call at least 3 functions or methods, at least one of which must return a value that is used somewhere else in your code. 
# // To clarify, at least one function should be called in your code, that function should calculate, retrieve, or otherwise set the value of a variable or data structure, 
# // return a value to where it was called, and use that value somewhere else in your code. //  
# def date_function():
# Function iterates the "product_grid = []" list to find each release date of the Lego items then appends it to "price_tag = []" list.
def date_function():
    index = 0
    for html in product_grid:        
        html = product_grid[index].prettify()
        # ***feature list item 4 from readme.(Fifth scrape)***
        # scapes each item in list "product_grid = []" to find the HREF on <a> element of each item to later go into 
        # that specific items' page to pull it's release date because it isn't displayed on the main search page.  
        soup = BeautifulSoup(html, 'html.parser')

        title = soup.find("a")
        date_title = title['href']
        
        url_lego = 'https://www.lego.com'
        # ***feature list item 4 from readme.(Sixth scrape)***
        # scapes current item page to find <div> and <span> element to find items' release date. 
        page = requests.get(url_lego + date_title)
        soup = BeautifulSoup(page.content, "html.parser")        

        results_div2 = soup.find("div", class_="ProductOverviewstyles__Container-sc-1a1az6h-2 cIoioK")
        results2 = results_div2.find_all("span", class_="Markup__StyledMarkup-ar1l9g-0 hlipzx")[1]

        ### for title2 in results2:            
        ###     print(title2.text, end="\n"*2)            
        ###     oct_release = 'Coming Soon on October 1, 2021'
        ###    if title2.text == oct_release:
        ###         oct.append(title2.text)
        ###         date_tag.append(title2.text)
        ###     else:
        ###        date_tag.append(title2.text)                
        index += 1        
        date_tag.append(results2.text)  
        

### date_function()  


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


### Extra list items were being created for the date list. Haven't looked into it yet.
### So to match the other lists I had to delete those items. Luckily they all included '\n'
for duplicate in date_tag:
    if '\n' in duplicate:    
        date_tag.remove(duplicate)
    else:
        pass


print(title_tag)
print(price_tag)
print(date_tag)

print(url_cont_list)




# ***feature list item 5 from readme. (With Mentor Approval)***
# // Other features can be added to this list with mentor or staff permission, 
# but we want to see you stretch your skills, so you’ll want to pick something challenging. //
# I would like to add this for Mentor approval. The creation of an Excel file using the results of scraping pages and 
# building lists. It takes each list and iterates through it to place each index of the list into a separate Excel cell. 
# Then when finished, it labels the file using the the current date. 

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