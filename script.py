import pyautogui
import time
import keyboard

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
        pyautogui.click()

        # short break to not overload the script
        time.sleep(delay)

        # check if ESC key is pressed to stop the script
        if keyboard.is_pressed('esc'):
            print("Program stopped by user")
            break

except KeyboardInterrupt:
    print("Program stopped by user in command line")
