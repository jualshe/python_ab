# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = WebDriver()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def open_home_page(self, driver):
        driver.get("https://www.kanopy.us/")

    def open_signup_page(self, driver):
        # open signup page
        driver.find_element(By.ID("button_widget_1640300835539")).click()


    def test_signup(self):
        driver = self.driver
        self.open_home_page(driver)

        self.open_signup_page(driver)

        #enter new user data
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]
        # driver.find_element(By.NAME("first_name")).click()
        # driver.find_element(By.NAME("first_name")).clear()
        driver.find_element(By.NAME("first_name")).send_keys("li")
        driver.find_element_by_name("last_name").clear()
        driver.find_element_by_name("last_name").send_keys("na")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("lina@mailinator.com")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("12345678")
        #select agree checkbox
        driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div[2]/div/div[7]/div/div/div/div[2]").click()
        driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div[2]/div[2]/div/button/div").click()
        driver.find_element_by_name("vcode").click()
        #click create account button


    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
