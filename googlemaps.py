try:
    from PIL import Image
except ImportError:
    import Image
from constants import *
from pathlib import Path
from pprint import pprint
import pyautogui
import pytesseract
from typing import List, Text, Tuple
from time import sleep as wait
from util import image_to_fare
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True


def close_directions() -> None:
    """Close Google Maps directions pane. Returns None."""
    locate_click(CLOSE)

def goto_maps() -> None:
    """Opens Google Maps in Chrome browser. Returns None."""
    chrome_x, chrome_y = pyautogui.locateCenterOnScreen(
            CHROME, confidence=0.9)

    # weird thing, dock moves icon to left a little.
    pyautogui.moveTo(chrome_x-20, chrome_y)
    pyautogui.click()
    wait(1)

    # expand to fullscreen, for consistency
    fullscreen_x, fullscreen_y = pyautogui.locateCenterOnScreen(
            FULLSCREENDOT)
    pyautogui.moveTo(fullscreen_x+3, fullscreen_y+3)
    pyautogui.click()
    wait(1)

    # if maps icon is still on the screen click again
    pyautogui.click()
    wait(1)

    # find google maps, click
    maps_x, maps_y = pyautogui.locateCenterOnScreen(MAPS)
    pyautogui.moveTo(maps_x, maps_y)
    pyautogui.click()

    # if maps icon is still on the screen click again
    if pyautogui.locateCenterOnScreen(MAPS):
        pyautogui.moveTo(maps_x, maps_y)
    pyautogui.click()
    wait(1)


def goto_search_input() -> None:
    """Puts focus on the Google Maps search input field. Returns None."""
    try:
        x, y = pyautogui.locateCenterOnScreen(
            SEARCH_INPUT, confidence=0.9,
            region=(100, 120, 130, 40))
        pyautogui.click(x, y)
    except TypeError:
        LOG.debug("Search input not found. Quitting...")
        exit()


def enter_text(dest: Text) -> None:
    """Enter text into search input. Returns None."""
    pyautogui.typewrite(dest)
    pyautogui.press("enter")


def locate(image: Text) -> None:
    """Moves mouse to image. Returns None."""
    transitX, transitY = pyautogui.locateCenterOnScreen(
            image, confidence=0.9)
    pyautogui.moveTo(transitX, transitY)


def locate_click(image: Text) -> None:
    """Locates, clicks image. Returns None."""
    dirX, dirY = pyautogui.locateCenterOnScreen(image, confidence=0.9)
    pyautogui.moveTo(dirX, dirY)
    pyautogui.click()


def locate_directions_arrow() -> None:
    """Locates, clicks directions arrow image. Returns None."""
    attempts, max_attempts = 0, 3
    while attempts < max_attempts:
        try: 
            locate_click(ARROW1)
            return
        except TypeError:
            wait(attempts)  # extend time with attempts
        attempts += 1
    print("{ARROW1} not found. Trying {ARROW2}.")
    attempts, max_attempts = 0, 3
    while attempts < max_attempts:
        try: 
            locate_click(ARROW1)
            return
        except TypeError:
            wait(attempts)
        attempts += 1
    print("{ARROW2} not found. Quitting...")
    exit()


def capture_fare(start: Text, dest: Text) -> int:
    """Screenshot the first fare price. Returns int."""
    save_to: Text = f"{FARES}{start}_{dest}.png"
    attempts = 0
    max_attempts = 5
    fare = 0
    while attempts < max_attempts:
        try:
            yenX, yenY = pyautogui.locateCenterOnScreen(YEN,
                    region=(50, 460, 80, 50), confidence=0.9)
            img = pyautogui.screenshot(
                region=(yenX-10, yenY-10, 60, 20))
            img.save(save_to)
            fare = image_to_fare(img)  # pytesseract
        except TypeError:
            print("Yen not found, capture_fare(). Skipping...")
        except:
            print("Unknown error, capture_fare(). Quitting...")
            attempts += max_attempts
        wait(1)
        attempts += 1


#TODO
def capture_many_fares(start: Text, dest: Text) -> List[int]:
    """Screenshot the first fare price. Returns list of fares."""
    attempts, max_attempts = 0, 5
    fares = []
    while attempts < max_attempts:
        try:
            train_listings = list(pyautogui.locateAllOnScreen(
                TRAINRESULT, region=(10, 380, 50, 500)))
            attempts += max_attempts
            print("maxing out attempts, leaving while loop")
        except:
            print("Unknown error, capture_many_fares(). Quitting...")
            attempts += max_attempts
        wait(1)
        attempts += 1
    first_listing = train_listings[0]
    other_listings = train_listings[1:]
    train_center = pyautogui.center(first_listing)
    pyautogui.moveTo(train_center)
    fare = capture_yen(pyautogui.center(first_listing), offsetY=50)
    fares.append(fare)
    for listing in other_listings:
        train_center = pyautogui.center(listing)
        pyautogui.moveTo(train_center)
        pyautogui.click()
        wait(1)
        fare = capture_yen(train_center)
        fares.append(fare)
    return fares


def capture_yen(row: Tuple[int, int], offsetY: int = -20) -> int:
    """Capture the fare for the row. Returns int."""
    yenX, yenY = pyautogui.locateCenterOnScreen(YEN,region=(row.x+23, row.y+offsetY, 80, 80), confidence=0.9)
    img = pyautogui.screenshot(
        region=(yenX-10, yenY-10, 60, 20))
    debug_img = pyautogui.screenshot(
        region=(yenX-10, yenY-10, 60, 20))
    fare = image_to_fare(img)  # pytesseract
    return fare


def change_starting_station(st_name: Text) -> None:
    """Changes starting station in search input. Returns None."""
    locate_click(TRANSIT)
    pyautogui.moveRel(0, 45)
    pyautogui.click()
    enter_text(st_name)


def change_dest_station(st_name: Text) -> None:
    """Changes dest station in search input. Returns None."""
    locate_click(TRANSIT)
    pyautogui.moveRel(0, 83)
    pyautogui.click()
    enter_text(st_name)
