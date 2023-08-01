from bs4 import BeautifulSoup as bs4
from selenium import webdriver
def request_for_soup(url):
    #used driver instead of requests because of js requierement
    driver = webdriver.Edge()
    driver.get(url)
    html = driver.page_source
    soup = bs4(html,features="html.parser")
    driver.quit()
    return soup

def add_keywords_for_url(keywords):
    global url
    """
    won't use categories/skills, as using them instead of 
    keywords gives less results
    """
    url = url+";".join(keywords)

def get_keywords():
    global keywords
    print("Input q to exit.")
    while True:
        inp = input("Provide keyword: ")
        if(inp=="q" or inp==""):
            break
        keywords.append(inp)

def filter_data_for_titles():
    pass

if __name__=="__main__":
    keywords = []
    url = "https://justjoin.it/?q="
    get_keywords()
    add_keywords_for_url(keywords)
    soup = request_for_soup(url)
    filter_data_for_titles()
    print(url)
    #save the soup html into the text file
    with open('temp2.html','w') as f:
        f.write(soup.prettify())