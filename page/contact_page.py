from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page.base_page import BasePage


class Contact(BasePage):

    def get_member(self):
        elements = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        member_list = []
        for element in elements:
            member = element.get_attribute("title")
            member_list.append(member)
        return member_list

    def delete_member(self):
        self.waits(By.CSS_SELECTOR, "#member_list tr:nth-child(1) input")
        self.find(By.CSS_SELECTOR, "#member_list tr:nth-child(1) input").click()

        self.waits(By.CLASS_NAME, "js_delete")
        self.find(By.CLASS_NAME, "js_delete").click()

        self.waits(By.CSS_SELECTOR, ".ww_dialog_foot a:nth-child(1)")
        self.find(By.CSS_SELECTOR, ".ww_dialog_foot a:nth-child(1)").click()
        sleep(5)
        return Contact(self.driver)
