# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import unittest
from user import User


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = WebDriver()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def open_home_page(self, driver):
        driver.get("https://www.kanopy.us/")

    def click_signup_button(self, driver):
        # open signup page
        driver.find_element(By.ID, 'button_widget_1640300835539').click()

    def test_signup(self):
        driver = self.driver
        self.open_home_page(driver)

        # Setup wait for later
        wait = WebDriverWait(driver, 10)

        # Store the ID of the original window
        original_window = driver.current_window_handle

        # Check we don't have other windows open already
        assert len(driver.window_handles) == 1

        # click signup button
        self.click_signup_button(driver)

        # Wait for the new window or tab
        wait.until(EC.number_of_windows_to_be(2))

        # Loop through until we find a new window handle
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break

        # enter new user data
        self.signup_user_data(driver, User(email="lilonann@mailinator.com", password="12345678", firstname="lil",
                                           lastname="nan"))
        # select agree checkbox
        driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div[2]/div/div[7]/div/div/div/div[2]").click()
        # click create account button

        driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div[2]/div[2]/div/button/div").click()

        # verification code field - driver.find_element_by_name("vcode").click()

    def signup_user_data(self, driver, user):
        driver.find_element(By.NAME, 'first_name').click()
        driver.find_element(By.NAME, 'first_name').send_keys(user.firstname)
        driver.find_element(By.NAME, 'last_name').clear()
        driver.find_element(By.NAME, 'last_name').send_keys(user.lastname)
        driver.find_element(By.NAME, 'email').clear()
        driver.find_element(By.NAME, 'email').send_keys(user.email)
        driver.find_element(By.NAME, 'password').clear()
        driver.find_element(By.NAME, 'password').send_keys(user.password)

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
