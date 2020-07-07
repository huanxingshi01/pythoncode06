from page.main_page import MainPage


class TestAddMember:
    def setup_class(self):
        self.main = MainPage()

    def test_add_member(self):
        # 1 添加成员，跳转至成员添加页面
        # 2 填写成员信息
        # 3 点击保存
        # 4 断言是否添加成功
        assert '李四' in self.main.goto_add_member().add_member().get_member()

    def test_add_member01(self):
        self.main = MainPage()
        # 1 添加成员，跳转至成员添加页面
        # 2 填写成员信息
        # 3 点击保存
        # 4 断言是否添加成功
        assert '李四' not in self.main.goto_add_member().add_member01().get_member()
        self.main.quit()