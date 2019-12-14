from constants import *
from googlemaps import (
        capture_fare,
        capture_many_fares,
        change_dest_station,
        change_starting_station,
        close_directions,
        enter_text,
        goto_search_input,
        locate_directions_arrow)
from time import sleep as wait
from typing import Dict, List, Set, Text, Tuple
from util import load_stations


def scrape_fares(info: Dict[Text, Text]) -> None:
    """Begin scraping fares. Returns None."""
    first_station = True
    station_data = load_stations(info["starting_stations"])
    starting_stations = set(station_data)
    fares = {}
    for dest in load_stations(info["destinations"]):
        starting_copy = list(starting_stations.copy())
        if dest in starting_copy:
            starting_copy.remove(dest)
        if first_station:
            first_station = False  # change flag
            goto_search_input()
            enter_text(f"{dest} Station")
            wait(1)
            locate_directions_arrow()
            wait(1)
        else:
            change_dest_station(f"{dest} Station") 
            wait(3)
        while len(starting_copy) > 0:
            start = starting_copy.pop()
            change_starting_station(f"{start} Station") 
            wait(3)
            try:
                key = f"{start}_{dest}"
                fares[key] = capture_many_fares(start, dest)
            except:
                print("fares = ", fares)
    print("fares = ", fares)
    close_directions()
    return fares
