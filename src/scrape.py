from bs4 import BeautifulSoup as bs4
from selenium import webdriver




def request_for_soup(url) -> bs4:
    # used driver instead of requests because of js requierement
    driver = webdriver.Edge()
    driver.get(url)
    html = driver.page_source
    soup = bs4(html, features="html.parser")
    driver.quit()
    return soup


if __name__ == "__main__":
    keywords = []
    url = "https://justjoin.it/?q="
    file = open("test.html", "r")
    soup = bs4(file.read(), "html.parser")
    file.close()
    #get_keywords()
    #add_keywords_to_url(url,keywords)
    #request_for_soup(url)
    print(soup.find_all(["span"], text="Latest"))
