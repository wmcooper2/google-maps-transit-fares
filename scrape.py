from time import sleep as wait
from util import load_stations
from util import file_counter
from util import fares_already_scraped
from milestones import confirm_start
from googlemaps import *

fares = "fares/"
icons = "icons/"
# dest = f"{stations.pop(0)} Station"
dest = "Shinjuku Station" # temp fix, delete
fare_count = file_counter(fares)
print(f"starting fare count: {fare_count}")
stations_finished = fares_already_scraped(fares)
all_stations = set(load_stations("data/trains/Keio.txt"))
fares_waiting = all_stations.difference(stations_finished)
fares_waiting.remove(dest.split()[0]) # dest == start, nonsense
stations = list(fares_waiting)
print(f"fares waiting to be collected: {len(stations)}")

# stations = load_stations("data/trains/Keio.txt")
direction_arrow1 = icons+"directionarrow1.png"
direction_arrow2 = icons+"directionarrow2.png"
wait(3)  # time to switch desktops
# goto_maps()
# switch_desktop()

goto_search_input()
enter_text(dest)
# verify destination was entered

# something weird with the arrows and the change that happens next
try: 
    locate_click(direction_arrow1)
except TypeError:
    print("Normal arrow not found, trying other arrow")
    locate_click(direction_arrow2)


while len(stations) > 0:
    start = f"{stations.pop(0)} Station"
    change_starting_station(start) 
    capture_fare(f"{fares}{start}_{dest}.png")

    # verify new file was made
    assert fare_count == file_counter(fares) - 1
    fare_count += 1

print(f"fares collected: {fare_count}")
