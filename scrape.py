import pyautogui
from time import sleep as wait
from util import load_stations
from googlemaps import *
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
fares = "fares/"

wait(3)
# goto_maps()
# switch_desktop()
stations = load_stations()
dest = stations.pop(0)

# get directions of first station
goto_search_input()
enter_text(dest)
locate_directions_arrow()
start = stations.pop(0)
enter_text(start)
capture_fare(f"{fares}{start}_{dest}.png")

for station in stations:
    start = stations.pop(0)
    change_starting_station(start) 
    capture_fare(f"{fares}{start}_{dest}.png")
