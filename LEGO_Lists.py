import requests
from bs4 import BeautifulSoup


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

html =product_grid[0].prettify()

soup = BeautifulSoup(html, 'html.parser')

title = soup.find("span", class_='Markup__StyledMarkup-ar1l9g-0 hlipzx')
no_space = title.text
print(no_space.lstrip())
#title = soup.find("a")
#print(title.string)


#parse_each_item()
#print(product_grid)
#print(len(product_grid))