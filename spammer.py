from pynput.keyboard import Key, Controller
import time


Keyboard = Controller()
time.sleep(2)

for i in range(50):
     for letter in "lolol":
          Keyboard.press(letter)
          Keyboard.release(letter)
     Keyboard.press(Key.enter)


