import pyautogui
import time
msg=('Radhe Radhe '
     'This is a trail')

while True:
    time.sleep(5)
    pyautogui.typewrite(msg)
    pyautogui.press('enter')
    time.sleep(5)

