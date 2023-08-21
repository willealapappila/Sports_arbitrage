# Import libraries

from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Set chromedriver to constant scraping

options = Options()
# options.add_argument('--headless')
# options.add_argument('window-size = 1920x1080')

# Website to be scraped

url = 'https://rizk.com/en/sportsbook/live/football'

# Execute driver

driver = webdriver.Chrome()
driver.get(url)

# Accept cookies

accept = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')))
accept.click()

# Initialize storage

teams = []
x12 = []
both_teams_to_score = []
over_under = []
odds_events = []

# Select different markets

time.sleep(2)

# iframe = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'sportsBookIframe')))
try:
    iframe = driver.find_element(By.CLASS_NAME, 'sportsBookIframe')
except:
    print("Couldn't find ifrmae")


driver.switch_to.frame(iframe)

drops = driver.find_element(By.CLASS_NAME, 'obg-m-market-selector-wrapper')
drops.click()

# dropdowns = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'obg-m-market-selector-menu-trigger')))
# dropdowns.click()

# first_dropdown = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/obg-m-betting-layout-container/obg-m-sportsbook-layout-container/app-m-sidenav/mat-sidenav-container/mat-sidenav-content/div/div/ng-scrollbar/div/div/div/div/section/div/obg-m-lg-live-lobby-container/obg-m-live-lobby-container/obg-m-events-master-detail-container/div/obg-m-events-master-detail-filter-bar/div/obg-m-market-selector-container/div[2]/div[2]/div/div/button[2]')))
# first_dropdown.click()

# print(first_dropdown.txt)

time.sleep(2)