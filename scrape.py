from constants import *
from googlemaps import (
        capture_fare,
        close_directions,
        goto_search_input,
        enter_text,
        locate_directions_arrow,
        change_dest_station,
        change_starting_station)
from time import sleep as wait
from typing import Dict, List, Set, Text, Tuple
from util import load_stations


def scrape_fares(info: Dict[Text, Text]) -> None:
    """Begin scraping fares. Returns None."""
    first_station = True
    station_data = load_stations(info["starting_stations"])
    starting_stations = set(station_data)
    fares = []
    for dest in load_stations(info["destinations"]):
        station_copy = list(starting_stations.copy())
        if dest in station_copy:
            station_copy.remove(dest)
        if first_station:
            first_station = False  # change flag
            goto_search_input()
            wait(1)
            enter_text(f"{dest} Station")
            wait(1)
            locate_directions_arrow()
            wait(1)
        else:
            change_dest_station(f"{dest} Station") 
            wait(3)
        while len(station_copy) > 0:
            station = station_copy.pop()
            wait(2)
            change_starting_station(f"{station} Station") 
            wait(1)
            try:
                fare = capture_fare(station, dest)
                print(f"{fare}_{station}_{dest}\n")
                fares.append([fare, station, dest])
            except:
                print(f"ERROR: fares_to_dest(), {fare}_{station}_{dest}\n")
    close_directions()
    return fares
