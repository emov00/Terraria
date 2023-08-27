import cv2 
import numpy as np

def upscale(title, percent):
    img = cv2.imread(title)

    width = int(img.shape[1] * percent/100)
    height = int(img.shape[0] * percent/100)
    dim = (width, height)
    
    scaled = cv2.resize(img, dim, interpolation= cv2.INTER_AREA)
    return scaled


def bounding(title):
    img = cv2.imread(title)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    cnts = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
    i = 0
    p = []
    for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
        if cv2.contourArea(c) < 230 or cv2.contourArea(c) > 270:
            pass
        else:
            cv2.rectangle(img, (x,y), (x+w, y+h), (36, 255, 12), 2)
            i += 1
            p.append(cv2.contourArea(c))
        
    print(max(p))



    cv2.imshow('title', img)
    print(i)
    cv2.waitKey(0)




def bounding_scale(title, x):
    img = upscale(title, x)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    cnts = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
    
    for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
        if cv2.contourArea(c) < 1250 or cv2.contourArea(c) > 1800:
            pass
        else:
            cv2.rectangle(img, (x,y), (x+w, y+h), (36, 255, 12), 3)

    cv2.imshow('title', img)
    cv2.waitKey(0)

# bounding_scale('hearts.PNG', 250)


bounding('hearts.PNG')