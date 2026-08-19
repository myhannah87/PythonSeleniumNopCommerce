from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


#Locators on Your Cart Page

class Your_Cart_Page:

    cart_quantity_xpath = "//div[@class='cart_quantity']"
    remove_button_id = "remove-sauce-labs-onesie"
    continue_shopping_button_id = "continue-shopping"
    checkout_button_id = "checkout"

    def __init__(self, driver):
        self.driver = driver

    def click_shopping_button(self):
        self.driver.find_element(By.ID, self.checkout_button_id).click()


