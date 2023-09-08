from bs4 import BeautifulSoup as bs4
from bs4 import element as bs4_elem
import user_interaction as ui
import scrape as sc

# instead of changing it to list, just do find_all('div')
def filter_for_tiles(soup: bs4) -> list:
    # filter for blocks which contain every information
    # about the specific offer (a div basically)
    tiles = []
    root_div = soup.find(id="root")
    div_list = []

    # keep only elements that are divs
    for elem in root_div:
        if elem.name == "div":
            div_list.append(elem)

    # nest it 3 times to get the div in which the data about offers is stored
    working_div = div_list[-2].find("div").find("div")
    temp_dirs = [x for x in working_div.children if type(x) == bs4_elem.Tag]

    # picking specific div and going through nested divs again
    working_div = temp_dirs[-1].find("div").find("div").find("div")
    for div in working_div.children:
        if type(div) == bs4_elem.Tag:
            tiles.append(div)
    return tiles

def extract_data_from_tiles(tiles) -> list:
    # filter the previously-provided divs into
    # dictionaries of data
    listed_data = []
    id_number = 1
    for tile in tiles:
        data = dict()
        # if there is less than 15 tiles in the results, ignore the last div (not needed)
        try:
            working_div = (
                tile.find("div").find("div").find_all("div", recursive=False)[1]
            )
        except AttributeError:
            break
        name = working_div.find("div").find("div").find("div").string.strip()

        salary = (
            working_div.find("div")
            .find_all("div", recursive=False)[1]
            .find("div")
            .find("div")
            .string.strip()
        )

        location = (
            working_div.find_all("div", recursive=False)[1]
            .find_all("div", recursive=False)[1]
            .find("span")
            .next_element.strip()
        )

        is_remote = (
            tile.find(
                "span", string="\n                  Fully Remote\n                 "
            )
            != None
        )

        requirements = working_div.find_all("div", recursive=False)[1].find_all(
            "div", recursive=False
        )[2]

        requirements = [
            x.next_element.strip() for x in list(requirements.find_all("span"))
        ]

        link = "https://justjoin.it" + tile.find("a")["href"]

        data["id"] = id_number
        data["name"] = name
        data["salary"] = salary
        data["location"] = location
        data["remote"] = is_remote
        data["requirements"] = requirements
        data["link"] = link

        listed_data.append(data)
        id_number += 1

    return listed_data

def get_offers_from_url(url: str, keywords: list) -> list:
    final_url = add_keywords_to_url(url,keywords)
    soup = sc.request_for_soup(url)
    tiles = filter_for_tiles(soup)
    offers = extract_data_from_tiles(tiles)
    return offers

def get_offers_from_test_file() -> dict:
    file = open(r"test.html", "r")
    soup = bs4(file.read(), "html.parser")
    file.close()

    tiles = filter_for_tiles(soup)
    offers = extract_data_from_tiles(tiles)
    return offers

def add_keywords_to_url(url: str, keywords: list) -> None:
    """
    won't use categories/skills, as using them instead of
    keywords gives less results
    """
    url = url + ";".join(keywords)
    return url


    
if __name__ == "__main__":
    offers = get_offers_from_test_file()
    ans = ui.ask_for_format()
    ui.show_offers(offers, ans)
