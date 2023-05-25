#!/usr/bin/env python
# coding: utf-8

# In[52]:


import pyautogui as pg
import time
from ui_macro.common import find_and_click, wait_image, i

def create_finctional_game(save_name):
    try:
        find_and_click(i('start'))
        find_and_click(i('optout_challenge'))
    except:
        find_and_click(i('start'))
        find_and_click(i('optout_challenge'))
        

    wait_image(i('start_fictional'), confidence=0.9)
    find_and_click(i('start_fictional'), confidence=0.9)

    find_and_click(i('next_step'), release_focus=True)

    wait_image(i('step_2_of_6'))
    find_and_click(i('next_step'))

    wait_image(i('step_3_of_6'))
    find_and_click(i('toggle_fantasydraft'))
    find_and_click(i('next_step'))

    wait_image(i('step_4_of_6'))
    find_and_click(i('toggle_leagueevolv'))
    find_and_click(i('next_step'))

    find_and_click(i('textinput_newgame'))
    pg.press('delete')
    pg.typewrite(save_name)
    time.sleep(1)
    find_and_click(i('next_step'), release_focus=True)

    wait_image(i('step_6_of_6'), max_wait=300)
    find_and_click(i('start_game'))

    wait_image(i('in_game_file_tab'))

    return True




