from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time, sys


# İnstagram Otomatik Giriş Botu

class InstagramSigninBot:
    def __init__(self, username, passwd):
        self.username = username
        self.passwd = passwd
        self.login_page = "https://www.instagram.com/"
        self.driver = None
        self.Run()

    def OpenDriver(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get(self.login_page)
        time.sleep(10)

    def Run(self):
        self.OpenDriver()

        username_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_input.send_keys(self.username)

        passwd_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        passwd_input.send_keys(self.passwd)

        login_btn = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        login_btn.click()

        time.sleep(10)
        self.driver.quit()

username = input("Enter username: ")
password = input("Enter password: ")
instagramSigninBot = InstagramSigninBot(username, password)