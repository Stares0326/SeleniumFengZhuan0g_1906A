
'''
PageObject 所有页面的父类
'''
import csv
import time
from selenium import webdriver

from com.ytu.common.selenium_driver import logger


class PageObject:
    # 初始化
    def __init__(self,driver):
        self.driver = driver

    # 查找元素   .....(By.ID,'input1')
    def find_element(self,*args):

        return self.driver.find_element(*args)

    def find_elements(self,*args):

        return self.driver.find_elements(*args)

    # 截图操作 ....登录失败_时间.png...desc截图描述
    def getScreenShot(self,desc):
        file = '../screen_shot/'+str(desc)+'_'+time.strftime('%Y%m%d%H%M%S')+'.png'
        self.driver.get_screenshot_as_file(file)

        logger.error('截图操作:'+str(desc))

    # 读取excel/csv表格数据..csv_file读取的文件路径,line读取哪一行
    def getCsvData(self,csv_file,line):
        file = open(file=csv_file, mode='r', encoding='utf-8-sig')

        # 把表格里面所有的数据读取,记录到reader对象
        reader = csv.reader(file)

        for index, row in enumerate(reader, 1):
            if index == line:
                return row


