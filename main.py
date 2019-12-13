if __name__ == "__main__":
    from constants import *
    from scrape import *
    from time import sleep as wait
    from util import *

    debug = False
    debug = True

    if debug:
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
            give_user_time_to_swipe_desktop(3)
            swipe_desktop("left")
            wait(2)
            scrape_fares(station_info)
    else:
        give_user_time_to_swipe_desktop(3)
        scrape_fares(station_info)
    swipe_desktop("right")
    print("\nQuitting...")
    exit()
