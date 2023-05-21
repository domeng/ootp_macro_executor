#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyautogui as pg
import time
from common import find_and_click, wait_image


# In[2]:


IMG_PATH = './images/ootp24/laptop/'


# In[3]:


find_and_click(IMG_PATH + 'start.png')


# In[4]:


find_and_click(IMG_PATH + 'optout_challenge.png')


# In[5]:


wait_image(IMG_PATH + 'start_fictional.png')
find_and_click(IMG_PATH + 'start_fictional.png')


# In[6]:


find_and_click(IMG_PATH + 'next_step.png', release_focus=True)


# In[ ]:





# In[7]:


wait_image(IMG_PATH + 'step_2_of_6.png')
find_and_click(IMG_PATH + 'next_step.png', release_focus=True)


# In[8]:


wait_image(IMG_PATH + 'step_3_of_6.png')
find_and_click(IMG_PATH + 'toggle_fantasydraft.png')
find_and_click(IMG_PATH + 'next_step.png')


# In[9]:


wait_image(IMG_PATH + 'step_4_of_6.png')
find_and_click(IMG_PATH + 'toggle_leagueevolv.png')
find_and_click(IMG_PATH + 'next_step.png')


# In[10]:


find_and_click(IMG_PATH + 'textinput_newgame.png')
pg.press('delete')
pg.typewrite('autotest_20230521')
time.sleep(1)
find_and_click(IMG_PATH + 'next_step.png', release_focus=True)


# In[11]:


wait_image(IMG_PATH + 'step_6_of_6.png', max_wait=60)
find_and_click(IMG_PATH + 'start_game.png')


# In[12]:


wait_image(IMG_PATH + 'in_game_file_tab.png')


# In[ ]:




