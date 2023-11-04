from Scraping.scrape_driv import request_for_soup as req_d
from Scraping.scrape_req import request_for_soup as req_r
import JustJoinIt.filter_data as fd_jj
import NoFluffJobs.filter_data as fd_nfj
import user_interaction as ui
import GUI_gen as gui


# send requests based on the library neccessary to use
# filer the requested data
# add filtered data to offers
# display the filtered data based on the form choosed
def data_to_offers(keywords):
    offers = []
    # for each service:
    req_services = [fd_nfj]
    driv_services = [fd_jj]

    # treat services differently based on whether they have to use a driver or a http request
    for service in driv_services:
        URL = service.add_keywords_to_url(keywords)
        # soup = req_d.request_for_soup(URL)
        soup = req_d(URL)
        data = service.soup_to_data(soup)
        offers += data

    for service in req_services:
        URL = service.add_keywords_to_url(keywords)
        # soup = req_r.request_for_soup(URL)
        soup = req_r(URL)
        data = service.soup_to_data(soup)
        offers += data

    return offers


if __name__ == "__main__":
    pass
