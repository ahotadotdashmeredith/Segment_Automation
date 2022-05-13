from selenium.webdriver.common.by import By
from Calls.makingPageCall import driver
from Input.input import inputUrl
from selenium.webdriver.common.action_chains import ActionChains
import time


try:
    webElement ='.general-search__icon-button'
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(inputUrl)

    time.sleep(5)

    element = driver.find_element(By.CSS_SELECTOR, webElement)
    action = ActionChains(driver)
    action.move_to_element(element)
    time.sleep(5)
    action.click(on_element=element)
    action.perform()
except:
    print('Error in Header Action Taken')