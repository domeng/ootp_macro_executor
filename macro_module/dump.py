import pyautogui as pg
import time
from macro_module.common import find_and_click, wait_image, i

def dump_player_ratings():
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