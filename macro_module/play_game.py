from macro_module.common import find_and_click, wait_image, i, find_and_click_setting_value

def play_until_playoff_end():
    find_and_click(i('play'))
    find_and_click(i('until_playoff_end'))
    wait_image(i('offseason'), max_wait=600)

def play_until_preseason_begin():
    find_and_click(i('play'))
    find_and_click(i('until_preseason_begin'))
    wait_image(i('preseason'), max_wait=600)