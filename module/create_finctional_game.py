#!/usr/bin/env python
# coding: utf-8

# In[52]:


import pyautogui as pg
import time
from module.common import find_and_click, wait_image

def create_finctional_game(img_path):
    find_and_click(img_path + 'start.png')

    find_and_click(img_path + 'optout_challenge.png')

    wait_image(img_path + 'start_fictional.png')
    find_and_click(img_path + 'start_fictional.png')

    find_and_click(img_path + 'next_step.png', release_focus=True)

    wait_image(img_path + 'step_2_of_6.png')
    find_and_click(img_path + 'next_step.png')

    wait_image(img_path + 'step_3_of_6.png')
    find_and_click(img_path + 'toggle_fantasydraft.png')
    find_and_click(img_path + 'next_step.png')

    wait_image(img_path + 'step_4_of_6.png')
    find_and_click(img_path + 'toggle_leagueevolv.png')
    find_and_click(img_path + 'next_step.png')

    find_and_click(img_path + 'textinput_newgame.png')
    pg.press('delete')
    pg.typewrite('autotest_20230521')
    time.sleep(1)
    find_and_click(img_path + 'next_step.png', release_focus=True)

    wait_image(img_path + 'step_6_of_6.png', max_wait=300)
    find_and_click(img_path + 'start_game.png')

    wait_image(img_path + 'in_game_file_tab.png')

    return True




