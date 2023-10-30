from bs4 import BeautifulSoup as bs4
from bs4 import element as bs4_elem


# justjoin
def add_keywords_to_url(keywords: list) -> None:
    """
    won't use categories/skills, as using them instead of
    keywords gives less results
    """
    url = "https://justjoin.it/?keyword="
    url = url + ";".join(keywords)
    return url


def filter_for_tiles(soup: bs4) -> list:
    # filter for blocks which contain every information
    # about the specific offer (a div basically)
    tiles = []
    working_div = soup.find(id="__next").find(
        "div", attrs={"data-test-id": "virtuoso-item-list"}
    )
    for div in working_div.find_all("div", recursive=False):
        tiles.append(div)
    tiles.pop()
    return tiles


def extract_data_from_tiles(tiles: list) -> list:
    # filter the previously-provided divs into
    # dictionaries of data
    listed_data = []
    id_number = 1
    for tile in tiles:
        tile: bs4_elem.Tag = tile.find("div").find("div")
        temp_dict = dict()

        info_div: bs4_elem.Tag = (
            tile.find_all("div", recursive=False)[1]
            .find_all("div", recursive=False)[1]
            .find("div")
            .find("div")
        )
        name = tile.find("h2").text.strip()

        # find the salary
        salary = None
        spans = info_div.find_all("span")
        for span in spans:
            if "PLN" in span.text:
                salary = span.text.strip().rstrip(" PLN").replace("K", " 000")

        # If salary is given in different currency, but given in PLN, then the dot appears
        if salary and "." in salary:
            salary = salary.replace(".", " ").replace(" 000", "00")

        # find the locations
        locations = (
            info_div.find_all("div", recursive=False)[2].find("div").text.strip()
        )

        # get rid of all uneccessary white signs when more locations were provided
        locations = locations.split("\n")
        locations = [
            part.strip()
            for part in locations
            if part.strip() != "Location" and part.strip() != "Locations"
        ]
        locations = "".join(locations)
        remote = bool(
            info_div.find_all("div", recursive=False)[2].find("span", recursive=False)
        )
        company = tile.find("span").text.strip()

        link = "https://justjoin.it" + tile.find("a")["href"]

        temp_dict["name"] = name
        temp_dict["company"] = company
        temp_dict["salary"] = salary
        temp_dict["locations"] = locations
        temp_dict["remote"] = remote
        temp_dict["link"] = link

        listed_data.append(temp_dict)
        id_number += 1

    return listed_data


# whole process of change soup into job offers
def soup_to_data(soup: bs4) -> list:
    tiles = filter_for_tiles(soup)
    offers = extract_data_from_tiles(tiles)
    return offers


def local_test() -> dict:
    try:
        file = open(r"tempJustJoinIt.html", "r", encoding="utf-8")
    except OSError:
        print("Local file not found.")
        return
    soup = bs4(file.read(), "html.parser")
    file.close()

    offers = soup_to_data(soup)

    return offers


if __name__ == "__main__":
    offers = local_test()
    for offer in offers:
        for x, y in offer.items():
            print(f"{x}: {y}")
        print("----------------------")
