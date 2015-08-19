# coding: utf-8

from appium import webdriver
import unittest
from me import *
from Gossip import *
import sys


class test_case_android_gossip(unittest.TestCase):
    def setUp(self):
        self.desired_caps = {}
        self.desired_caps['appium-version'] = '1.4.0'
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = '4.4'
        self.desired_caps['deviceName'] = '56a1d004'
        #self.desired_caps['app'] = os.path.abspath('/Users/lonres/apppackge/android/ooch_20150812/Ooch_test.apk')
        self.desired_caps['appPackage'] = 'com.android.ooch'
        self.desired_caps['appActivity'] = 'com.android.ooch.activity.WelcomeActivity'
        self.driver = webdriver.Remote('http://0.0.0.0:4727/wd/hub', self.desired_caps)
        self.driver.implicitly_wait(60)
        welcome(self.driver)
        islogin(self.driver)
        #点击八卦页面
        self.driver.find_element_by_id('com.android.ooch:id/gossip_image').click()

    def test_create_gossip_biaoqing_only(self):
        try:
            print u'\n发布一个不带图片的有表情的八卦'
            create_gossip(self.driver, gissip_text='biaoqing')
        finally:
            self.driver.get_screenshot_as_file(get_pic_path(sys._getframe().f_code.co_name))

    def test_create_gossip_text_noly(self):
        try:
            print u'发布一个不带图片的文字八卦'
            create_gossip(self.driver, gissip_text=unicode(randomStr(10)))
        finally:
            self.driver.get_screenshot_as_file(get_pic_path(sys._getframe().f_code.co_name))

    def test_create_gossip_pic_text(self):
        try:
            print u'发布一个带图片的和文字的八卦'
            create_gossip(self.driver, gissip_text=unicode(randomStr(5)), with_pic='yes')
        finally:
            self.driver.get_screenshot_as_file(get_pic_path(sys._getframe().f_code.co_name))

    def test_share_gossip_qq(self):
        try:
            print u'随机分享一个八卦到qq'
            share_gossip(self.driver, 'qq')
        finally:
            self.driver.get_screenshot_as_file(get_pic_path(sys._getframe().f_code.co_name))

    def test_share_gossip_weibo(self):
        try:
            print u'随机分享一个八卦到微博'
            share_gossip(self.driver, 'weibo')
        finally:
            self.driver.get_screenshot_as_file(get_pic_path(sys._getframe().f_code.co_name))

    def test_search_gossip(self):
        try:
            print u'按照搜索内容：分享，查看搜索结果'
            search_gossip(self.driver, u'1')
        finally:
            self.driver.get_screenshot_as_file(get_pic_path(sys._getframe().f_code.co_name))

    def test_gossip_comment(self):
        try:
            print u'随机评论一个八卦，评论内容为随机生成'
            gossip_comment(self.driver)
        finally:
            self.driver.get_screenshot_as_file(get_pic_path(sys._getframe().f_code.co_name))

    def test_gossip_comment_with_biaoping(self):
        try:
            print u'随机选择一个八卦，评论内容为表情'
            gossip_comment(self.driver, u'表情')
        finally:
            self.driver.get_screenshot_as_file(get_pic_path(sys._getframe().f_code.co_name))

    def test_collect_gossip(self):
        try:
            print u'随机收藏一个八卦'
            collect_gossip(self.driver)
        finally:
            self.driver.get_screenshot_as_file(get_pic_path(sys._getframe().f_code.co_name))

    def test_board(self):
        try:
            print u'随机给一个艺人签到'
            board(self.driver)
        finally:
            self.driver.get_screenshot_as_file(get_pic_path(sys._getframe().f_code.co_name))

    def tearDown(self):
        self.driver.quit()

    #def suite(self):
    #    testSuite = unittest.TestSuite(map(test_case_android_gossip,
    #                                          tuple(
    #                                              filter(lambda x: x.startswith('test_'),
    #                                                     dir(test_case_android_gossip)))))
    #    return testSuite

if __name__ == "__main__":
    unittest.main()
