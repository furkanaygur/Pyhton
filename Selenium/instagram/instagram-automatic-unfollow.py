from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# *********************** Classes *************************************
class Instagram:
    def __init__(self, username, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en, en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://instagram.com")
        time.sleep(1)
        usernameInput = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        passwordInput = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)

    def unfollowUser(self, username):
        self.browser.get(f"https://www.instagram.com/{username}")
        time.sleep(2)
        unfollowBtn = self.browser.find_element_by_tag_name("button")
        if unfollowBtn.text == 'Following':
            unfollowBtn.click()
            time.sleep(1)
            self.browser.find_element_by_xpath('//button[text()="Unfollow"]').click()
        else:
            print("Already not following...")


# ******************** Main **************************

username = input("Username: ")
password = input("Password: ")

instagram = Instagram(username, password)
instagram.signIn()

usernameF = input("who do you want to unfollow: ")
instagram.unfollowUser(usernameF)

# userList = ['a','b']
# for user in userList:
#     instagram.followUser(user)
