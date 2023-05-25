import pyautogui as pg
import time
from macro_module.common import find_and_click, wait_image, i, find_and_click_setting_value, select_nth_setting_option

def optimize_run():
    find_and_click(i('in_game_game_tab'))
    wait_image(i('game_tab_game_settings'))
    find_and_click(i('game_tab_game_settings'))

    # disable preseason pred
    try:
        wait_image(i('game_setting_preseason_pred'))
    except:
        #try one more time
        wait_image(i('game_tab_game_settings'))
        find_and_click(i('game_tab_game_settings'))
        wait_image(i('game_setting_preseason_pred'))
        
    find_and_click_setting_value(i('game_setting_preseason_pred'))
    select_nth_setting_option(2) # on demand

    # disable save box score
    wait_image(i('game_setting_save_box_scores'))
    find_and_click_setting_value(i('game_setting_save_box_scores'))
    select_nth_setting_option(6) # none

    # disable save replay
    wait_image(i('game_setting_save_replay'))
    find_and_click_setting_value(i('game_setting_save_replay'))
    select_nth_setting_option(6) # none

def setup_dump_game_logs(major_only=False):
    find_and_click(i('in_game_game_tab'))
    wait_image(i('game_tab_game_settings'))
    find_and_click(i('game_tab_game_settings'))

    wait_image(i('game_setting_save_game_logs_from'))
    find_and_click_setting_value(i('game_setting_save_game_logs_from'))

    if major_only:
        select_nth_setting_option(2)
    else:
        select_nth_setting_option(1)

def setup_do_not_disturb():
    find_and_click(i('jim_smith_manager_name'))
    wait_image(i('manager_options'))
    find_and_click(i('manager_options'))
    wait_image(i('toggle_donotdisturb'))
    find_and_click(i('toggle_donotdisturb'))