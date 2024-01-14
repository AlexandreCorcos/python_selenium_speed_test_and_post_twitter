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


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(chrome_options)
        self.driver.maximize_window()
        self.driver.get(SPEEDTEST_URL)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(SPEEDTEST_URL)
        sleep(1)
        # close pop up
        pop_up_button = self.driver.find_element(By.ID, value="onetrust-accept-btn-handler")
        pop_up_button.click()

        # find elements using selenium

        sleep(1)
        start_button = self.driver.find_element(By.CLASS_NAME, value="start-text")
        start_button.click()

        sleep(45)
        # Result elements banner

        close_button = self.driver.find_element(By.XPATH,
                                                value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/p[2]/button')
        close_button.click()

        # Get result

        download_speed = self.driver.find_element(By.XPATH,
                                                  value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        print(download_speed.text)
        upload_speed = self.driver.find_element(By.XPATH,
                                                value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        print(upload_speed.text)

    def tweet_at_provider(self):
        self.driver.get(TWITTER_URL)
        sleep(2)

        # Find box text
        write_twitter = self.driver.find_element(By.XPATH,
                                                 value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        write_twitter.send_keys("test")


bot = InternetSpeedTwitterBot(TWITTER_URL)
# bot.get_internet_speed()
bot.tweet_at_provider()
