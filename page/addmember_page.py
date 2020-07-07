import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.contact_page import Contact


class AddMember(BasePage):

    def add_member(self):
        self.find(By.ID, "username").send_keys("李四")
        self.find(By.ID, "memberAdd_acctid").send_keys("lisi")
        self.find(By.ID, "memberAdd_phone").send_keys("18713128662")
        self.find(By.CLASS_NAME, "js_btn_save").click()
        return Contact(self.driver)

    def add_member01(self):
        self.find(By.ID, "username").send_keys("李四01")
        self.find(By.ID, "memberAdd_acctid").send_keys("lisi01")
        self.find(By.ID, "memberAdd_phone").send_keys("18713128662")
        self.find(By.CLASS_NAME, "js_btn_save").click()
        self.find(By.CLASS_NAME, "js_btn_cancel").click()
        return Contact(self.driver)