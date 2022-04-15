import random
import pyautogui as pg
import time
animal = ('Monkey','Stupid')
time.sleep(20)
for i in range(500):
    a = random.choice(animal)
    pg.write('you are '+' '+a)
    pg.press('Enter')
