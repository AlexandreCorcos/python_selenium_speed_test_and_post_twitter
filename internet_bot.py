from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Websites and variables
TWITTER_URL = "https://twitter.com/home"
TWITTER_EMAIL = "alexandrecorcos@gmail.com"
SPEEDTEST_URL = "https://www.speedtest.net/"


PROMISED_DOWN = 150
PROMISED_UP = 10

# Keep Chroe browser open after program finished
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the Chrome Webdriver
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

# Navigate to where you want
driver.get(SPEEDTEST_URL)

# close pop up
sleep(3)
pop_up_button = driver.find_element(By.ID, value="onetrust-accept-btn-handler")
pop_up_button.click()

# find elements using selenium

sleep(1)
start_button = driver.find_element(By.CLASS_NAME, value="start-text")
start_button.click()

sleep(45)
# Result elements banner

close_button = driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/p[2]/button')
close_button.click()

# Get result

download_speed = driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
print(download_speed.text)
upload_speed = driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
print(upload_speed.text)

cookies = browser.get