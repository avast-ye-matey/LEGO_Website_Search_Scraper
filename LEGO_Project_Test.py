import requests
from bs4 import BeautifulSoup

print('What would you like to search?', end='\n')
user_input = input()
user_input_without_spaces = user_input.replace(' ','%20')
url = "https://www.lego.com/en-us/search?q="+ user_input_without_spaces
url_page_2 = "https://www.lego.com/en-us/search?q="+ user_input_without_spaces + "&page=2"
#url = "https://www.lego.com/en-us/search?q=santa" **************************
url_lego = 'https://www.lego.com'
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
#print(page.text)

results_div = soup.find("div", class_="SearchPagestyles__MainContainer-sc-1d2gqze-5 jFRDvz")
results = results_div.find_all("span", class_="Markup__StyledMarkup-ar1l9g-0 hlipzx")
#tag = soup.span
#tag.string
#type(tag.string)
#print(results)

oct = []

for title in results:
    #print(title.prettify(), end="\n")
    #print(title, end="\n"*2)

    #print(title.text, end="\n")************************
    link = title.find_parents('a')

    if results != None:
    
        for href in link:
            #print(href['href'])*************************
            link_href = href['href']

            url_lego = 'https://www.lego.com'
            page = requests.get(url_lego + link_href)

            soup = BeautifulSoup(page.content, "html.parser")
            #print(page.text)

            results_div2 = soup.find("div", class_="ProductOverviewstyles__Container-sc-1a1az6h-2 cIoioK")
            results2 = results_div2.find_all("span", class_="Markup__StyledMarkup-ar1l9g-0 hlipzx")[1]

            for title2 in results2:
                #print(title.prettify(), end="\n")
                #print(title, end="\n"*2)
                #print(title2.text, end="\n"*2)*****************************************
                oct_release = 'Coming Soon on October 1, 2021'
                if title2.text == oct_release:
                    oct.append(title.text)
                else:
                    pass
                
                #print(title2.text, end="\n"*2)
                #link = title.find_parents('a')
    else:
        pass


    #print(title.text, end="\n")


    #print(link)

if url_page_2 != None:
    print("there is a page 2")
else:
    print('there is Not a page 2')
#oct = 'Coming Soon on October 1, 2021'
print("These sets come out on Oct. 1")
print(oct)