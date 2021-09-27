import requests
from bs4 import BeautifulSoup
import xlsxwriter
from datetime import date




today = date.today()
today_date_title = today.strftime("%B %d, %Y")
print(today_date_title)



print('What would you like to search?')
#print('What would you like to search?', file=f)
user_input = input()
#f.write(user_input)
#f.write('\n'*2)
user_input_without_spaces = user_input.replace(' ','%20')
url_lego = 'https://www.lego.com'
url = "https://www.lego.com/en-us/search?q="+ user_input_without_spaces
url_cont = "https://www.lego.com/en-us/search?q="+ user_input_without_spaces

#url_UL = <ul class="ProductGridstyles__Grid-lc2zkx-0 gxucff">
#url_LI = <li data-test="product-item" class="ProductGridstyles__Item-lc2zkx-1 dDUIzA">
#url_A_Title&Link = <a data-test="product-leaf-title-link" href="/en-us/product/santa-s-sleigh-40499"><h2 color="black" data-test="product-leaf-title" class="Text__BaseText-sc-178efqu-0 fUTvnf ProductLeafSharedstyles__Title-sc-1epu2xb-9 iqocOo"><span class="Markup__StyledMarkup-ar1l9g-0 hlipzx">Santa's Sleigh</span></h2></a>
#url_DIV_Price = <div data-test="product-leaf-price" class="ProductLeafSharedstyles__PriceRow-sc-1epu2xb-10 fEzYBd"><div class="ProductPricestyles__Wrapper-vmt0i4-1 dEqmbq"><span data-test="product-price" class="Text__BaseText-sc-178efqu-0 cVmQPV ProductPricestyles__StyledText-vmt0i4-0 eGdbAY"><span class="VisuallyHidden-sc-1dwqwvm-0 gREPpa">Price</span>$36.99</span></div></div>

product_grid = []

def parse_this_page(url_cont):
        global results
        global product_grid
        page = requests.get(url_cont)
        soup = BeautifulSoup(page.content, "html.parser")
        #print(page.text)
        results_div = soup.find("ul", class_="ProductGridstyles__Grid-lc2zkx-0 gxucff") #item main group
        results = results_div.find_all("li", class_="ProductGridstyles__Item-lc2zkx-1 dDUIzA") #item block
        #results_title = results.find("a", class_='Text__BaseText-sc-178efqu-0 fUTvnf ProductLeafSharedstyles__Title-sc-1epu2xb-9 iqocOo')
        #results_price = results.find("div", class_='ProductLeafSharedstyles__PriceRow-sc-1epu2xb-10 fEzYBd')
        for li_results in results:
            #print(li_results.text)
            #li_results = results.find("a", class_='Text__BaseText-sc-178efqu-0 fUTvnf ProductLeafSharedstyles__Title-sc-1epu2xb-9 iqocOo')
            #print(li_results.text)
            #results_price = results.find("div", class_='ProductLeafSharedstyles__PriceRow-sc-1epu2xb-10 fEzYBd')
            product_grid.append(li_results)
            #for title in results_title:
                #print(title.text)
                #print(li_results)
                #li_results = li_results.text
            #for price in results_price:
                #print(price.text)
                #print(li_results.text)
                #print(li_results.text)

#def parse_each_item():
    #global product_grid
    #for title in product_grid:
        #soup = BeautifulSoup(product_grid[0], 'html.parser')
        #title = soup.find("a", class_='Text__BaseText-sc-178efqu-0 fUTvnf ProductLeafSharedstyles__Title-sc-1epu2xb-9 iqocOo')
        #print(title.text)
        


        

parse_this_page(url_cont)

#print(product_grid[0].prettify())
#html =product_grid[0].prettify()***************

#[x.prettify() for x in product_grid]

#print(product_grid)

title_tag = []
def title():
    index = 0
    for html in product_grid:
        #index = 0
        html = product_grid[index].prettify()

        soup = BeautifulSoup(html, 'html.parser')

        title = soup.find("span", class_='Markup__StyledMarkup-ar1l9g-0 hlipzx')
        no_space_pre = title.text.removeprefix('\n       ')
        no_space_suff = no_space_pre.removesuffix('\n      ')
        #no_space2 = title.removesuffix('')
        #print(title.strip())
        index += 1
        print(index)
        title_tag.append(no_space_suff)   #.strip())

