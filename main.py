import pyautogui as p
import keyboard as k
import time
import random

class Play:
    
    #define available
    def check(self, position):
        true = p.pixelMatchesColor(position, (139,149,109))
        if true:
            p.click(position)
        
        #enough life
        
    
    def upgrade_random(self, coords):
        for i in random.shuffle(coords):
            self.check(i)
    #check status
    
    


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
            time.sleep(0.001)
            self.upgrade_random(coord.values())
            #click bird
            if k.is_pressed("e"):   #exit
                break
            else:
                pass

if __name__ == "__main__":
    app = Play()