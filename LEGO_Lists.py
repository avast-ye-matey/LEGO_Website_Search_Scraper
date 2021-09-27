import requests
from bs4 import BeautifulSoup
import xlsxwriter


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




date_tag = []
def date():
    index = 0
    for html in product_grid:
        #index = 0
        html = product_grid[index].prettify()

        soup = BeautifulSoup(html, 'html.parser')

        title = soup.find("span", class_='Text__BaseText-sc-178efqu-0 ListingProductstyles__ActionText-sc-1p6pmbg-1 dEjyWi')
        date_title = title.text
        #no_space_pre = title.text.removeprefix('\n       ')
        #no_space_suff = no_space_pre.removesuffix('\n      ')
        #no_space2 = title.removesuffix('')
        #print(title.strip())
        index += 1
        print(index)
        date_tag.append(date_title)   #.strip())

date()



# page = requests.get(url_cont)
# soup = BeautifulSoup(page.content, "html.parser")
# results_div = soup.find("ul", class_="ProductGridstyles__Grid-lc2zkx-0 gxucff") #item main group
# results = results_div.find_all("li", class_="ProductGridstyles__Item-lc2zkx-1 dDUIzA")
# html = results_div.prettify()
# print(html)




print(title_tag)
print(price_tag)


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


workbook = xlsxwriter.Workbook('test.xlsx')
worksheet = workbook.add_worksheet()

#cell_format = workbook.add_format()
#cell_format.set_font_size(15)
cell_format = workbook.add_format({'bold': True})
#cell_format = workbook.add_format({'font_size': 15})
#bold.set_font_size(15)
#cell_format.set_bold
worksheet.write('A1' , 'LEGO Set Name', cell_format)
worksheet.write('B1' , 'Price', cell_format)





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

workbook.close()