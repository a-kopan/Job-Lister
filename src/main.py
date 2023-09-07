import filter_data as fd
import scrape
import user_interaction as ui
import GUI_gen as gui

if __name__ == "__main__":
    gui.generate_GUI()
    #placeholder for gui testing
    quit()
    url = "https://justjoin.it/?q="
    keywords = ui.get_keywords()
    view_format = ui.ask_for_format()

    url = ui.add_keywords_to_url(url, keywords)
    soup = scrape.request_for_soup(url)

    tiles = fd.filter_for_tiles(soup)
    offers = fd.extract_data_from_tiles(tiles)

    ui.clear_screen()
    print(f"Generated URL: {url}")
    ui.show_offers(offers, view_format)

