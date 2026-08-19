from selenium.webdriver.common.by import By


class Checkout_Your_Info_Page:

    first_name_id = "first-name"
    last_name_id = "last-name"
    zip_code_id = "postal-code"
    cancel_button_id = "cancel"
    continue_button_id = "continue"

    def __init__(self, driver):
        self.driver = driver

    def enter_first_name(self, first_name):
        self.driver.find_element(By.ID, self.first_name_id).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(By.ID, self.last_name_id).send_keys(last_name)

    def enter_zip_code(self, zip_code):
        self.driver.find_element(By.ID, self.zip_code_id).send_keys(zip_code)

    def click_cancel_button(self):
        self.driver.find_element(By.ID, self.cancel_button_id).click()

    def click_continue_button(self):
        self.driver.find_element(By.ID, self.continue_button_id).click()
