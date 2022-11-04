import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pyjavaproperties import Properties
from selenium.webdriver.chrome.options import Options


class BaseTest:
    @pytest.fixture(autouse=True)
    def pre_condition(self):
        p_file = Properties()
        p_file.load(open('config.properties'))
        url = p_file['url']
        browser = p_file['browser']
        implicit_timeout = p_file['implictTimeout']

        if browser == 'chrome':
            # options = ChromeOptions()
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            # webdriver.Remotes()
        else:
            self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(implicit_timeout)
        yield
        self.driver.quit()
