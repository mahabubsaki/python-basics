#we can import like js in python. But here we don't have to export anything
#internel
# from function import all_sum # for import sepcific function
# from operators import * #for import all functions

# print(all_sum)

#externel

# from math import *
# from random import*

# print(randint(1,1000))

#pip packages

import pyautogui
# for i in range(0,100):
#     pyautogui.write("Lol",interval=0.2)
#     pyautogui.press("enter")

import cv2

cam = cv2.VideoCapture(0)

while True:
    _,frame = cam.read()
    cv2.imshow('my cam',frame)
    cv2.waitKey(1)