import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page.addmember_page import AddMember
from page.base_page import BasePage
from page.contact_page import Contact
from page.import_contact_page import ImportContact


class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    # def goto_add_member(self):
    #     self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
    #     return AddMember(self.driver)
    #
    def goto_contact(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located
                                            ((By.CSS_SELECTOR, "#menu_contacts")))
        self.find(By.CSS_SELECTOR, "#menu_contacts").click()
        return Contact(self.driver)

    # 跳转至导入通讯录页面
    def goto_import_contact(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located
                                            ((By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)")))
        self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        return ImportContact(self.driver)
