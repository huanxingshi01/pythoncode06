from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page.base_page import BasePage


class ImportContact(BasePage):
    # 上传通讯录操作
    def upload(self):

        self.waits(By.CSS_SELECTOR, "#js_upload_file_input")
        self.find(By.CSS_SELECTOR, "#js_upload_file_input").send_keys("C:\\Users\\90619\\PycharmProjects"
                                                                      "\\pythoncode05\\test_case\\通讯录批量导入模板.xlsx")
        return ImportContact(self.driver)

    # 显示上传的通讯录文件操作
    def file_display(self):
        self.waits(By.CSS_SELECTOR, "[id = upload_file_name]")
        letter = self.find(By.CSS_SELECTOR, "[id = upload_file_name]").text
        return letter
