from constants import *
from googlemaps import *
from time import sleep as wait
from typing import List, Text
from util import *

def get_fares_from_google_maps():
    fares_waiting: set = load_fares_waiting(TARGET_STATIONS)
    fare_count: int = file_counter(FARES)

    if DEST in fares_waiting:
        fares_waiting.remove(DEST)

    stations: List[Text] = list(fares_waiting)
    stations.sort()

#     wait(3)  # manually switch desktop
    goto_search_input()
    enter_text(f"{DEST} Station")
    wait(3)
    locate_directions_arrow()
    wait(2)

    # input the station starting points
    while len(stations) > 0:
        errors = 0
        station = stations.pop(0)
        change_starting_station(f"{station} Station") 

        if errors > 20:
            LOG.debug("Too many errors. Quitting...")
            exit()
        if station not in load_stations(ISSUE_STATIONS):
            if capture_fare(station):
                fare_count += 1
            else:
                LOG.debug(f"Fare not found: {station} to {DEST}")
                with open(ISSUE_STATIONS, "a+") as f:
                    f.write(station+"\n")
                errors += 1
