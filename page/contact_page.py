from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Contact(BasePage):

    def get_member(self):
        elements = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        member_list = []
        for element in elements:
            member = element.get_attribute("title")
            member_list.append(member)
        return member_list
