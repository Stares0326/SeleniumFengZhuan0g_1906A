import logging
from logging import config

from selenium import webdriver

# 加载一下日志配置文件,得到打印日志的对象
config.fileConfig('../config/log.conf')
# 获取打印日志对象
logger = logging.getLogger()




# 定义一个函数 获取driver驱动
def selenium_driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()

    return driver

