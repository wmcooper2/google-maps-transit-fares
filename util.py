try:
    from PIL import Image
except ImportError:
    import Image
from constants import *
from pathlib import Path
import pyautogui
import pytesseract
from typing import Any, List, Set, Text
from time import sleep as wait
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True


def file_counter(_dir: Text) -> int:
    """Count files in _dir. Returns int."""
    return sum([1 for p in Path(_dir).iterdir()])


def fares_already_scraped(_dir: Text) -> Set[Text]:
    """Loads names of stations already looked up. Returns set."""
    return set([str(p.name).split(" ")[0] for p in Path(_dir).iterdir()])


def extract_num(num: Text) -> Text:
    """Extracts the number portion of num. Returns string."""
    return num.split("¥")[-1]


def give_user_time_to_swipe_desktop(secs: int) -> None:
    """Give user time to go to Google Maps. Returns None."""
    for i in range(secs, -1, -1):
        print(f"\rTaking control in: {i} seconds.", end="\r")
        wait(1)
    print()


def image_to_fare(img: Any) -> int:
    """Converts png image of price to a number. Returns int."""
    num = pytesseract.image_to_string(img)
    try: 
        return int(num)
    except ValueError:
        return int(extract_num(num))


def load_stations(stations: Text) -> List[Text]:
    """Load station names. Returns List.

    Example:
    If the lines in "stations" text file look like this...
        Abe
        Abekawa

    The return list looks like this...
        ["Abe", "Abekawa"]
    """

    with open(stations, "r") as f:
        return [line.strip() for line in f.readlines()]


def load_stations_long_name(stations: Text) -> List[Text]:
    """Load station names. Returns List.

    Example: 
    If the lines in "stations" text file look like this...
        Abe Station	安部駅（あべ）
        Abekawa Station	安倍川駅（あべかわ）
    
    The return list looks like this...
        ["Abe", "Abekawa"]
    """

    with open(stations, "r") as f:
        eng_jap_name = [line.strip() for line in f.readlines()]
    stations = [name.split("\t") for name in eng_jap_name]
    return [station[0].split(" ")[0] for station in stations]


def swipe_desktop(direction: Text) -> None:
    """Swipes desktop to 'direction'. Returns None."""
#     pyautogui.hotkey("ctrl", direction)
    pyautogui.keyDown ('ctrl')
    pyautogui.press ('left')
    pyautogui.keyUp ('left')
    pyautogui.keyUp ('ctrl')

