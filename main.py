import pyautogui as p
import keyboard as k
import time
import random

class Play:
    
        
    def __init__(self):
        title = p.locateCenterOnScreen('assets/main.png', confidence = 0.9)

        coord = {
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
            p.click(title)
            available = [i for i in coord.values() if p.pixelMatchesColor(i[0], i[1], (139,149,109))]
            birds = p.locateAllOnScreen('assets/birds.png', confidence = 0.9)
            try:
                p.click(random.choice(available))
                p.click(i for i in birds)
            except:
                pass
            time.sleep(0.001)
            if k.is_pressed("e"):   #exit
                break
            else:
                pass

if __name__ == "__main__":
    app = Play()