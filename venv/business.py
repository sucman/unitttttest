# -*- coding:utf-8 -*-
"""
第三层是服务层，几乎所有的实参都在此层传输:
"""
import uiAction


# QQ 登录
class business():
    self.qq = uiAction(appPackage, appActivity)

    '''登录'''

    def Login(self):
        self.qq.about_input('android.widget.EditText', '920100886', 'className')  # 输入用户名
        self.qq.about_input('com.tencent.mobileqq:id/password', 'drmy-9Y5a', 'id')  # 输入密码
        self.qq.about_click('com.tencent.mobileqq:id/login', 'id')  # 登录按钮

    '''清理'''

    def tui(self):
        self.qq.tearDown()
