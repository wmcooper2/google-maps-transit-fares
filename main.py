# load graph and tree
    # graph: collection of nodes with fare information
    # tree:  a fast way to check for fare existence

# get station names through user input
    # a list of names
    # check if they already exist
        # if in the tree, check the graph, else get from gui
        # if checking the graph, return the price


# manipulate the gui to get the directions 
    # pyautogui
    # googlemaps

# extract the fare from the image
    # pytesseract

# insert the fare into the gui
# add the station names to the tree if not there.

if __name__ == "__main__":
    from constants import *
    from googlemaps import swipe_desktop
    from time import sleep as wait
    from scrape import scrape_fares

    debug = False
#     debug = True

    if not debug:
        station_info = {
            "destinations": EXAMPLE_DESTINATIONS,
            "starting_stations": EXAMPLE_TARGET_STATIONS,
            "issues": EXAMPLE_ISSUE_STATIONS,
            }
    else:
        station_info = {
            "destinations": DESTINATIONS,
            "starting_stations": TARGET_STATIONS,
            "issues": ISSUE_STATIONS,
            }

    if not debug:
        answer = input(
            "This program will take control of your mouse and keyboard.\nAfter pressing [y], move the desktop to a fullscreen view of google maps. ")
        if answer == "y":
            for i in range(3, -1, -1):
                print(f"\rTaking control in: {i} seconds.", end="\r")
                wait(1)
            print()
            swipe_desktop("left")
            wait(2)
            scrape_fares(station_info)
    else:
        scrape_fares(station_info)
    swipe_desktop("right")
    print("\nQuitting...")
    exit()
