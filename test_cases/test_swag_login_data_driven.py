import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import read_config
from utilities.custom_logger import log_maker
from utilities import excel_utils

class Test_02_Login:
    url = read_config.getURL()
    logger = log_maker.log()
    path = ".//test_data//python_swag_login_usernames.xlsx"
    status_list = []

    def test_valid_login_date_driven(self, setup):
        self.logger.info("*************test_valid_login_data_driven_started*************")
        self.driver = setup
        self.driver.implicitly_wait(5)
        self.driver.get(self.url)
        self.admin_lp = Login_Admin_Page(self.driver)
        #GET EXCEL ROW COUNT
        self.rows = excel_utils.get_row_count(self.path, "Sheet1")
        print("number of rows: ", self.rows)



        for r in range(2, self.rows+1):
            self.username = excel_utils.read_data(self.path, "Sheet1", r, 1)
            self.password = excel_utils.read_data(self.path, "Sheet1", r, 2)
            self.exp_login = excel_utils.read_data(self.path, "Sheet1", r, 3)
            self.admin_lp.enter_username(self.username)
            self.admin_lp.enter_password(self.password)
            self.admin_lp.click_login_button()
            time.sleep(5)
            actual_title = self.driver.title
            expected_title = "Single Page Apps for GitHub Pages"

            if actual_title == expected_title:
                if self.exp_login == "Yes":
                    self.logger.info("Test data has passed")
                    self.status_list.append("Passed")
                    self.admin_lp.click_logout_button()

                elif self.exp_login == "No":
                    self.logger.info("Test data has failed")
                    self.status_list.append("Fail")
                    self.admin_lp.click_logout_button()

            elif actual_title != expected_title:
                if self.exp_login == "Yes":
                    self.logger.info("The test data has failed")
                    self.status_list.append("Fail")
                elif self.exp_login == "No":
                    self.logger.info("The test data has passed")
                    self.status_list.append("Pass")

        print("Status list is ", self.status_list)

        if "Fail" in self.status_list:
            self.logger.info("Test admin data driven test has failed")
            assert False
        else:
            self.logger.info("Test admin data driven test has passed")
            assert True

        self.admin_lp.click_logout_button()
