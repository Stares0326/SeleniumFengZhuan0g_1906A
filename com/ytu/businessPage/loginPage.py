'''
每一个业务视图(页面)操作:
    1.写一个类继承PageObject
    2.按照固定格式找到所有需要的元素
    3.具体的业务逻辑操作(登录操作 注册操作 加入购物车操作...)
    4.逻辑操作结果的检查
'''
from time import sleep

from selenium.webdriver.common.by import By

from com.ytu.common.selenium_driver import logger
from com.ytu.data.apiUrl import LOGIN_URL
from com.ytu.pageObject.pageObject import PageObject


class LoginPage(PageObject):
    # 找元素
    name = (By.ID,'username')
    pwd = (By.ID,'password')
    btn_login = (By.XPATH,'//button[@type="submit"]')

    # 具体的登录操作
    def loginAction(self,username,password):
        # 打开登录页面
        self.driver.get(LOGIN_URL)
        logger.info('--------打开登录页面-----------')
        sleep(2)

        logger.info('用户名:'+username)
        logger.info('密码:'+password)

        # 找到元素 进行操作
        self.find_element(*self.name).clear()
        self.find_element(*self.name).send_keys(username)

        self.find_element(*self.pwd).clear()
        self.find_element(*self.pwd).send_keys(password)

        self.find_element(*self.btn_login).click()

        logger.info('点击了登录按钮,开始登录')

    # 操作结果检查
    def checkLoginStatus(self):
        if '登录' in self.driver.title:
            logger.info('登录失败,即将截图')
            self.getScreenShot('登录失败')
            return False
        else:
            logger.info('登录成功')
            return True

















