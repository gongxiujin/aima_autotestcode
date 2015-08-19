# coding: utf-8

import unittest
from me import *
from Guess import *
import sys
from appium import webdriver
from manager import get_pic_path



class test_case_android_guess(unittest.TestCase):
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
        #到竞猜页面
        self.driver.find_element_by_id('com.android.ooch:id/lottery_image').click()

    def test_create_guss(self):
        try:
            print u'\n创建一个nicaicai竞猜，并且到web页面将该竞猜发布'
            create_guss(self.driver, u'nicaicai')
        finally:
            self.driver.get_screenshot_as_file(get_pic_path(sys._getframe().f_code.co_name))

    def test_participation_guess_hemai(self):
        try:
            print u'随机合买一个竞猜'
            participation_guess(self.driver, u'合买')
        finally:
            self.driver.get_screenshot_as_file(get_pic_path(sys._getframe().f_code.co_name))

    def test_participation_guess_goumai(self):
        try:
            print u'随机购买一个竞猜答案'
            participation_guess(self.driver, u'购买')
        finally:
            self.driver.get_screenshot_as_file(get_pic_path(sys._getframe().f_code.co_name))

    def test_participation_guess_gendan(self):
        try:
            print u'随机跟单一个竞猜'
            participation_guess(self.driver, u'跟单')
        finally:
            self.driver.get_screenshot_as_file(get_pic_path(sys._getframe().f_code.co_name))

    def test_shareto_qq(self):
        try:
            print u'随机购买一个答案，然后分享到qq'
            participation_guess(self.driver, u'购买')
            time.sleep(3)
            shareto(self.driver, u'qq')
        finally:
            self.driver.get_screenshot_as_file(get_pic_path(sys._getframe().f_code.co_name))

    def test_shareto_weibo(self):
        try:
            print u'随机购买一个答案，然后分享到微博'
            participation_guess(self.driver, u'购买')
            time.sleep(3)
            shareto(self.driver, u'weibo')
        finally:
            self.driver.get_screenshot_as_file(get_pic_path(sys._getframe().f_code.co_name))

    def test_search_guess(self):
        try:
            print u'搜索竞猜条件:test，查看内容'
            search_guess(self.driver, u'test')
        finally:
            self.driver.get_screenshot_as_file(get_pic_path(sys._getframe().f_code.co_name))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(defaultTest='suite')
