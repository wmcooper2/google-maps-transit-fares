from constants import *
from googlemaps import *
from milestones import confirm_start
from time import sleep as wait
from util import *

dest = "Shinjuku Station" # change for different target venues
target_stations = "data/trains/TokyoMetro.txt"

#for each destination choice (decided before hand)
# dest = f"{stations.pop(0)} Station"
# all_stations = set(load_stations_long_name(STATION_FILE))

fares_waiting = load_fares_waiting(target_stations)
fare_count = file_counter(FARES)
print(f"Fares already collected: {fare_count}")

if dest in fares_waiting:
    fares_waiting.remove(dest)

stations = list(fares_waiting)
print(f"Fares waiting to be collected: {len(stations)}")

stations.sort()
print(stations[0])


#to switch desktops
wait(3)
# goto_maps()
# switch_desktop()
goto_search_input()
enter_text(dest)


#2 different versions from google maps
try: 
    locate_click(DIRECTION_ARROW1)
except TypeError:
    print("Normal arrow not found, trying other arrow")
    locate_click(DIRECTION_ARROW2)


while len(stations) > 0:
    errors = 0
    station = stations.pop(0)
    start = f"{station} Station"
    change_starting_station(start) 

    if errors > 20:
        #just quit
        print("Too many errors. Quitting...")
        exit()
    if station in load_stations(ISSUE_STATIONS):
        continue
    else:
        # if capturing the fare image was successful
        if capture_fare(f"{FARES}{start}_{dest}.png"):
#             assert fare_count == file_counter(FARES) - 1
            fare_count += 1
        else:
            print("Unable to locate the fare. Quitting...")
            # add station to issue file
            with open(ISSUE_STATIONS, "a+") as f:
                f.write(station+"\n")
            errors += 1


print(f"fares collected: {fare_count}")
