import filter_data as fd
import scrape
import user_interaction as ui
if __name__ == "__main__":
    url = "https://justjoin.it/?q="
    keywords = ui.get_keywords()
    
    ui.add_keywords_to_url(url,keywords)
    soup = scrape.request_for_soup(url)
    
    tiles = fd.filter_for_tiles(soup)
    offers = fd.filter_for_data(tiles)
    
    ui.show_offers(offers)
