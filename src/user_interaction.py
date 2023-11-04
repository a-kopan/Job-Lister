import os
import GUI_gen as gui


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
    while ans not in ["F", "f", "w", "W"]:
        ans = input("Write results to file (F), or display them in window (W): ")
    if ans in ["F", "f"]:
        return input("Name the output file (don't add the extenstion): ") + ".txt"
    else:
        return None


def show_offers(offers: list, *args) -> None:
    # If the list is empty
    if len(offers) == 0:
        print("Empty List")
    ##If the window option was choosen
    ##then the data will be displayed in GUI anyways
    # elif len(args) == 0 or args[0] == (None):
    #    pass
    # If the file option was choosed
    else:
        file = open(args[0], "w")
        for offer in offers:
            for key in offer:
                print(key.capitalize() + ":", offer[key], file=file)
            print("-" * 30, file=file)
        file.close()
