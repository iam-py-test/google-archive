# https://faun.pub/how-to-install-selenium-in-linux-e8928b2b709
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import datetime

# Set path Selenium
CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
s = Service(CHROMEDRIVER_PATH)
WINDOW_SIZE = "1920,1080"

# Options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(service=s, options=chrome_options)

dt = datetime.datetime.now()

driver.get("https://google.com")
driver.save_screenshot("screenshots/google.com/{}_google.png".format(dt.strftime("%H_%d_%m_%Y")))
driver.get("https://duckduckgo.com")
driver.save_screenshot("screenshots/duckduckgo.com/{}_duckduckgo.png".format(dt.strftime("%H_%d_%m_%Y")))
driver.close()
