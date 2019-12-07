import pyautogui
from time import sleep
from fileparser import parser 
from pprint import pprint
from typing import Any, Text, Tuple

# pprint(parser("data/trains/Keio.txt"))

print("window size: ", pyautogui.size())
width, height = pyautogui.size()

# pause length between pyautogui function calls
pyautogui.PAUSE = 1

# failsafe, crash program when you move the cursor to the upper left corner
pyautogui.FAILSAFE = True

def controlling_keyboard_example():
    sleep(3)
    pyautogui.typewrite("Hello")
    pyautogui.press("enter")
#     pyautogui.typewrite("お腹すいた") # doesn't automatically handle 日本語
# controlling_keyboard_example()


def move_mouse_example(): 
    for i in range(2):
        pyautogui.moveRel(100, 100, duration=0.25)
        print(pyautogui.position())
        pyautogui.moveRel(200, 100, duration=0.25)
        print(pyautogui.position())
        pyautogui.moveRel(200, 200, duration=0.25)
        print(pyautogui.position())
        pyautogui.moveRel(100, 200, duration=0.25)
        print(pyautogui.position())


def mouse_pos():
    running = True
    print("Press <ctrl+c> to quit.")
    try:
        while running:
#             sleep(0.1)
            x, y = pyautogui.position()
            positionStr = "X: "+ str(x).rjust(4) + " Y: "+ str(y).rjust(4)
            pixelColor= pyautogui.screenshot().getpixel((x, y))
            positionStr += " RGB: " + str(pixelColor[0]).rjust(3)
            positionStr += ", " + str(pixelColor[1]).rjust(3)
            positionStr += ", " + str(pixelColor[2]).rjust(3)
            print(positionStr, end="")
            print("\b" * len(positionStr), end="", flush=True)
    except KeyboardInterrupt:
        print("\nDone.")


def draw_spiral():
    sleep(5)
    # pyautogui.click()
    distance = 300
    while distance > 0:
        pyautogui.dragRel(distance, 0, duration=0.2, button="left")
        distance= distance - 20
        pyautogui.dragRel(0, distance, duration=0.2, button="left")
        pyautogui.dragRel(-distance, 0, duration=0.2, button="left")
        distance= distance - 20
        pyautogui.dragRel(0, -distance, duration=0.2, button="left")


def scroll_example():
    sleep(3)
    pyautogui.scroll(100)


def screen_shot_example():
    im = pyautogui.screenshot()
    print(im.getpixel((0,0)))


def wait(sec: int) -> None:
    sleep(sec)

def click() -> None:
    pyautogui.moveTo()
    pyautogui.click()

# def find(img: Text) -> Tuple[int, int]:
def find(img: Text) -> Any:
    return pyautogui.locateOnScreen(img, confidence=0.8)
#     icons = pyautogui.locateAllOnScreen(img)
#     for x in icons:
#         print(x)

if __name__ == "__main__":
    wait(1)
    chrome = find("icons/googlechrome.png")
#     click()
#     find("icons/googlemaps.png")
