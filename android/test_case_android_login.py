# coding: utf-8

from appium import webdriver
import unittest
from me import *
from Gossip import *
import time, sys


class test_case_android_login(unittest.TestCase):
    def setUp(self):
        self.desired_caps = {}
        self.desired_caps['appium-version'] = '1.4.0'
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = '4.4'
        self.desired_caps['deviceName'] = '56a1d004'
        #self.desired_caps['app'] = os.path.abspath('/Users/lonres/apppackge/android/ooch_20150812/Ooch_test.apk')
        self.desired_caps['appPackage'] = 'com.android.ooch'
        self.desired_caps['appActivity'] = 'com.android.ooch.activity.WelcomeActivity'
        #
        self.driver = webdriver.Remote('http://0.0.0.0:4727/wd/hub', self.desired_caps)
        self.driver.implicitly_wait(60)
        welcome(self.driver)
        islogin(self.driver)
        #点击个人资料页面
        self.driver.find_element_by_id('com.android.ooch:id/me_image').click()

    def test_login(self):
        try:
            print u'\n正确的用户名：gong，密码：123456登录app成功'
            login(self.driver, u'gong', u'123456')
        finally:
            self.driver.get_screenshot_as_file(get_pic_path(sys._getframe().f_code.co_name))

    def test_resgister(self):
        try:
            print u'注册%s，123456成功' % unicode(resgister(self.driver, unicode(randomStr(5)), u'123456', method=True))
        finally:
            self.driver.get_screenshot_as_file(get_pic_path(sys._getframe().f_code.co_name))

    def test_error_morename(self):
        try:
            name = unicode(randomStr(30))
            print u'超长的用户名:%s注册失败' % unicode(resgister(self.driver, name, u'123456', method=False))
        finally:
            self.driver.get_screenshot_as_file(get_pic_path(sys._getframe().f_code.co_name))

    def test_three_qq(self):
        try:
            print u'测试三方登录：qq'
            three_login(self.driver, 'qq')
        finally:
            self.driver.get_screenshot_as_file(get_pic_path(sys._getframe().f_code.co_name))

    def test_three_weibo(self):
        try:
            print u'测试三方登录：weibo'
            three_login(self.driver, 'weibo')
        finally:
            self.driver.get_screenshot_as_file(get_pic_path(sys._getframe().f_code.co_name))


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(defaultTest='suite')
