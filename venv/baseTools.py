# -*- coding:utf-8 -*-
"""
第一层是自己的定义一个工具层，封装了几种定位和四种滑动：
"""

import time
import warnings

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

'''工具类'''


class baseTools:
    '''初始化方法'''

    def __init__(self, appPackage, appActivity):
        warnings.simplefilter("ignore", ResourceWarning)  # 忽略警告
        desired_caps = {
            "platformName": "Android",  # 设备平台
            "deviceName": "b43d2c1",  # 设备名称
            "platformVersion": "6.0.1",  # 设备系统版本
            "appPackage": appPackage,  # 包名
            "appActivity": appActivity,  # 启动项
            "unicodeKeyboard": True,  # 此两行是为了解决字符输入不正确的问题
            "resetKeyboard": True  # 运行完成后重置软键盘的状态
        }

        # 驱动连接
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(5)

    '''id定位'''

    def MyfindID(self, id):
        ID = (By.ID, id)
        WebDriverWait(self.driver, 30, 0.1).until(EC.presence_of_all_elements_located(ID))
        return self.driver.find_element_by_id(id)

    '''xpath定位'''

    def MyfindXPATH(self, xpath):
        XPATH = (By.XPATH, xpath)
        WebDriverWait(self.driver, 30, 0.1).until(EC.presence_of_all_elements_located(XPATH))
        return self.driver.find_element_by_xpath(xpath)

    '''name定位'''

    def MyfindNAME(self, name):
        NAME = (By.NAME, name)
        WebDriverWait(self.driver, 30, 0.1).until(EC.presence_of_all_elements_located(NAME))
        return self.driver.find_element_by_name(name)

    '''class_name定位元素'''

    def MyfindCLASS_NAME(self, class_name):
        CLASS_NAME = (By.CLASS_NAME, class_name)
        WebDriverWait(self.driver, 30, 0.1).until(EC.presence_of_all_elements_located(CLASS_NAME))
        return self.driver.find_element_by_class_name(class_name)

    '''link_name定位'''

    def MyfindLINK_TEXT(self, link_text):
        LINK_TEXT = (By.LINK_TEXT, link_text)
        WebDriverWait(self.driver, 30, 0.1).until(EC.presence_of_all_elements_located(LINK_TEXT))
        return self.driver.find_element_by_name(link_text)

    '''
　　全屏滑动
　　上下滑动 X轴(宽)不变，Y轴(高)交换位置
　　左右滑动 Y轴(高)不变，X轴(宽)交换位置
　　'''

    def MySwipe(self, direction, n, duration=1000):  # direction为滑动方向（t,d,l,r 四个参数）, # n为滑动次数(n应为整数) duration 为间隔时间

        if direction == 't':  # top 上滑动
            d = self.driver
            width = d.get_window_size()['width']  # 获取宽度
            height = d.get_window_size()['height']  # 获取高度

            for i in range(n):
                d.swipe(width * 0.5, height * 0.75, width * 0.5, height * 0.25, duration)

        elif direction == 'd':  # down 下滑动
            width = d.get_window_size()['width']
            height = d.get_window_size()['height']

        elif direction == 'l':  # left 左滑动
            d.swipe(width * 0.75, height * 0.5, width * 0.25, height * 0.5, duration)

        elif direction == 'r':  # right 右滑动
            pass

    '''返回driver'''

    def Mydriver(self):
        return self.driver
