from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


USERNAME = os.environ.get("YOUR_ACCOUNT_NAME")
PASSWORD = os.environ.get("YOUR_ACCOUNT_PASSWORD")
SIMILAR_ACCOUNT = os.environ.get("SIMILAR_ACCOUNT")

CHROME_DRIVER_PATH = os.environ.get("YOUR_CHROME_DRIVER_PATH")


# DRIVER.maximize_window()
# DRIVER.implicitly_wait(5)

class InstaFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome(service=Service(path))

    def login(self):
        self.driver.get("https://www.instagram.com/")
        self.driver.implicitly_wait(10)

        username_field = self.driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")
        username_field.send_keys(USERNAME)

        password_field = self.driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")
        password_field.send_keys(PASSWORD)

        login_button = self.driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]/button/div")
        login_button.click()

        time.sleep(5)

        # click on "not now" after logging in
        not_now_button = self.driver.find_element(By.XPATH, "//*[@id='react-root']/section/main/div/div/div/div/button")
        not_now_button.click()

        time.sleep(5)

        # no notification
        notification_pop_up = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div[3]/button[2]")
        notification_pop_up.click()


    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        self.driver.implicitly_wait(10)

        # click on the number of followers
        number_followers = self.driver.find_element(By.XPATH, "//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/div")
        number_followers.click()

        # scroll the accounts in the pop up
        modal = self.driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div[2]/ul/div/li[1]/div/div[2]/button/div")
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        pass


insta_follower = InstaFollower(CHROME_DRIVER_PATH)
insta_follower.login()
insta_follower.find_followers()
insta_follower.follow()