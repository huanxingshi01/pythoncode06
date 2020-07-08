from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _base_url = None

    def __init__(self, driverbase: WebDriver = None):

        if driverbase is None:
            option = Options()
            option.debugger_address = "localhost:9222"
            self.driver = webdriver.Chrome(options=option)
            # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        else:
            self.driver = driverbase

        if self._base_url is not None:
            self.driver.get(self._base_url)

    def find(self, by, value):
        return self.driver.find_element(by=by, value=value)

    def finds(self, by, value):
        return self.driver.find_elements(by=by, value=value)

    def waits(self, by, value):
        return WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located
                                                   ((by, value)))

    def quit(self):
        self.driver.quit()
