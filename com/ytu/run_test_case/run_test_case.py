import unittest

import time

from com.ytu.run_test_case import HTMLTestRunnerX
from com.ytu.test_case.loginTestCase import LoginTestCase

if __name__ == '__main__':
    # 1.测试套件
    suite = unittest.TestSuite()
    # 2.添加测试用例
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(LoginTestCase))
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(LoginTestCase))

    file = open(file='../reports/report_'+time.strftime('%Y%m%d%H%M%S'+'.html'),mode='wb')
    # 3.获取运行器
    runner = HTMLTestRunnerX.HTMLTestRunner(stream=file,verbosity=3,title='云OA',description='云OA测试报告')

    # 4.运行
    runner.run(suite)
