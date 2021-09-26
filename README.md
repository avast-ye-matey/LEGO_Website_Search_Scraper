# LEGO_Website_Search_Scrapper


Please forgive the messy code! WORK IN PROGRESS!<br />
I leave myself a lot of notes and use print function after almost ever line to help me debug



**About:**<br />
The program takes a user input to scrape the Lego website for sets and availability dates using the user input. It also returns all sets coming out Oct 1st. This program was originally meant to find what sets came out October 1st because weirdly that doesn't exist on their site. The program also creates a `.txt` file of the results (it varies slightly than what's in the terminal. The output is cleaner on the `.txt` file because I print more info than needed to help with debugging). The program scrapes the search function as if you went directly to their site and used the search function. In its current state the program only returns the set name and the release date then after it finishes it shows what sets come out Oct 1. (currently its blank if none no sets come out Oct 1). 

**Steps to run program:**
1) You will first need to install 2 packages-

`pip install requests`
[Documentation link](https://docs.python-requests.org/en/master/user/install/)

`pip install beautifulsoup4`
[Documentation link](https://www.crummy.com/software/BeautifulSoup/#Download)

2) Run-

`LEGO_Project.py`

3) Program will ask what do you want to search. Input anything you want to search on lego.com (santa, harry potter, and star wars are known working searches)

4) Be patient. Depending on connection, it could take a little bit to start returning values

5) Don't forget to check `.txt` document after program is done running



**Plans before final submittal:**
1) Make sure there is an error message presented to user if user input returns a None value (currently it crashes).
2) Re-write the messages for better discription and more of a personal experience. 
3) Clean-up code. There are a lot of excess spaces and unused code commented out. 
4) Add project requirements into the `readme.md` file and what code accomplished those requirements. 
5) Make more commits!



**Future features/ Changes to code:**
1) Add pricing to the list. 
2) Output to Excel file
3) Have release date be able to change instead of a static Oct 1.
4) Turn results into a searchable database


I do have a version 2 I'm working on. It's labeled `LEGO_Lists.py`. But it is unfinished. Instead of how it currently parses the page and displays results, I'm putting the results in a list for each category: title, price, and release date. Then I'll use those lists to fill in an Excel spreadsheet. 
