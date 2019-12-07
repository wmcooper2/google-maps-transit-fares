from time import sleep as wait
from util import load_stations
from util import file_counter
from milestones import confirm_start
from googlemaps import *

fares = "fares/"
icons = "icons/"
fare_count = file_counter(fares)
stations = load_stations("data/trains/Keio.txt")
direction_arrow1 = icons+"directionarrow1.png"
direction_arrow2 = icons+"directionarrow2.png"

print(f"starting fare count: {fare_count}")
print(f"fares waiting to be collected: {stations}")
# exit()

wait(3)  # time to switch desktops
# if not confirm_start():
#     exit()


# goto_maps()
# switch_desktop()
dest = f"{stations.pop(0)} Station"
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

    # verify fare file was created 
    assert fare_count == file_counter() - 1
    fare_count += 1

print(f"fares collected: {fare_count}")
