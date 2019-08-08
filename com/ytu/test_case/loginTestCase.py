from com.ytu.businessPage.loginPage import LoginPage
from com.ytu.common.myunit import MyUnit


class LoginTestCase(MyUnit):

    csv_file = '../data/user.csv'

    def testLogin_01(self):

        # 初始化登录页面对象
        l = LoginPage(self.driver)

        # 读取一行数据
        row = l.getCsvData(csv_file=self.csv_file,line=1)

        # 调用登录操作
        l.loginAction(row[0],row[1])

        # 断言
        self.assertTrue(l.checkLoginStatus())

    def testLogin_02(self):
        # 初始化登录页面对象
        l = LoginPage(self.driver)

        # 读取一行数据
        row = l.getCsvData(csv_file=self.csv_file, line=2)

        # 调用登录操作
        l.loginAction(row[0], row[1])

        # 断言
        self.assertTrue(l.checkLoginStatus())

    def testLogin_03(self):
        # 初始化登录页面对象
        l = LoginPage(self.driver)

        # 读取一行数据
        row = l.getCsvData(csv_file=self.csv_file, line=3)

        # 调用登录操作
        l.loginAction(row[0], row[1])

        # 断言
        self.assertTrue(l.checkLoginStatus())