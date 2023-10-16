"""
Scrape the url's html data using Edge webdriver
Used for websites that require javascript to load its contents
"""
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from bs4 import BeautifulSoup as bs4

#Scrape a given url by using Edge Webdriver
def request_for_soup(url):
    edge_options = Options()
    edge_options.headless = True

    driver = webdriver.Edge(options=edge_options)
    driver.get(url)

    html = driver.page_source
    soup = bs4(html, "html.parser")

    return soup


if __name__ == "__main__":
    url = "https://justjoin.it/?q=junior"
    soup = request_for_soup(url)
    with open("response_text.html", "w") as f:
        f.write(soup.prettify())
