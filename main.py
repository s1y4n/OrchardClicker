import pyautogui as p
import keyboard as k
import time
import random

class Play:
    def __init__(self):

        tweaks = {
            "trees": (403,252),
            "leaves": (398,330),
            "apples":(410,378),
            "inc_birds":(397,463),
            "inc_leaves":(952,249),
            "inc_trees":(970,310),
            "inc_rate":(971,400),
            "birds":(962,467),
        }
        
        while True:
            for i in range(0, 200, 20):
                p.click((690, 300 + i))
            available = [i for i in tweaks.values() if p.pixelMatchesColor(i[0], i[1], (139,149,109))]
            try:
                p.click(random.choice(available))
            except:
                pass
            time.sleep(0.001)
            if k.is_pressed("e"):
                break
            else:
                pass

if __name__ == "__main__":
    app = Play()