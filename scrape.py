from time import sleep as wait
from util import load_stations
from util import load_stations2
from util import file_counter
from util import fares_already_scraped
from milestones import confirm_start
from googlemaps import *

fares = "fares/"
icons = "icons/"
direction_arrow1 = icons+"directionarrow1.png"
direction_arrow2 = icons+"directionarrow2.png"
issue_stations = "data/stations/issuestations.txt"


#for each destination choice (decided before hand)
# dest = f"{stations.pop(0)} Station"
dest = "Shinjuku Station"
fare_count = file_counter(fares)
print(f"starting fare count: {fare_count}")
stations_finished = fares_already_scraped(fares)
# all_stations = set(load_stations("data/trains/Keio.txt"))
all_stations = set(load_stations2("data/stations/A.txt"))
fares_waiting = all_stations.difference(stations_finished)

# dest == start, nonsense
if dest in fares_waiting:
    fares_waiting.remove(dest)

stations = list(fares_waiting)
stations.sort()
print(stations[0])
print(f"fares waiting to be collected: {len(stations)}")
# stations = load_stations("data/trains/Keio.txt")
# exit()


#to switch desktops
wait(3)
# goto_maps()
# switch_desktop()
goto_search_input()
enter_text(dest)


#2 different versions from google maps
try: 
    locate_click(direction_arrow1)
except TypeError:
    print("Normal arrow not found, trying other arrow")
    locate_click(direction_arrow2)


while len(stations) > 0:
    errors = 0
    station = stations.pop(0)
    start = f"{station} Station"
    change_starting_station(start) 

    if errors > 20:
        #just quit
        print("Too many errors. Quitting...")
        exit()
    if station in load_stations(issue_stations):
        continue
    else:
        # if capturing the fare image was successful
        if capture_fare(f"{fares}{start}_{dest}.png"):
            assert fare_count == file_counter(fares) - 1
            fare_count += 1
        else:
            print("Unable to locate the fare. Quitting...")
            # add station to issue file
            with open(issue_stations, "a+") as f:
                f.write(station+"\n")
            errors += 1


print(f"fares collected: {fare_count}")
