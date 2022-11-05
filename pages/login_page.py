from selenium.webdriver.common.by import By


class LoginPage:
    __username = (By.ID, 'username')
    __password = (By.NAME, 'pwd')
    __login_button = (By.XPATH, '//div[. = "Login "]')

    def __init__(self, driver):
        self.__driver = driver

    def set_username(self, un):
        self.__driver.find_element(*self.__username).send_keys(un)

    def set_password(self, pwd):
        self.__driver.find_element(*self.__password).send_keys(pwd)

    def click_login_button(self):
        self.__driver.find_element(*self.__login_button).click()


