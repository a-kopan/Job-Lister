from bs4 import BeautifulSoup as bs4

def filter_for_tiles(soup: bs4):
    working_dir = soup.find('div',class_="list-container ng-star-inserted",recursive=True)
    #tiles will be made out of pairs (a,popover-content),
    #which store (data for tile, locations aside from the first one)
    tiles = []
    children = working_dir.find_all(recursive=False)
    
    for ind in range(0,len(children),2):
        tiles.append((children[ind],children[ind+1]))
    return tiles

def extract_data_from_tiles(tile_pairs):
    to_traverse = []
    for tile in to_traverse:
        name = tile.find('h3',attrs={"data-cy":"title position on the job offer listing"}).text.strip()
        company = tile.find('span',attrs={"data-cy":"company name on the job offer listing"}).text.strip()
        salary = tile.find('span',attrs={"data-cy":"salary ranges on the job offer listing"}).text.strip().rstrip("PLN").strip().replace('\xa0',' ')
        location = tile.find('nfj-posting-item-city').find('span').text.strip()
        remote = 'Zdalnie' in location

def add_keywords_to_url(url: str, keywords: str):
    pass

def get_offers_from_url(url: str):
    pass

if __name__=="__main__":
    file = open("tempNoFluffJobs.html",'r',encoding='utf-8')
    soup = bs4(file,'html.parser')
    tiles = filter_for_tiles(soup)
    a=4