title()

price_tag = []
def price():
    index = 0
    for html in product_grid:
        #index = 0
        html = product_grid[index].prettify()

        soup = BeautifulSoup(html, 'html.parser')

        title = soup.find("div", class_='ProductLeafSharedstyles__PriceRow-sc-1epu2xb-10 fEzYBd')
        no_space_pre = title.text.removeprefix('\n\n\n\n        Price\n       \n       ')
        no_space_suff = no_space_pre.removesuffix('\n      \n\n')
        #i = title.text
        
        #print(no_space.lstrip())
        index += 1
        print(index)
        #numbers = '1', '2', '3', '4', '5', '6','7','8','9','0'
        #if no_space_suff.find('1', '2', '3', '4', '5', '6','7','8','9','0') != str:
        if no_space_suff == '\n':
            no_space_suff = 'N/A'
            price_tag.append(no_space_suff)
        else:
            price_tag.append(no_space_suff)

price()



oct = []
date_tag = []
def date_function():
    index = 0
    for html in product_grid:
        #index = 0
        html = product_grid[index].prettify()

        soup = BeautifulSoup(html, 'html.parser')

        title = soup.find("a")
        date_title = title['href']
        #no_space_pre = title.text.removeprefix('\n       ')
        #no_space_suff = no_space_pre.removesuffix('\n      ')
        #no_space2 = title.removesuffix('')
        #print(title.strip())
        url_lego = 'https://www.lego.com'
        page = requests.get(url_lego + date_title)

        soup = BeautifulSoup(page.content, "html.parser")
        #print(page.text)

        results_div2 = soup.find("div", class_="ProductOverviewstyles__Container-sc-1a1az6h-2 cIoioK")
        results2 = results_div2.find_all("span", class_="Markup__StyledMarkup-ar1l9g-0 hlipzx")[1]

        for title2 in results2:
            #print(title.prettify(), end="\n")
            #print(title, end="\n"*2)
            print(title2.text, end="\n"*2)
            #print(title2.text, end="\n"*2, file=f)
            #sys.stdout.write(title2.text, end="\n"*2)
            #f.write(title2.text + '\n')
            oct_release = 'Coming Soon on October 1, 2021'
            if title2.text == oct_release:
                oct.append(title2.text)
                date_tag.append(title2.text)
            else:
                date_tag.append(title2.text)

                #pass
        index += 1
        #print(index)
        date_tag.append(title.text)   #.strip())

date_function()
for duplicate in date_tag:
    if '\n' in duplicate:    
        date_tag.remove(duplicate)
    else:
        pass




# page = requests.get(url_cont)
# soup = BeautifulSoup(page.content, "html.parser")
# results_div = soup.find("ul", class_="ProductGridstyles__Grid-lc2zkx-0 gxucff") #item main group
# results = results_div.find_all("li", class_="ProductGridstyles__Item-lc2zkx-1 dDUIzA")
# html = results_div.prettify()
# print(html)




print(title_tag)
print(price_tag)
print(date_tag)


# final_results = zip( price_tag , title_tag )
# print(final_results)

# print ('Zip:')
# for x, y in map(None, title_tag, price_tag):
#     print (x, y)


# def final_list(n):
#     return n + n

# result_final = map(final_list , )

#print(index)


#title = soup.find("a")
#print(title.string)


#parse_each_item()
#print(product_grid)
#print(len(product_grid))


workbook = xlsxwriter.Workbook('LEGO search results ' + today_date_title + '.xlsx')
worksheet = workbook.add_worksheet(today_date_title)

#cell_format = workbook.add_format()
#cell_format.set_font_size(15)
cell_format = workbook.add_format({'bold': True})
#cell_format = workbook.add_format({'font_size': 15})
#bold.set_font_size(15)
#cell_format.set_bold
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