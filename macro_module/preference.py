import pyautogui as pg
import time
from macro_module.common import find_and_click, wait_image, i

def setup_dump_all_game_logs():
    find_and_click(i('in_game_game_tab'))
    wait_image(i('game_tab_game_settings'))
    find_and_click(i('game_tab_game_settings'))

    wait_image(i('game_setting_save_game_logs_from'))
    pos = pg.locateCenterOnScreen(i('game_setting_save_game_logs_from'), grayscale = True)
    pos2 = pg.locateCenterOnScreen(i('human_teams'), grayscale = True, region=(pos.x,pos.y-20,pos.x+1920,pos.y+20)) 
    print(pos2)
    if pos2 != None:
        pg.click(pos2)
        time.sleep(0.5)
        pg.press('down')
        time.sleep(0.5)
        pg.keyDown('enter')
        time.sleep(0.1)
        pg.keyUp('enter')
    else:
        raise Exception("Can't find 'Human Teams' img after 'Save Game Logs from' menu")

def setup_do_not_disturb():
    find_and_click(i('jim_smith_manager_name'))
    wait_image(i('manager_options'))
    find_and_click(i('manager_options'))
    wait_image(i('toggle_donotdisturb'))
    find_and_click(i('toggle_donotdisturb'))