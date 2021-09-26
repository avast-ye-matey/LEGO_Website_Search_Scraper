import requests
from bs4 import BeautifulSoup
#import os
#import sys

#sys.stdout = open("test.txt", "w")

#this version has different/extra loops for scrapping price


with open('lego_list.txt', 'w') as f:

    print('What would you like to search?')
    print('What would you like to search?', file=f)
    #sys.stdout.write('What would you like to search?', end='\n')
    #f.write('What would you like to search?\n')
    user_input = input()
    #sys.stdout.write(user_input)
    f.write(user_input)
    f.write('\n'*2)
    user_input_without_spaces = user_input.replace(' ','%20')
    url_lego = 'https://www.lego.com'
    url = "https://www.lego.com/en-us/search?q="+ user_input_without_spaces
    url_cont = "https://www.lego.com/en-us/search?q="+ user_input_without_spaces
    #url_page_2 = "https://www.lego.com/en-us/search?q="+ user_input_without_spaces + "&page=2"
    #****print(url) #https://www.lego.com/en-us/search?q=harry%20potter
    #****print(url, file=f) #https://www.lego.com/en-us/search?q=harry%20potter
    #sys.stdout.write(url)
    #f.write(url + '\n')

    oct = []
    results = ""


    def parse_this_page(url_cont):
        global results
        page = requests.get(url_cont)
        soup = BeautifulSoup(page.content, "html.parser")
        #print(page.text)
        results_div = soup.find("div", class_="SearchPagestyles__MainContainer-sc-1d2gqze-5 jFRDvz")
        #*****results = results_div.find_all("span", class_="Markup__StyledMarkup-ar1l9g-0 hlipzx")
        results = results_div.find_all("li", class_="ProductGridstyles__Item-lc2zkx-1 dDUIzA")
        #results_title = 
        #results_price = 
        for text_results in results:
            text_results = text_results.text
            #print(text_results)
            print(text_results)
            for results_title in text_results:
                results_title = results_div.find("span", class_="Markup__StyledMarkup-ar1l9g-0 hlipzx")
                results_title = results_title.text
                print(results_title)
                for results_price in results_title:
                    results_price = results_div.find('span', class_='Text__BaseText-sc-178efqu-0 cVmQPV ProductPricestyles__StyledText-vmt0i4-0 eGdbAY')
                    results_price = results_price.text
                    print(results_price)

        sub_url()
        find_next_page()

    

    def sub_url():
        global results
        for title in results:
        #print(title.prettify(), end="\n")
        #print(title, end="\n"*2)

            print(title.text, end="\n")
            print(title.text, end="\n", file=f)
            #sys.stdout.write(title.text, end="\n")
            #f.write(title.text + '\n')
            link = title.find_parents('a')

            if results != None:
            
                for href in link:
                    #****print(href['href'])**************
                    #****print(href['href'], file=f)*******************
                    #sys.stdout.write(href['href'])
                    #f.write(href['href'] + '\n')
                    
                    
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
                        print(title2.text, end="\n"*2)
                        print(title2.text, end="\n"*2, file=f)
                        #sys.stdout.write(title2.text, end="\n"*2)
                        #f.write(title2.text + '\n')
                        oct_release = 'Coming Soon on October 1, 2021'
                        if title2.text == oct_release:
                            oct.append(title.text)
                        else:
                            pass
                        
                        #print(title2.text, end="\n"*2)
                        #link = title.find_parents('a')
            else:
                pass
        



        



    link_href_a = ''
    #url_cont = ''

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
            print(link_href_a, file=f) #page=2
            #sys.stdout.write(link_href_a)
            #f.write(link_href_a + '\n')
            print('inside2')
            print(url_cont) #https://www.lego.com/en-us/search?q=harry%20potterpage=2
            parse_this_page(url_cont)

        else:
            print("All done searching!\n")
            print("All done searching!\n", file=f)
            #sys.stdout.write('done')
            #f.write('done\n')
            



    
            
    parse_this_page(url_cont)


    #****print('inside3')
    #****print(link_href_a) #page=2
    #****print(url_cont) #https://www.lego.com/en-us/search?q=harry%20potterpage=2
            
        
    print("These sets come out on Oct. 1")
    print("These sets come out on Oct. 1", file=f)
    #sys.stdout.write("These sets come out on Oct. 1")
    #f.write("These sets come out on Oct. 1\n")
    print(oct)
    print(oct, file=f)
    #sys.stdout.write(oct)
    #f.write(oct + '\n')


    #sys.stdout.close()

f.close()