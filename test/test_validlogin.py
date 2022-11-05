from generic.basetest import BaseTest
from pages.login_page import LoginPage
from pages.home_page import HomePage


class TestLoginPage(BaseTest):

    def test_valid_login(self):
        loginpage = LoginPage(self.driver)
        loginpage.set_username('admin')
        loginpage.set_password('manager')
        loginpage.click_login_button()
        homepage = HomePage(self.driver)
        result = homepage.verify_homepage_displayed(self.wait)
        assert result


