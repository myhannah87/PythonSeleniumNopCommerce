from selenium.webdriver.common.by import By


class Checkout_Overview_Page:

    finish_button_id = "finish"

    def __init__(self, driver):
        self.driver = driver

    def click_finish_button(self):
        self.driver.find_element(By.ID, self.finish_button_id).click()