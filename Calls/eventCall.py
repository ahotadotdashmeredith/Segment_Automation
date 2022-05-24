import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By
from pathlib import Path

def readingEventInput(sheetName, parPath, relpath='Files\\Events\\Events.xlsx'):
    path = (parPath / relpath)
    excel_data = pd.read_excel(path, sheetName)
    df = pd.DataFrame(excel_data)
    df = df.fillna(0)
    return df


def performingEvent(driver, inputUrl, sheetName, parPath):
    df = readingEventInput(sheetName, parPath)
    for i in range(1, len(df)):
        className = df['className'][i]
        scroll = df['Scroll'][i]
        className = '.' + className.replace(' ','.')
        print(className)
        try:
            webElement = className
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[-1])
            driver.get(inputUrl)

            time.sleep(7)

            driver.execute_script(f'window.scrollTo(0, "{scroll}")')
            element = driver.find_element(By.CSS_SELECTOR, webElement)

            action = ActionChains(driver)
            action.move_to_element(element)
            time.sleep(5)
            action.click(on_element=element)
            action.perform()
            time.sleep(7)
        except:
            print('Error in Event')
    return driver

if __name__=='__main__':
    print(readingEventInput(Path.cwd().parent, 'BIO'))

