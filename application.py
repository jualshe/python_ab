from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver


class Application:
    def __init__(self):
        # self.destroy = None
        self.driver = WebDriver()
        self.driver.implicitly_wait(30)

    def open_home_page(self):
        driver = self.driver
        driver.get("https://app.kanopy.us/")

    def click_signup_button(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Create an account").click()

    def signup_user_data(self, user):
        driver = self.driver
        driver.find_element(By.NAME, 'first_name').click()
        driver.find_element(By.NAME, 'first_name').send_keys(user.firstname)
        driver.find_element(By.NAME, 'last_name').clear()
        driver.find_element(By.NAME, 'last_name').send_keys(user.lastname)
        driver.find_element(By.NAME, 'email').clear()
        driver.find_element(By.NAME, 'email').send_keys(user.email)
        driver.find_element(By.NAME, 'password').clear()
        driver.find_element(By.NAME, 'password').send_keys(user.password)

    def select_agree_checkbox(self):
        driver = self.driver
        driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div[2]/div/div[7]/div/div/div/div[2]").click()
        driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div[2]/div[2]/div/button/div").click()

    def destroy(self):
        driver = self.driver
        self.driver.quit()
