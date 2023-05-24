import pyautogui as pg
import time
from ui_macro.common import find_and_click, wait_image, i, select_nth_setting_option

def dump_csv():
    find_and_click(i('in_game_game_tab'))
    wait_image(i('game_tab_game_settings'))
    find_and_click(i('game_tab_game_settings'))
    wait_image(i('game_setting_database'))
    find_and_click(i('game_setting_database'))
    wait_image(i('game_setting_database_tools'))
    find_and_click(i('game_setting_database_tools'))
    
    select_nth_setting_option(-5)
    
    wait_image(i('in_game_game_tab'), max_wait=300) # wait until loading progress bar is gone

def dump_player_roaster():
    find_and_click(i('in_game_game_tab'))
    wait_image(i('game_tab_game_settings'))
    find_and_click(i('game_tab_game_settings'))
    wait_image(i('league_settings_under_game_setting'))
    find_and_click(i('league_settings_under_game_setting'))

    x = pg.locateAllOnScreen(i('partial_export_btn'), grayscale=True, confidence=0.99)
    # export roster, stats, retired numbers
    export_btns = sorted([box for box in x], key=lambda b: b.top)
    print (export_btns)
    x = export_btns[0].left + export_btns[0].width/2
    y = export_btns[0].top + export_btns[0].height/2
    pg.click(x,y)

    wait_image(i('ok'))
    find_and_click(i('ok'))

    # wth... second popup has different color 
    wait_image(i('ok_light'))
    find_and_click(i('ok_light'))