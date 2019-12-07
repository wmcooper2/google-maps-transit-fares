import pyautogui
from typing import Text
from time import sleep as wait
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True


# silence tkinter warning from pyautogui, doesnt work
# TK_SILENCE_DEPRECATION = 1


def goto_maps():
    """Opens Google Maps in Chrome browser. Returns None."""
    # find google chrome, center mouse on icon
    chrome_x, chrome_y = pyautogui.locateCenterOnScreen("icons/googlechrome.png", confidence=0.9)

    # weird thing with the dock, it moves the icon to the left a little.
    pyautogui.moveTo(chrome_x-20, chrome_y)
    pyautogui.click()
    wait(1)

    # expand to fullscreen, for consistency
    fullscreendot_x, fullscreendot_y = pyautogui.locateCenterOnScreen("icons/fullscreendot.png")
    pyautogui.moveTo(fullscreendot_x+3, fullscreendot_y+3)
    pyautogui.click()
    wait(1)

    # if maps icon is still on the screen click again
    pyautogui.click()
    wait(1)

    # find google maps, click
    maps_x, maps_y = pyautogui.locateCenterOnScreen("icons/googlemaps.png")
    pyautogui.moveTo(maps_x, maps_y)
    pyautogui.click()

    # if maps icon is still on the screen click again
    if pyautogui.locateCenterOnScreen("icons/googlemaps.png"):
        pyautogui.moveTo(maps_x, maps_y)
    pyautogui.click()
wait(1)


def switch_desktop():
    """Move to the left desktop. Returns None."""
    pyautogui.hotkey("ctrl", "left")
    wait(1)


def goto_search_input():
    """Puts focus on the Google Maps search input field."""
    try:
        search_x, search_y = pyautogui.locateCenterOnScreen(
                "icons/searchinput.png", confidence=0.9,
                region=(50, 100, 250, 200))
        pyautogui.moveTo(search_x, search_y)
    except TypeError:
#         pyautogui.alert(text='Google Maps search input not found', title='', button='OK')
        print("Search input not found. Quitting...")
        exit()
    pyautogui.click()


def enter_text(dest: Text) -> None:
    """Enter text into search input. Returns None."""
    pyautogui.typewrite(dest, interval=0.1)
    pyautogui.press("enter")
    wait(3)


def locate(image: Text) -> None:
    """Moves mouse to image. Returns None."""
    transitX, transitY = pyautogui.locateCenterOnScreen(
            image, confidence=0.9)
    pyautogui.moveTo(transitX, transitY)


def locate_click(image: Text) -> None:
    """Locates, clicks image. Returns None."""
    dirX, dirY = pyautogui.locateCenterOnScreen(
        image, confidence=0.9)
    pyautogui.moveTo(dirX, dirY)
    pyautogui.click()


def capture_fare(saveto: Text) -> None:
    """Screenshot the first fare price. Returns None."""
    yenX, yenY = pyautogui.locateCenterOnScreen(
            "icons/yen.png", confidence=0.9)
    pyautogui.moveTo(yenX, yenY)
    price = pyautogui.screenshot(region=(yenX-10, yenY-10, 45, 20))
    price.save(saveto)
    print(f"saved: {saveto}")


def change_starting_station(start: Text) -> None:
    """Changes the starting station. Returns None."""
    locate("icons/transit.png")
    pyautogui.moveRel(0, 45)
    pyautogui.click()
    enter_text(start)
