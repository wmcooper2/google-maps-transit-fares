import pyautogui
from time import sleep as wait
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

def load_stations():
    with open("example/stations.txt", "r") as f:
        return [line.strip() for line in f.readlines()]
