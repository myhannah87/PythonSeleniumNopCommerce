from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#Locators on Products Page
class Products_Page:
    price_dropdown_xpath = "//div[@class='right_component']/span"
    sl_onesie_id = 'add-to-cart-sauce-labs-onesie'
    sl_bike_light_id = 'add-to-cart-sauce-labs-bike-light'
    sl_bolt_tshirt_id = 'add-to-cart-sauce-labs-bolt-t-shirt'
    sl_allthethings_tshirt_id = 'add-to-cart-test.allthethings()-t-shirt-(red)'
    sl_backpack_id = 'add-to-cart-sauce-labs-backpack'
    sl_fleece_jacket_id = 'add-to-cart-sauce-labs-fleece-jacket'

    def __init__(self, driver):
        self.driver = driver

    def add_sl_onesie_to_cart(self):
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()

    def add_sl_bike_light_to_cart(self):
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light').click()

    def add_sl_bolt_tshirt_to_cart(self):
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()

    def add_sl_allthethings_to_cart(self):
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-allthethings').click()

    def add_sl_backpack_to_cart(self):
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()

    def add_sl_fleece_jacket_to_cart(self):
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-fleece-jacket')

    def price_dropdown_low_to_high(self):
        price_filter_dropdown = self.driver.find_element(By.ID, self.price_dropdown_xpath)
        select = Select(price_filter_dropdown)
        select.select_by_visible_text('Price (low to high)')

    def click_shopping_cart(self):
        self.driver.find_element(By.XPATH, "//div[@class='shopping_cart_container']").click()





