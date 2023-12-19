import pyautogui
import time

# define the delay between movements and the size of the square
delay = 1  # seconds
square_size = 100  # Pixel

try:
    while True:
        # move the mouse in a square pattern
        pyautogui.moveRel(square_size, 0, duration=delay)  # move right
        pyautogui.moveRel(0, square_size, duration=delay)  # move down
        pyautogui.moveRel(-square_size, 0, duration=delay) # move left
        pyautogui.moveRel(0, -square_size, duration=delay) # move up

        # short break to not overload the script
        time.sleep(delay)

except KeyboardInterrupt:
    print("Program stopped by user")
