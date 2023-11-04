import JustJoinIt.filter_data as fd_jj
import NoFluffJobs.filter_data as fd_nfj
import Scraping.scrape_req as sc_r
import Scraping.scrape_driv as sc_d
import user_interaction as ui
import GUI_gen as gui
from data_to_offers import data_to_offers

# get the format of displaying
# get keywords based on the format choosen
if __name__ == "__main__":
    # establish the way of saving the data (terminal/text file)
    display_format = ui.ask_for_format()

    # if the display was chosen to be saved in the text file, get them from terminal
    if display_format:
        keywords = ui.get_keywords()
        offers = data_to_offers(keywords)
        # display the offers
        ui.show_offers(offers, display_format)
    # if the display was chosen
    else:
        gui.main()

    # add id number for each offer
