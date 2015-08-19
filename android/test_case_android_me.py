# coding: utf-8

from appium import webdriver
import unittest
from me import *
from Gossip import *
#import test_case_android_login, test_case_android_guess, test_case_android_gossip
from test_case_android_guess import test_case_android_guess
from test_case_android_gossip import test_case_android_gossip
from test_case_android_login import test_case_android_login
import sys
import HTMLTestRunner


class test_case_android_me(unittest.TestCase):
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


    def test_change_pic(self):
        try:
            print u'\n修改我的照片，随机从我的相册中选择一张图片'
            change_mypic(self.driver)
        finally:
            self.driver.get_screenshot_as_file(get_pic_path(sys._getframe().f_code.co_name))

    def test_change_mysignature(self):
        try:
            print u'修改的我的签名，签名内容为随机生成'
            change_mysignature(self.driver)
        finally:
            self.driver.get_screenshot_as_file(get_pic_path(sys._getframe().f_code.co_name))

    def test_my_fans(self):
        try:
            print u'查看我的粉丝，随机查看一个粉丝'
            my_look_fans(self.driver, 'fans')
        finally:
            self.driver.get_screenshot_as_file(get_pic_path(sys._getframe().f_code.co_name))

    def test_my_message(self):
        try:
            print u'查看我的私信,并随机给一个人发送一条私信'
            my_message(self.driver)
        finally:
            self.driver.get_screenshot_as_file(get_pic_path(sys._getframe().f_code.co_name))


    def test_my_gossip(self):
        try:
            print u'查看我的八卦并发送一条评论'
            my_gossip(self.driver)
        finally:
            self.driver.get_screenshot_as_file(get_pic_path(sys._getframe().f_code.co_name))

    #def test_my_currency(self):
    #    try:
    #        print u'我的趣币页面随机购买一个'
    #        my_currency(self.driver)
    #    finally:
    #        self.driver.get_screenshot_as_file(get_pic_path(sys._getframe().f_code.co_name))

    def test_my_guess(self):
        try:
            print u'我的竞猜页面随机查看一个竞猜'
            my_guess(self.driver)
        finally:
            self.driver.get_screenshot_as_file(get_pic_path(sys._getframe().f_code.co_name))

    def test_my_profile(self):
        try:
            print u'修改我的个人资料'
            my_profile(self.driver)
        finally:
            self.driver.get_screenshot_as_file(get_pic_path(sys._getframe().f_code.co_name))

    def test_my_collect(self):
        try:
            print u'我的收藏页面'
            my_collect(self.driver)
        finally:
            self.driver.get_screenshot_as_file(get_pic_path(sys._getframe().f_code.co_name))

    def test_my_look(self):
        try:
            print u'我的关注页面，随机点击一个人查看他的信息'
            my_look_fans(self.driver, 'look')
        finally:
            self.driver.get_screenshot_as_file(get_pic_path(sys._getframe().f_code.co_name))


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    #添加测试用例到测试集中
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(test_case_android_me))
    suite.addTest(unittest.makeSuite(test_case_android_gossip))
    suite.addTest(unittest.makeSuite(test_case_android_guess))
    suite.addTest(unittest.makeSuite(test_case_android_login))
    #suite.addTest(test_case_android_gossip('test_gossip_comment_with_biaoping'))
    #生成测试报告文件
    file_name = "/Users/lonres/Documents/log/results/android_result.html"
    fp = file(file_name, 'wb')
    renner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试结果', description=u'测试报告')
    renner.run(suite)