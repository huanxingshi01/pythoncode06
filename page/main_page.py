import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from page.addmember_page import AddMember
from page.base_page import BasePage
from page.contact_page import Contact


class MainPage(BasePage):

    def goto_add_member(self):
        self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        return AddMember(self.driver)

    def goto_contact(self):
        return Contact(self.driver)

    def gpto_import_contact(self):
        pass
