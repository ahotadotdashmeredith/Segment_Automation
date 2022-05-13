from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from Calls.makingContentActionTakenTrackCall import driver
from Input.input import inputUrl
from selenium.webdriver.common.action_chains import ActionChains
import time


try :
    webElement ='.share-link.share-link-facebook'
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-2])
    driver.get(inputUrl)
except :
    print("Error in Final Call")