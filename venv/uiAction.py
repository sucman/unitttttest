# -*- coding:utf-8 -*-
"""
第二层是UI层，封装所有能看的见操作 主要有 输入 获取文本：
"""
import unittest
from HTMLTestRunner import HTMLTestRunner

import baseTools

'''UI层'''


class uiAction():
    '''初始化'''
    '''创建对象，引入baseTools'''
    self.d = baseTools(appPackage, appActivity)

    def about_click(self, locate, type):  # 参数type 判断传入定位参数的类型，调用不同的定位方式
        if type == 'id':
            self.d.MyfindID(locate).click()
        elif type == 'xpath':
            self.d.MyfindXPATH(locate).click()

        elif type == 'name':
            self.d.MyfindNAME(locate).click()

        elif type == 'className':
            self.d.MyfindCLASS_NAME(locate).click()

        elif type == 'linkText':
            self.d.MyfindLINK_TEXT(locate).click()

    '''输入'''

    def about_input(self, locate, value, type):  # 参数type 判断传入定位参数的类型，调用不同的定位方式
        self.d.MyfindID(locate).send_keys(value)
        self.d.MyfindXPATH(locate).send_keys(value)
        self.d.MyfindNAME(locate).send_keys(value)
        self.d.MyfindCLASS_NAME(locate).send_keys(value)
        self.d.MyfindLINK_TEXT(locate).send_keys(value)

    '''滑动'''

    def about_swipe(self, direction, n):
        self.d.MySwipe(direction, n)

    '''切换到H5'''

    def Switch_webview(self):
        self.d.driver._switch_to.context('WEBVIEW_cn.com.gsh.guoshihui')

    '''切换为 原生'''

    def Switch_native(self):
        self.d.driver._switch_to.context('NATIVE_APP')

    '''获取文本内容并返回数据'''

    def get_text(self, locate, type):  # type判断传入定位参数的类型
        str_Content = self.d.MyfindID(locate).text
        return str_Content

        str_Content = self.d.MyfindXPATH(locate).text

    '''退出'''

    def tearDown(self):
        self.d.driver.quit()
