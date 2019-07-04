# -*- coding:utf-8 -*-
"""
最后一层采用unittest框架，根据用例调用方法， 并打印测试报告。
"""
import unittest
from HTMLTestRunner import HTMLTestRunner

import business

'''
此层 调用方法，执行用例
使用unittest框架
'''


class Case(unittest.TestCase):

    # 初始化方法 此处传入的两个参数 为QQ的 Package（包名） 和 主Activity
    def setUp(self):
        self.cs = business('com.tencent.mobileqq', '.activity.SplashActivity')

    '''调用登录方法'''

    def test_login(self):
        '''QQ登录'''
        self.cs.Login()

    def t(self):
        self.cs.tui()
        if __name__ == '__main__':
            suite = unittest.TestSuite()
            suite.addTest(Case('test_login'))

    # 创建文件 并 设置编码
    file = open('result.html', 'w+', encoding='utf-8')

    # 标题
    t = 'QQ登录自动化测试'

    # 描述
    desc = 'This is MaZhengguang TEST REPORT'

    # 测试报告
    runner = HTMLTestRunner(stream=file, title=t, description=desc)

    # 运行
    runner.run(suite)
