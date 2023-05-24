#!/usr/bin/env python
# coding: utf-8
import pyautogui as pg
import time
from pyscreeze import Point
from ui_macro import const

def select_nth_setting_option(n):
    if n >= 0:
        for i in range(n):
            pg.press('down')
            time.sleep(0.5)
    else:
        pg.press('end')
        time.sleep(0.5)
        pg.press('end')
        time.sleep(0.5)
        for i in range(-n-1):
            pg.press('up')
            time.sleep(0.5)
    pg.keyDown('enter')
    time.sleep(0.1)
    pg.keyUp('enter')

def i(filename):
    return const.IMG_PATH + filename + ".png"

def find_and_click(img, grayscale = True, confidence=0.99, fail_on_not_found=True, **kwargs):
    pos = pg.locateCenterOnScreen(img, grayscale = grayscale, confidence = confidence)
    if pos is None:
        if fail_on_not_found:
            raise Exception("Can't find img")
        return False
   
    if kwargs.get('offset_x', 0) != 0:
        pos = Point(pos.x + kwargs.get('offset_x', 0), pos.y)

    pg.moveTo(pos)
    pg.click()
    time.sleep(0.5)
    
    if kwargs.get('release_focus', None):
        pg.moveTo(1, 1) # temporal hack
    return True

def wait_image(img, grayscale=True, confidence=0.99, max_wait=10, fail_on_not_found = True):
    for it in range(max_wait):
        pos = pg.locateCenterOnScreen(img, grayscale = grayscale, confidence = confidence)
        if pos != None:
            return True
        time.sleep(1)
    if fail_on_not_found:
        raise Exception("Can't find img")
    return False

def find_and_click_setting_value(img, grayscale = True, confidence=0.99, fail_on_not_found=True, **kwargs):
    pos = pg.locateCenterOnScreen(img, grayscale = grayscale)
    print(pos)
    pos2 = pg.locateCenterOnScreen(i('game_setting_down_arrow'), grayscale = grayscale, region=(pos.x,pos.y-20,pos.x+1920,pos.y+20))
    
    if pos2 is None:
        if fail_on_not_found:
            raise Exception("Can't find img")
        return False

    pg.moveTo(pos2)
    pg.click()
    return True


