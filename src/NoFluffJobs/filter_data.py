from bs4 import BeautifulSoup as bs4


# nofluffjobs
def add_keywords_to_url(keywords: list):
    head = "https://nofluffjobs.com/pl/?criteria=keyword%3D"
    tail = "&page=1"

    url = head + ",".join(keywords) + tail
    return url


def filter_for_tiles(soup: bs4) -> list:
    working_dir = soup.find(
        "div", class_="list-container ng-star-inserted", recursive=True
    )
    # tiles will be made out of pairs (a,popover-content),
    # which store (data for tile, locations aside from the first one)
    tiles = []
    children = working_dir.find_all(recursive=False)

    for ind in range(0, len(children), 2):
        tiles.append((children[ind], children[ind + 1]))
    return tiles


def extract_data_from_tiles(tile_pairs: list) -> list:
    REGIONS = [
        "Dolnośląskie",
        "Kujawsko-Pomorskie",
        "Lubelskie",
        "Lubuskie",
        "Łódzkie",
        "Małopolskie",
        "Mazowieckie",
        "Opolskie",
        "Podkarpackie",
        "Podlaskie",
        "Pomorskie",
        "Śląskie",
        "Świętokrzyskie",
        "Warmińsko-mazurskie",
        "Wielkopolskie",
        "Zachodniopomorskie",
        "Warmińsko-Mazurskie",
    ]
    offers = list()
    for a, popover in tile_pairs:
        temp_dict = {}
        # title of the offer
        name = a.find(
            "h3", attrs={"data-cy": "title position on the job offer listing"}
        ).text.strip()
        # the name of the company that posts the offer
        company = a.find(
            "span", attrs={"data-cy": "company name on the job offer listing"}
        ).text.strip()
        # salary range
        salary = (
            a.find("span", attrs={"data-cy": "salary ranges on the job offer listing"})
            .text.strip()
            .rstrip("PLN")
            .strip()
            .replace("\xa0", " ")
        )

        # check if there is a range given in the salary, if there is then change its format
        if "–" in salary:
            bounds = []
            for bound in salary.split("–"):
                bounds.append(bound.strip())
            salary = " - ".join(bounds)

        # for all possible locations (empty if only remote)
        locations = []

        # flag for remote job accessibility
        remote = False

        # url to the job offer
        link = "https://nofluffjobs.com" + a["href"]

        # dir in which all possible locations (along with remote) are stored
        locations_dir = popover.find("nfj-posting-item-place-popover").find("ul")
        # extract avaliable locations to list
        for li in locations_dir.find_all("li"):
            location = li.find("a").text.strip()
            if not location in REGIONS:
                # if there is a specific address, add only the name of the city
                locations.append(location.split(" ")[0])

        # check if there is an option for the remote job
        if "Zdalnie" in locations:
            locations.remove("Zdalnie")
            remote = True

        if len(locations) > 2:
            locations = f"{locations[0]}, +{len(locations)-1} Locations"
        elif len(locations) == 2:
            locations = f"{locations[0]}, +1 Location"

        temp_dict["name"] = name
        temp_dict["company"] = company
        temp_dict["salary"] = salary
        temp_dict["locations"] = locations
        temp_dict["remote"] = remote
        temp_dict["link"] = link

        offers.append(temp_dict)
    return offers


# whole process of change soup into job offers
def soup_to_data(soup: bs4) -> list:
    tiles = filter_for_tiles(soup)
    offers = extract_data_from_tiles(tiles)
    return offers


# tests the filters on local file, ignored for right categorisation on github
def local_test():
    try:
        file = open("tempNoFluffJobs.html", "r", encoding="utf-8")
    except OSError:
        print("Local file not found.")
        return []

    soup = bs4(file, "html.parser")
    file.close()

    offers = soup_to_data(soup)

    return offers


if __name__ == "__main__":
    offers = local_test()
    for offer in offers:
        for key, val in offer.items():
            print(key, ": ", val)
        print("----------")
