import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By
from pathlib import Path


def performEvent(driver, className, scroll):
    time.sleep(7)
    driver.switch_to.window(driver.window_handles[0])
    driver.execute_script(f'window.scrollTo(0, "{scroll}")')
    webElement = driver.find_element(By.CSS_SELECTOR, className)
    action = ActionChains(driver)
    action.move_to_element(webElement)
    time.sleep(5)
    action.click(on_element=webElement)
    action.perform()
    time.sleep(7)
    return driver


def performVideoEvents(driver, name):
    webElement = driver.find_element(By.CSS_SELECTOR, name)
    action = ActionChains(driver)
    action.move_to_element(webElement)
    time.sleep(5)
    action.click(on_element=webElement)
    action.perform()
    time.sleep(12)
    return driver


def executeSheetEvents(driver, sheetName, parPath):
    df = readingEventInput(sheetName, parPath)
    if (sheetName == 'GENERALVIDEO'):
        driver.execute_script(f'window.scrollTo(0, "{450}")')
        time.sleep(40)
        for i in range(1, len(df)):
            try:
                className, scroll = readingEventParameter(df, i)
                driver = performVideoEvents(driver, className)
            except:
                print('Error in Video Event')
    else:
        for i in range(1, len(df)):
            try:
                className, scroll = readingEventParameter(df, i)
                driver = performEvent(driver, className, scroll)
            except:
                print('Error in Event')
    return driver


def readingEventInput(sheetName, parPath, relpath='Files\\Events\\Events.xlsx'):
    path = Path(parPath) / Path(relpath)
    excel_data = pd.read_excel(path, sheetName)
    df = pd.DataFrame(excel_data)
    df = df.fillna(0)
    return df


def readingEventParameter(df, i):
    className = df['className'][i]
    scroll = df['Scroll'][i]
    className = '.' + className.replace(' ', '.')
    return className, scroll


def performingGeneralEvents(driver, parPath):
    sheetName = 'GENERAL'
    driver = executeSheetEvents(driver, sheetName, parPath)
    return driver


def performingGeneralVideoEvents(driver, parPath):
    sheetName = 'GENERALVIDEO'
    driver = executeSheetEvents(driver, sheetName, parPath)
    return driver


def performingEvent(driver, inputUrl, sheetName, viewType, parPath):
    driver = performingGeneralEvents(driver, parPath)
    if(viewType == 'Video'):
        driver = performingGeneralVideoEvents(driver, parPath)
    driver = executeSheetEvents(driver, sheetName, parPath)
    return driver


if __name__ == '__main__':
    print(readingEventInput('BIO', Path.cwd().parent))
