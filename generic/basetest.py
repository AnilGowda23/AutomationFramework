import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pyjavaproperties import Properties
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.support.wait import WebDriverWait


class BaseTest:
    @pytest.fixture(autouse=True)
    def pre_condition(self):
        p_file = Properties()
        try:
            p_file.load(open('../config.properties'))
        except:
            p_file.load(open('config.properties'))

        url = p_file['url']
        browser = p_file['browser']
        implicit_timeout = p_file['implicitTimeout']
        explicit_timeout = p_file['explicitTimeout']
        use_grid = p_file['usegrid']
        if use_grid == 'no':
            if browser == 'chrome':
                self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            else:
                self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        else:
            if browser == 'chrome':
                browser_options = ChromeOptions()
                self.driver = webdriver.Remote('https://oauth-anilkumargowda2404-9bcc3:2ccb2fee-bcc5-4d74-91d3'
                                               '-196396136283@ondemand.us-west-1.saucelabs.com:443/wd/hub',
                                               options=browser_options)
            else:
                browser_options = FirefoxOptions()
                self.driver = webdriver.Remote('https://oauth-anilkumargowda2404-9bcc3:2ccb2fee-bcc5-4d74-91d3'
                                               '-196396136283@ondemand.us-west-1.saucelabs.com:443/wd/hub',
                                               options=browser_options)

        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(implicit_timeout)
        self.wait = WebDriverWait(self.driver, explicit_timeout)
        yield
        self.driver.quit()
