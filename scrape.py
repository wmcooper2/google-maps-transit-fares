from constants import *
from googlemaps import *
from time import sleep as wait
from typing import Dict, List, Text
from util import *


def scrape_fares(info: Dict[Text, Text]) -> None:
    """Begin scraping fares. Returns None."""
    first_station = True
    all_stations: set = set(load_stations(info["starting_stations"]))
    stations_finished: set = fares_already_scraped(FARES)
    error_stations: set = set(load_stations(info["issues"]))
    to_scrape: set = all_stations.difference(
            stations_finished, error_stations)
    for dest in load_stations(info["destinations"]):
        if dest in to_scrape:
            to_scrape.remove(dest)
        if first_station:
            first_station = False
            goto_search_input()
            enter_text(f"{dest} Station")
            wait(3)
            locate_directions_arrow()
            wait(2)
        else:
            change_dest_station(f"{dest} Station") 
            wait(3)
        fares_to_dest(dest, to_scrape, info)


def fares_to_dest(dest: Text, stations: List[Text],
        info: Dict[Text, Text]) -> None:
    """Gets all fares to dest. Returns None."""
    while len(stations) > 0:
        errors = 0
        station = stations.pop()
        wait(2)
        change_starting_station(f"{station} Station") 
        wait(1)

        try:
            fare = capture_fare(station, dest)
            print(f"{actual_fare}_{start}_{dest}\n")
#             with open("results/TokyoMetro.txt", "a+") as f:
#                 csvfile = csv.writer(f, delimiter=",")
#                 csvfile.write([actual_fare, start, dest])
#                 f.write(f"{actual_fare}_{start}_{dest}\n")
        except:
            print(f"{actual_fare}_{start}_{dest}\n")
#             LOG.debug(f"Fare not found: {station} to {dest}")
#             with open(info["issues"], "a+") as f:
#                 f.write(station+"\n")
            errors += 1

        if errors > ERR_LIM:
            print(f"Too many errors, fares_to_dest(). Quitting...")
#             LOG.debug("Too many errors with fares_to_dest(). Quitting...")
            exit()
