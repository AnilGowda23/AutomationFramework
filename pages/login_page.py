from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class LoginPage:
    __username = (By.ID, 'username')
    __password = (By.NAME, 'pwd')
    __login_button = (By.XPATH, '//div[. = "Login "]')
    __error_message = (By.XPATH, '//span[contains(text(),"Username or Password is invalid. Please try again.")]')

    def __init__(self, driver):
        self.__driver = driver

    def set_username(self, un):
        self.__driver.find_element(*self.__username).send_keys(un)

    def set_password(self, pwd):
        self.__driver.find_element(*self.__password).send_keys(pwd)

    def click_login_button(self):
        self.__driver.find_element(*self.__login_button).click()

    def verify_if_error_message_is_displayed(self, wait):
        try:
            wait.until(expected_conditions.visibility_of_element_located(self.__error_message))
            print('Unsuccessful login, error message is displayed successfully')
            return True
        except:
            print('Successfully logged into application. Error message is not displayed')
            return False


