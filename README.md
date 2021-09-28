# LEGO_Website_Search_Scrapper


Please forgive the messy code! WORK IN PROGRESS!<br />
I leave myself a lot of notes and use the print function after almost ever line to help me debug


**What does this program do?:**<br />
This program takes a user input to scrape the LEGO website for sets, price, and availability using the user input. So lets say you want to see what LEGO Harry Potter sets  exist, if they're available (buy now, comming soon, retired, or back ordered), and how much they cost, well just type Harry Potter as your search input when asked. Once the program is done, the results are exported into an `.xlsx` (Excel) document and labeled with today's date. The functionality of the program is based on if you actually were searching the LEGO website. The program scrapes the search function as if you went directly to their site and used the search function. Also rely on the Excel file for results and not the terminal beyond the initial user input. 

**About:**<br />
This program was originally meant to find what sets came out October 1st because weirdly that doesn't exist on their site. My focus needed to be on the functionality so I moved this purpose for a later feature. The results already return a lot of useful info already. I wanted to build a solid foundation because I was already having to build a powerful program for something that could be labeled a feature. Some code I already wrote is commented out for when I add the feature back. I also want to add a more functional search option for release timeframes beyond the static Oct 1st. This program in its current state is meant to utilize the Excel file and not the terminal (beyond the initial user input). I use the terminal as a testing tool so it varies wildly from end results. 

**Steps to run program:**
1) You will first need to install 3 packages-

`pip install requests`
[Documentation link](https://docs.python-requests.org/en/master/user/install/)

`pip install beautifulsoup4`
[Documentation link](https://www.crummy.com/software/BeautifulSoup/#Download)

`pip install XlsxWriter`
[Documentation link](https://xlsxwriter.readthedocs.io/getting_started.html)

2) Run-

`LEGO_Project_Run_Me.py`

3) Program will ask what do you want to search. Input anything you want to search on lego.com (santa, harry potter, and star wars are known working searches)

4) Be patient. Depending on connection, it could take a little bit to start returning values

5) Don't forget to check `.xlsx` document after program is done running!

6) **If you don't have Excel but have Visual Studio:** Add extension *Excel Viewer* by GrapeCity. Once downloaded, RIGHT-CLICK on file inside Visual Studio and selest OPEN PREVIEW. If you double-click file it won't open properly in Visual Studio. 



**Plans before final submittal:**
1) Re-write the messages for better discription and more of a personal experience. 
2) Clean-up code. There are a lot of excess spaces and unused code commented out. 
3) Add project requirements into the `readme.md` file and what code accomplished those requirements. 
4) Make more commits!
- [x] Make sure there is an error message presented to user if user input returns a None value (currently it crashes).



**Future features/ Changes to code:**
1) Have release date be able to change instead of a static Oct 1.
2) Make program into a web app. 
3) Add single item hyperlink
4) Add single item picture thumbnails
5) Find free alterntives to preview Excel spreadsheet
6) Include alternative export file extension like pdf
- [x] Add pricing to the list. 
- [x] Output to Excel file
- [x] Turn results into a searchable database



