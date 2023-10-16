"""
Scrape the url's html data using requests library
Used for websites that don't require javascript to load its content
"""
import requests
from bs4 import BeautifulSoup as bs4

#Scrape a given url by using requests
def request_for_soup(url):
    
    response = requests.get(url)
    
    if(response.status_code!=200):
        return None

    soup = bs4(response.text,"html.parser")
    return soup