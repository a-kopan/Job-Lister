import JustJoinIt.filter_data as fd_jj
import NoFluffJobs.filter_data as fd_nfj
import Scraping.scrape_req as sc_r
import Scraping.scrape_driv as sc_d
import user_interaction as ui
import GUI_gen as gui

if __name__ == "__main__":
    offers = []
    #get the keywords
    keywords = ui.get_keywords()
    #establish the way of saving the data (terminal/text file)
    
    display_format = ui.ask_for_format()
    
    #for each service:
    req_services = [fd_nfj]
    driv_services = [fd_jj]
    
    #treat services differently based on whether they have to use a driver or a http request
    
    for service in req_services:
        URL = service.add_keywords_to_url(keywords)
        soup = sc_r.request_for_soup(URL)
        data = service.soup_to_data(soup)
        offers+=data
    
    #add id number for each offer
    

    #display the offers
    ui.show_offers(offers,display_format)


