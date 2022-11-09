import pytest

from generic.basetest import BaseTest
from pages.login_page import LoginPage
from pages.home_page import HomePage
import time
from generic.utility import Excel


class TestLoginPage(BaseTest):

    @pytest.mark.run(order=1)
    def test_valid_login(self):
        user_name = Excel.get_cellvalue('../data/input.xlsx', 'LoginData', 2, 1)
        password = Excel.get_cellvalue('../data/input.xlsx', 'LoginData', 2, 2)
        loginpage = LoginPage(self.driver)
        loginpage.set_username(user_name)
        loginpage.set_password(password)
        loginpage.click_login_button()
        homepage = HomePage(self.driver)
        result = homepage.verify_homepage_displayed(self.wait)
        assert result

    @pytest.mark.run(order=3)
    def test_invalid_password(self):
        loginpage = LoginPage(self.driver)
        loginpage.set_username('admin')
        loginpage.set_password('invalid')
        time.sleep(5)
        loginpage.click_login_button()
        time.sleep(5)
        result = loginpage.verify_if_error_message_is_displayed(self.wait)
        assert result

    def test_invalid_username(self):
        loginpage = LoginPage(self.driver)
        loginpage.set_username('invalid')
        loginpage.set_password('manager')
        time.sleep(5)
        loginpage.click_login_button()
        time.sleep(5)
        result = loginpage.verify_if_error_message_is_displayed(self.wait)
        assert result

    @pytest.mark.run(order=4)
    def test_blank_username_and_password(self):
        loginpage = LoginPage(self.driver)
        loginpage.set_username(' ')
        loginpage.set_password(' ')
        time.sleep(5)
        loginpage.click_login_button()
        time.sleep(5)
        result = loginpage.verify_if_error_message_is_displayed(self.wait)
        assert result
