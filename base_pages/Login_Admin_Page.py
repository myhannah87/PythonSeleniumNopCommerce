import time

from selenium.webdriver.common.by import By


class Login_Admin_Page:
    login_username = "user-name"
    login_password = "password"
    login_button = "login-button"
    burger_button = "react-burger-menu-btn"
    logout_button = "logout_sidebar_link"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.login_username).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.login_password).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.ID, self.login_button).click()

    def click_burger_button(self):
        self.driver.find_element(By.ID, self.burger_button).click()

    def click_logout_button(self):
        self.driver.find_element(By.ID, self.burger_button).click()
        self.driver.find_element(By.ID, self.logout_button).click()

    def login(self, username, password):
        self.driver.find_element(By.ID, self.login_username).send_keys(username)
        self.driver.find_element(By.ID, self.login_password).send_keys(password)
        self.driver.find_element(By.ID, self.login_button).click()




