import unittest

from com.ytu.common.selenium_driver import selenium_driver


class MyUnit(unittest.TestCase):

    def setUp(self):
        # 真正获取驱动的位置....selenium_driver()函数只在这里调用一次
        self.driver = selenium_driver()

    def tearDown(self):
        self.driver.quit()