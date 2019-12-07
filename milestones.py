import pyautogui

# silence tkinter warning from pyautogui
# TK_SILENCE_DEPRECATION = 1

def confirm_start() -> None:
    """Shows confirmation prompt. Returns bool."""
#     answer = pyautogui.confirm(text='pyautogui will take control of your mouse and keyboard. Do not touch them until finished.', title='Ready to begin', buttons=['OK', 'Cancel'])
    if not answer == "OK":
        return False
    return True
        



# destination was inputed correctly

# image of fare was captured

