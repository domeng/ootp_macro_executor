#!/usr/bin/env python
# coding: utf-8
import pyautogui as pg
import time

def find_and_click(img, grayscale = True, confidence=0.90, fail_on_not_found=True, **kwargs):
    pos = pg.locateCenterOnScreen(img, grayscale = grayscale, confidence = confidence)
    if pos is None:
        if fail_on_not_found:
            raise Exception("Can't find img")
        return False
   
    pg.moveTo(pos)
    pg.click()
    time.sleep(0.5)
    
    if kwargs.get('release_focus', None):
        pg.moveTo(1, 1) # temporal hack
    return True

def wait_image(img, grayscale=True, confidence=0.90, max_wait=10, fail_on_not_found = True):
    for it in range(max_wait):
        pos = pg.locateCenterOnScreen(img, grayscale = grayscale, confidence = confidence)
        if pos != None:
            return True
        time.sleep(1)
    if fail_on_not_found:
        raise Exception("Can't find img")
    return False




