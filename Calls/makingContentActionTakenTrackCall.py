from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from Calls.makingClickToContentTrackCall import driver
from Input.input import inputUrl
from selenium.webdriver.common.action_chains import ActionChains
import time


try :
    webElement ='.share-link.share-link-facebook'
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(inputUrl)

    time.sleep(10)
    driver.execute_script("window.scrollTo(0, 100)")
    element = driver.find_element(By.CSS_SELECTOR, webElement)

    action = ActionChains(driver)
    action.move_to_element(element)
    time.sleep(5)
    action.click(on_element=element)
    action.perform()
except :
    print("Error in Content Action Taken")