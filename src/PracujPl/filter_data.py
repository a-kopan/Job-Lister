from bs4 import BeautifulSoup as bs4
from bs4 import element as bs4_elem
#justjoin
def add_keywords_to_url(keywords: list) -> str:
    head = "https://it.pracuj.pl/praca/"
    tail = ";kw?itth=37"
    url = head+'%20'.join(keywords)+tail
    return url
    
def filter_for_tiles(soup: bs4) -> list:
    working_div = soup.find('div',{"data-test":"section-offers"})
    for tile in working_div.find_all('div',recursive=False):
        tile: bs4_elem.Tag = tile.find('div')
        name_and_link_tag: bs4_elem.Tag = tile.find('h2')
        check_for_href = name_and_link_tag.find('a')
        if check_for_href: 
            name_and_link_tag=check_for_href
            link = name_and_link_tag.attrs['href'] 
        else:
            link = ''
        name = name_and_link_tag.text.strip()

        company = tile.find('h4',attrs={"data-test":"text-company-name"}).text.strip()
        location = tile.find('h5',attrs={"data-test":"text-region"}).text.strip()
        salary = tile.find('span', attrs={"data-test":"offer-salary"})
        if salary: salary = salary.text.strip()
        else: salary = "Undefined"
        technologies = []
        technologies_list = tile.find('div',attrs={"data-test":"technologies-list"})
        if technologies_list:
            for span in technologies_list.find_all('span'):
                technologies.append(span.text.strip())
        a=5
    return []

def extract_data_from_tiles(tiles: list) -> list:
    pass

#whole process of change soup into job offers
def soup_to_data(soup: bs4) -> list:
    tiles = filter_for_tiles(soup)
    offers = extract_data_from_tiles(tiles)
    return offers


def local_test() -> dict:
    try:
        file = open(r"tempPracujpl.html", "r",encoding='utf-8')
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