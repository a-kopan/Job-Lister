from bs4 import BeautifulSoup as bs4
from bs4 import element as bs4_elem
#justjoin
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
    root_div = soup.find(id="__next")
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

def extract_data_from_tiles(tiles: list) -> list:
    # filter the previously-provided divs into
    # dictionaries of data
    listed_data = []
    id_number = 1
    for tile in tiles:
        temp_dict = dict()
        # if there is less than 15 tiles in the results, ignore the last div (empty)
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

        locations = (
            working_div.find_all("div", recursive=False)[1]
            .find_all("div", recursive=False)[1]
            .find("span")
            .next_element.strip()
        )

        remote = (
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

        temp_dict["name"] = name
        #temp_dict["company"] = company
        temp_dict["salary"] = salary
        temp_dict["locations"] = locations
        temp_dict["remote"] = remote
        temp_dict["link"] = link

        listed_data.append(temp_dict)
        id_number += 1

    return listed_data

#whole process of change soup into job offers
def soup_to_data(soup: bs4) -> list:
    tiles = filter_for_tiles(soup)
    offers = extract_data_from_tiles(tiles)
    return offers

def local_test() -> dict:
    try:
        file = open(r"tempJustJoinIt.html", "r",encoding='utf-8')
    except OSError:
        print("Local file not found.")
        return
    soup = bs4(file.read(), "html.parser")
    file.close()
    
    offers = soup_to_data(soup)
    
    return offers

if __name__=="__main__":
    offers = local_test()
    print(offers)