import time


def finalCall(driver, inputUrl):
    try :
        time.sleep(8)
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[-1])
        driver.get(inputUrl)
        time.sleep(10)
    except :
        print("Error in Final Call")
    return driver