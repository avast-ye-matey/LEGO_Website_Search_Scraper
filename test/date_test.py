import requests
from bs4 import BeautifulSoup
import xlsxwriter
from datetime import date
import re



def date_p():
        
        grid = []
        x = 'https://www.lego.com/en-us/search?q=santa'
        page = requests.get(x)
        soup = BeautifulSoup(page.content, "html.parser")
        
        results_div = soup.find("ul", class_="ProductGridstyles__Grid-lc2zkx-0 gxucff") 
        if results_div != None:
            results = results_div.find_all("li", class_="ProductGridstyles__Item-lc2zkx-1 dDUIzA") 
            for li_results in results:            
                grid.append(li_results)              
        else:  
            print('No results found. Please try another search.') 
            exit()    


        date_tag = []
        index = 0
        for html in grid:        
            html = grid[index].prettify()            
            soup = BeautifulSoup(html, 'html.parser')
            title = soup.find("a")
            date_title = title['href']            
            url_lego = 'https://www.lego.com'            
            page = requests.get(url_lego + date_title)
            soup = BeautifulSoup(page.content, "html.parser")        

            results_div2 = soup.find("div", class_="ProductOverviewstyles__Container-sc-1a1az6h-2 cIoioK")
            results2 = results_div2.find_all("span", class_="Markup__StyledMarkup-ar1l9g-0 hlipzx")[1]
                          
            index += 1     
            #return results2.text    ##########
            date_tag.append(results2.text)  ###################
        return date_tag

datel = date_p()
print(datel)