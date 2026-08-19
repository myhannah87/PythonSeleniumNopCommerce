import random
import string

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from base_pages.Checkout_Overview_Page import Checkout_Overview_Page
from base_pages.Checkout_Your_Info_Page import Checkout_Your_Info_Page
from base_pages.Products_Page import Products_Page
from base_pages.Login_Admin_Page import Login_Admin_Page
from base_pages.Your_Cart_Page import Your_Cart_Page
from utilities.read_properties import read_config
from utilities.custom_logger import log_maker

class Test_Products_page:
    url = read_config.getURL()
    username = read_config.get_username()
    password = read_config.get_password()
    locked_out_user = read_config.get_lockedOutUser()
    invalid_user = read_config.get_invalidUser()
    logger = log_maker.log()

    @pytest.mark.regression
    def test_add_SLOnesie_to_cart(self, setup):
        self.logger.info("*************test_add_SLOnesie_to_cart*************")
        self.driver = setup
        self.driver.get(self.url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.login(self.username, self.password)
        self.products_page = Products_Page(self.driver)
        self.products_page.add_sl_onesie_to_cart()
        actual_add_cart_text = self.driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']").text
        if actual_add_cart_text == "1":
            assert True
            self.logger.info("*************test_add_SLOnesie_to_cart: Onesie was successfully added to cart*************")

        else:
            self.driver.save_screenshot(".\\screenshots\\test_add_SLOnesie_to_cart.png")
            self.logger.info("*************test_add_SLOnesie_to_cart: Onesie was NOT added to cart*************")
            assert False


        actual_SLOnesie_button_text = self.driver.find_element(By.ID, 'remove-sauce-labs-onesie').text
        if actual_SLOnesie_button_text == "Remove":
            assert True
        else:
            assert False

        self.products_page.click_shopping_cart()

        self.myCartPage = Your_Cart_Page(self.driver)
        self.myCartPage.click_shopping_button()

        self.checkout_info = Checkout_Your_Info_Page(self.driver)
        self.checkout_info.enter_first_name("Big")
        self.checkout_info.enter_last_name("Ben")
        self.checkout_info.enter_zip_code("12345")
        self.checkout_info.click_continue_button()

        self.checkout_overview = Checkout_Overview_Page(self.driver)
        self.checkout_overview.click_finish_button()
        self.logger.info("*************test_add_SLOnesie_to_cart: Checkout was successful!*************")
        self.driver.close()

    @pytest.mark.regression
    def test_add_SLBackpack_to_cart(self, setup):
        self.logger.info("*************test_add_SLBackpack_to_cart*************")
        self.driver = setup
        self.driver.get(self.url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.login(self.username, self.password)
        self.products_page = Products_Page(self.driver)
        self.products_page.add_sl_backpack_to_cart()
        actual_add_cart_text = self.driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']").text
        if actual_add_cart_text == "1":
            assert True
            self.logger.info(
                "*************test_add_SLBackpack_to_cart: Backpack was successfully added to cart*************")

        else:
            self.driver.save_screenshot(".\\screenshots\\test_add_SLBackpack_to_cart.png")
            self.logger.info("*************test_add_SLOnesie_to_cart: Backpack was NOT added to cart*************")
            assert False

        actual_SLBackpack_button_text = self.driver.find_element(By.ID, 'remove-sauce-labs-backpack').text
        if actual_SLBackpack_button_text == "Remove":
            assert True
        else:
            assert False

        self.products_page.click_shopping_cart()
        self.myCartPage = Your_Cart_Page(self.driver)
        self.myCartPage.click_shopping_button()
        self.checkout_info = Checkout_Your_Info_Page(self.driver)
        self.checkout_info.enter_first_name("Big")
        self.checkout_info.enter_last_name("Ben")
        self.checkout_info.enter_zip_code("12345")
        self.checkout_info.click_continue_button()

        self.checkout_overview = Checkout_Overview_Page(self.driver)
        self.checkout_overview.click_finish_button()
        self.logger.info("*************test_add_SLBackpack_to_cart: Checkout was successful!*************")
        self.driver.close()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_add_SLBikeLight_to_cart(self, setup):
        self.logger.info("*************test_add_SLBikeLight_to_cart*************")
        self.driver = setup
        self.driver.get(self.url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.login(self.username, self.password)
        self.products_page = Products_Page(self.driver)
        self.products_page.add_sl_bike_light_to_cart()
        actual_add_cart_text = self.driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']").text
        if actual_add_cart_text == "1":
            assert True
            self.logger.info(
                "*************test_add_SLBikeLight_to_cart: Bike Light was successfully added to cart*************")

        else:
            self.driver.save_screenshot(".\\screenshots\\test_add_SLBikeLight_to_cart.png")
            self.logger.info("*************test_add_SLBikeLight_to_cart: Bike Light was NOT added to cart*************")
            assert False

        actual_SLBikeLight_button_text = self.driver.find_element(By.ID, 'remove-sauce-labs-bike-light').text
        if actual_SLBikeLight_button_text == "Remove":
            assert True
        else:
            assert False

        self.products_page.click_shopping_cart()

        self.myCartPage = Your_Cart_Page(self.driver)
        self.myCartPage.click_shopping_button()

        self.checkout_info = Checkout_Your_Info_Page(self.driver)
        self.checkout_info.enter_first_name("Big")
        self.checkout_info.enter_last_name("Ben")
        self.checkout_info.enter_zip_code("12345")
        self.checkout_info.click_continue_button()

        self.checkout_overview = Checkout_Overview_Page(self.driver)
        self.checkout_overview.click_finish_button()
        self.logger.info("*************test_add_SLBikeLight_to_cart: Checkout was successful!*************")
        self.driver.close()

    def test_add_SLBoltTshirt_to_cart(self, setup):
        self.logger.info("*************test_add_SLBoltTshirt_to_cart*************")
        self.driver = setup
        self.driver.get(self.url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.login(self.username, self.password)
        self.products_page = Products_Page(self.driver)
        self.products_page.add_sl_bike_light_to_cart()
        actual_add_cart_text = self.driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']").text
        if actual_add_cart_text == "1":
            assert True
            self.logger.info(
                "*************test_add_SLBoltTshirt_to_cart: Bolt Tshirt was successfully added to cart*************")

        else:
            self.driver.save_screenshot(".\\screenshots\\test_add_SLBoltTshirt_to_cart.png")
            self.logger.info("*************test_add_SLBoltTshirt_to_cart: Bolt Tshirt was NOT added to cart*************")
            assert False

        actual_SLBoltTshirt_button_text = self.driver.find_element(By.ID, 'remove-sauce-labs-bolt-t-shirt').text
        if actual_SLBoltTshirt_button_text == "Remove":
            assert True
        else:
            assert False

        self.products_page.click_shopping_cart()

        self.myCartPage = Your_Cart_Page(self.driver)
        self.myCartPage.click_shopping_button()

        self.checkout_info = Checkout_Your_Info_Page(self.driver)
        self.checkout_info.enter_first_name("Big")
        self.checkout_info.enter_last_name("Ben")
        self.checkout_info.enter_zip_code("12345")
        self.checkout_info.click_continue_button()

        self.checkout_overview = Checkout_Overview_Page(self.driver)
        self.checkout_overview.click_finish_button()
        self.logger.info("*************test_add_SLBoltTshirt_to_cart: Checkout was successful!*************")
        self.driver.close()

    def test_add_SLFleeceJacket_to_cart(self, setup):
        self.logger.info("*************test_add_SLFleeceJacket_to_cart*************")
        self.driver = setup
        self.driver.get(self.url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.login(self.username, self.password)
        self.products_page = Products_Page(self.driver)
        self.products_page.add_sl_fleece_jacket_to_cart()
        actual_add_cart_text = self.driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']").text
        if actual_add_cart_text == "1":
            assert True
            self.logger.info(
                "*************test_add_SLFleeceJacket_to_cart: Fleece Jacket was successfully added to cart*************")

        else:
            self.driver.save_screenshot(".\\screenshots\\test_add_SLFleeceJacket_to_cart.png")
            self.logger.info(
                "*************test_add_SLFleeceJacket_to_cart: Fleece Jacket was NOT added to cart*************")
            assert False

        actual_SLFleeceJacket_button_text = self.driver.find_element(By.ID, 'remove-sauce-labs-fleece-jacket').text
        if actual_SLFleeceJacket_button_text == "Remove":
            assert True
        else:
            assert False

        self.products_page.click_shopping_cart()

        self.myCartPage = Your_Cart_Page(self.driver)
        self.myCartPage.click_shopping_button()

        self.checkout_info = Checkout_Your_Info_Page(self.driver)
        self.checkout_info.enter_first_name("Big")
        self.checkout_info.enter_last_name("Ben")
        self.checkout_info.enter_zip_code("12345")
        self.checkout_info.click_continue_button()

        self.checkout_overview = Checkout_Overview_Page(self.driver)
        self.checkout_overview.click_finish_button()
        self.logger.info("*************test_add_SLFleeceJacket_to_cart: Checkout was successful!*************")
        self.driver.close()

    def test_add_allTheThingsTshirt_to_cart(self, setup):
        self.logger.info("*************test_add_allTheThingsTshirt_to_cart*************")
        self.driver = setup
        self.driver.get(self.url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.login(self.username, self.password)
        self.products_page = Products_Page(self.driver)
        self.products_page.add_sl_allthethings_to_cart()
        actual_add_cart_text = self.driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']").text
        if actual_add_cart_text == "1":
            assert True
            self.logger.info(
                "*************test_add_allTheThingsTshirt_to_cart: allTheThingsTshirt was successfully added to cart*************")

        else:
            self.driver.save_screenshot(".\\screenshots\\test_add_test_add_allTheThingsTshirt_to_cart.png")
            self.logger.info(
                "*************test_add_allTheThingsTshirt_to_cart: allTheThingsTshirt was NOT added to cart*************")
            assert False

        actual_SLFleeceJacket_button_text = self.driver.find_element(By.ID, 'remove-test.allthethings()-t-shirt-(red)').text
        if actual_SLFleeceJacket_button_text == "Remove":
            assert True
        else:
            assert False

        self.products_page.click_shopping_cart()

        self.myCartPage = Your_Cart_Page(self.driver)
        self.myCartPage.click_shopping_button()

        self.checkout_info = Checkout_Your_Info_Page(self.driver)
        self.checkout_info.enter_first_name("Big")
        self.checkout_info.enter_last_name("Ben")
        self.checkout_info.enter_zip_code("12345")
        self.checkout_info.click_continue_button()

        self.checkout_overview = Checkout_Overview_Page(self.driver)
        self.checkout_overview.click_finish_button()
        self.logger.info("*************remove-test.allthethings()-t-shirt-(red): Checkout was successful!*************")
        self.driver.close()

    #function to generate random email address
def generate_random_email(self):
    username = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    domain = random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])
    return f'{username}@{domain}'