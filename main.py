if __name__ == "__main__":
    from constants import *
    import csv
    from scrape import scrape_fares
    from time import sleep as wait
    from util import (
            give_user_time_to_swipe_desktop,
            swipe_desktop,
            load_stations,
            fares_already_scraped)

    #move DEBUG stuff to constants when finished
    DEBUG = False
    DEBUG = True
    if DEBUG:
        station_info = {
            "destinations": EXAMPLE_DESTINATIONS,
            "starting_stations": EXAMPLE_TARGET_STATIONS,
            "issues": EXAMPLE_ISSUE_STATIONS,
            }
        start_points: set = set(load_stations(
            station_info["starting_stations"]))
        print("start_points = ", start_points)
        dest_points: set = set(load_stations(
            station_info["destinations"]))
        print("dest_points = ", dest_points)
    else:
        station_info = {
            "destinations": DESTINATIONS,
            "starting_stations": TARGET_STATIONS,
            "issues": ISSUE_STATIONS,
            }

    if not DEBUG:
        answer = input(
            "This program will take control of your mouse and keyboard.\nAfter pressing [y], move the desktop to a fullscreen view of google maps. ")
        if answer == "y":
            give_user_time_to_swipe_desktop(3)
            swipe_desktop("left")
            wait(2)
            fare_information = scrape_fares(station_info)
    else:
#         give_user_time_to_swipe_desktop(3)
        swipe_desktop("left")
        fare_information = scrape_fares(station_info)
    #save fares
    with open("results/TokyoMetro.csv", "a+") as f:
        csvfile = csv.writer(f)
        csvfile.writerows(fare_information)
    swipe_desktop("right")
    print("\nQuitting...")
    exit()
