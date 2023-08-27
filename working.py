import cv2 
import numpy as np
from mss import mss 
import pygetwindow as gw 
import re
import time



def get_terraria():
    win_titles = gw.getAllTitles()
    pat = r"^Terraria"
    
    for i in win_titles:
        comp = re.findall(pat, i)
        if comp:
            terr = i
            break
        else:
            pass

    w = gw.getWindowsWithTitle(terr)[0]
    # w.activate()
    d = {'left': w.left, 'top': w.top, 'width': w.width, 'height': w.height}
    return d

def thresh(image,x): #old function
    gray = cv2.cvtColor(image ,cv2.COLOR_BGR2GRAY)
    t = cv2.threshold(gray, x, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    return t

def convert(img, x):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3,3), 0)
    thresh = cv2.threshold(blur, x, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    return thresh


def bounding(title):
    cnts = cv2.findContours(title, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
    count = 0
    r = []
    for c in cnts:
        area = cv2.contourArea(c)
        x,y,w,h = cv2.boundingRect(c)
        if area < 210 or area > 300:
            pass
        else:
            cv2.rectangle(title, (x,y), (x+w, y+h), (36, 255, 12), 2)
            count += 1
            r.append(area)
    return count

def capture():
    with mss() as sct:
        mon_number = 2
        mon = sct.monitors[mon_number]
        screen = get_terraria()
        screen['mon'] = mon_number
        l = []


        while True:
            img = np.array(sct.grab(screen))
            #life = img[65:120, 1600:1900]
            life = img[(screen['top'] + 74): (screen['top'] + 129), (screen['left'] - 295): (screen['left'] - 20)]
            life2 = convert(life, 170)

            time.sleep(.25)
            q = bounding(life2)
            l.append(q)
            if len(l) > 2:
                l.pop(0)

            print(l)
            cv2.imshow('test', life2)
            try:
                if l[0] < l[1]:
                    print('Gain life')
                elif l[0] > l[1]:
                    print('lost life')
                else:
                    pass
            except:
                pass

            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
        

# capture()


