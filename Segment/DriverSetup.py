from seleniumwire import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#
#
# caps = DesiredCapabilities.CHROME
# caps['goog:loggingPrefs'] = {'performance': 'ALL'}
# driver = webdriver.Chrome()

from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())




