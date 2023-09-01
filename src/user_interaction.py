def get_keywords() -> list:
    print("Input q to exit.")
    keywords = []
    while True:
        inp = input("Provide keyword: ")
        if inp == "q" or inp == "":
            break
        keywords.append(inp)
    return keywords

def add_keywords_to_url(url,keywords) -> None:
    """
    won't use categories/skills, as using them instead of 
    keywords gives less results
    """
    url = url + ";".join(keywords)
    print("Generated url:",url)
    
def show_offers(offers):
    for offer in offers:
        print("Name:",offer["name"])
        print("Salary:",offer["salary"])
        print("Locations:",offer["location"])
        print("Requirements:",*offer["requirements"])
        print('-'*30)