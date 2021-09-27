




list = [1]

def date_function():
    index = 0
    for html in list:        
        html = list[index]
        #soup = BeautifulSoup(html, 'html.parser')

        #title = soup.find("a")
        #date_title = title['href']
        
        #url_lego = 'https://www.lego.com'
        #page = requests.get(url_lego + date_title)
        #soup = BeautifulSoup(page.content, "html.parser")        

        #results_div2 = soup.find("div", class_="ProductOverviewstyles__Container-sc-1a1az6h-2 cIoioK")
        #results2 = results_div2.find_all("span", class_="Markup__StyledMarkup-ar1l9g-0 hlipzx")[1]

        # for title2 in results2:            
        #     print(title2.text, end="\n"*2)            
        #     oct_release = 'Coming Soon on October 1, 2021'
        #     if title2.text == oct_release:
        #         oct.append(title2.text)
        #         date_tag.append(title2.text)
        #     else:
        #         date_tag.append(title2.text)                
        index += 1        
        list.append(html)  
        
print(list)
date_function()

print(list)
