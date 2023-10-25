import os

def get_keywords() -> list:
    print("Input q to exit.")
    keywords = []
    while True:
        inp = input("Provide keyword: ")
        if inp == "q" or inp == "":
            break
        keywords.append(inp)
    return keywords

def clear_screen():
    os.system("cls")

def ask_for_format():
    ans = ""
    while ans not in ["F", "f", "t", "T"]:
        ans = input("Write results to file (F), or display them in terminal (T): ")
    if ans in ["F", "f"]:
        return input("Name the output file (don't add the extenstion): ") + ".txt"
    else:
        return None

def show_offers(offers, *args) -> None:
    if len(args) == 0 or args[0]==(None):
        for offer in offers:
            # print each attribute with format Key: value
            for key in offer:
                print(key.capitalize() + ":", offer[key])
            print("-" * 30)

        input()
    else:
        file = open(args[0], "w")
        for offer in offers:
            for key in offer:
                print(key.capitalize() + ":", offer[key], file=file)
            print("-" * 30, file=file)
        file.close()
