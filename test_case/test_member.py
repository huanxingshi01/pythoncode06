from page.main_page import MainPage


class TestMember:

    def setup_class(self):
        self.main = MainPage()

    def test_import_member(self):
        assert "通讯录批量导入模板.xlsx" == self.main.goto_import_contact().upload().file_display()

    def test_delete_member(self):
        assert "李四" not in self.main.goto_contact().delete_member().get_member()
