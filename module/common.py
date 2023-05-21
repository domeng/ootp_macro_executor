import pyautogui as pg


# In[2]:


def find_and_click(img, grayscale = True, confidence=0.90, fail_on_not_found=True):
    pos = pg.locateCenterOnScreen(img, grayscale = grayscale, confidence = confidence)
    if pos is None:
        if fail_on_not_found:
            raise Exception("Can't find img")
        return False
    print(pos)
    pg.click(pos)
    time.sleep(0.5)
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

