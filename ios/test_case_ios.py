# coding: utf-8
import unittest

from appium import webdriver

from manager import *
from ios_me import *


class test_case_ios(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['appium-version'] = '1.4.8'
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '8.4'
        desired_caps['deviceName'] = 'iPhone 5c'
        #5c
        desired_caps['udid'] = '801b0f1b4f52e937cb535087b10d397c54e6d020'
        #5s
        #desired_caps['udid'] = '56f1efccdc3dfd6f7388dac67c143df8163c0038'
        desired_caps['app'] = os.path.abspath('/Users/lonres/apppackge/IOS/卧趣_1.0.4_测试环境_0729.ipa')
        self.wd = webdriver.Remote('http://127.0.0.1:4727/wd/hub', desired_caps)
        self.wd.implicitly_wait(60)
        #capabilities = {'browserName': 'Safari', 'platformName': 'iOS', 'deviceName': 'iPhone 5c',
        #                'udid': '801b0f1b4f52e937cb535087b10d397c54e6d020'}
        #self.web_driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)

    def test_login(self):
        driver = self.wd
        time.sleep(3)
        is_alert_present(driver)

        time.sleep(3)
        try:

            driver.find_element_by_name('我').click()
            #change_myprofile(driver)
            time.sleep(2)
            #print driver.get_window_size()
            #print driver.contexts

            my_profile(driver)





        except:
            logging.error(traceback.format_exc())
            logging.error('error !!!')
            print_erro_picture(driver, save_path=save_path)
            raise Exception('error!!!!')
            #finally:
            #    self.wd.quit()

    def tearDown(self):
        self.wd.quit()