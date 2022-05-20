from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def driverCall():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver




