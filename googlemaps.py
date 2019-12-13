try:
    from PIL import Image
except ImportError:
    import Image

from constants import *
import csv
from pathlib import Path
import pyautogui
import pytesseract
from typing import Text
from time import sleep as wait
from util import image_to_fare
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True


def goto_maps():
    """Opens Google Maps in Chrome browser. Returns None."""
    chrome_x, chrome_y = pyautogui.locateCenterOnScreen(
            CHROME, confidence=0.9)

    # weird thingthe dock, it moves the icon to the left a little.
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
    pyautogui.typewrite(dest, interval=0.15)
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
    attempts, max_attempts = 0, 5
    while attempts < max_attempts:
        try: 
            locate_click(ARROW1)
            attempts += max_attempts
        except TypeError:
            LOG.debug("{ARROW1} not found. Trying {ARROW2}.")
            locate_click(ARROW2)
            attempts += max_attempts
        except:
            attempts += max_attempts
        wait(2)
        attempts += 1


def capture_fare(start: Text, dest: Text) -> int:
    """Screenshot the first fare price. Returns int."""
    save_to: Text = f"{FARES}{start}_{dest}.png"
    attempts = 0
    max_attempts = 5
    actual_fare = 0
    while attempts < max_attempts:
        try:
            yenX, yenY = pyautogui.locateCenterOnScreen(YEN,
                    region=(50, 460, 80, 50), confidence=0.9)
            pyautogui.moveTo(yenX, yenY)
            img = pyautogui.screenshot(
                region=(yenX-10, yenY-10, 60, 20))
            img.save(save_to)
            actual_fare = image_to_fare(img)  # pytesseract
#             with open("results/TokyoMetro.txt", "a+") as f:
#                 csvfile = csv.writer(f, delimiter=",")
#                 csvfile.write([actual_fare, start, dest])
#                f.write(f"{actual_fare}_{start}_{dest}\n")
#             return actual_fare
        except TypeError:
#             LOG.debug("Yen not found, capture_fare(). Skipping...")
            print("Yen not found, capture_fare(). Skipping...")
        except:
#             LOG.debug("Unknown error, capture_fare(). Quitting...")
            print("Unknown error, capture_fare(). Quitting...")
            attempts += max_attempts
        wait(1)
        attempts += 1
    return actual_fare


def change_starting_station(st_name: Text) -> None:
    """Changes starting station in search input. Returns None."""
    locate(TRANSIT)
    pyautogui.moveRel(0, 45)
    pyautogui.click()
    enter_text(st_name)


def change_dest_station(st_name: Text) -> None:
    """Changes dest station in search input. Returns None."""
    locate(TRANSIT)
    pyautogui.moveRel(0, 83)
    pyautogui.click()
    enter_text(st_name)
