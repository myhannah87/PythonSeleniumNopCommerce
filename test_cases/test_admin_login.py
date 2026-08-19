import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import read_config
from utilities.custom_logger import log_maker

class Test_01_Admin_Login:
    url = read_config.getURL()
    username = read_config.get_username()
    password = read_config.get_password()
    locked_out_user = read_config.get_lockedOutUser()
    invalid_user = read_config.get_invalidUser()
    logger = log_maker.log()

    @pytest.mark.regression
    def test_title_verification(self, setup):
        self.logger.info("*************Test_01_Admin_Login*************")
        self.logger.info("*************verification of page title*************")
        self.driver = setup
        self.driver.get(self.url)
        actual_title = self.driver.title
        expected_title = "Swag Labs"
        if actual_title == expected_title:
            self.logger.info("*************test_title_verification matched*************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_title_verification.png")
            self.logger.info("*************test_title_verification title did not match*************")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_valid_login(self, setup):
        self.logger.info("*************test_valid_login*************")
        self.driver = setup
        self.driver.get(self.url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login_button()
        actual_dashboard_text = self.driver.find_element(By.XPATH, "//div[@class='header_secondary_container']/span").text
        if actual_dashboard_text == "Products":
            self.logger.info("*************Dashboard text found*************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_valid_admin_login.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_locked_out_login(self, setup):
        self.logger.info("*************test_locked_out_login*************")
        self.driver = setup
        self.driver.get(self.url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.locked_out_user)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login_button()
        invalid_login_text = self.driver.find_element(By.XPATH, "//div[@class='error-message-container error']/h3").text
        if invalid_login_text == "Epic sadface: Sorry, this user has been locked out.":
            self.logger.info("*************error message matches*************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_invalid_email_address_admin_login.png")
            self.driver.close()
            assert False

    def test_incorrect_user_login(self, setup):
        self.logger.info("*************test_incorrect_user_login*************")
        self.driver = setup
        self.driver.get(self.url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.invalid_user)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login_button()
        error_message = self.driver.find_element(By.XPATH, "//div[@class='error-message-container error']/h3").text
        if error_message == "Epic sadface: Username and password do not match any user in this service":
            self.logger.info("*************error text matches*************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_incorrect_admin_login.png")
            self.driver.close()
            assert False

