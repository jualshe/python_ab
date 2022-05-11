from selenium.webdriver.firefox.webdriver import WebDriver


class Application:
    def __init__(self):
        self.driver = WebDriver()
        self.driver.implicitly_wait(30)


def open_home_page(self):
    driver = self.driver
    driver.get("https://app.kanopy.us/")


def click_signup_button(self):
    # open signup page
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


def destroy(self):
    self.driver.quit()
