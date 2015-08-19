# coding: utf-8
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
import os
from appium import webdriver

success = True
desired_caps = {}
desired_caps['appium-version'] = '1.0'
desired_caps['platformName'] = 'iOS'
desired_caps['platformVersion'] = '8.1.1'
desired_caps['deviceName'] = 'iPhone 5'
desired_caps['udid'] = 'd8d2c6e304c64345b05753f86a283c37a99d5ff2'
desired_caps['app'] = os.path.abspath('/Users/lonres/apppackge/IOS/卧趣_1.0.4_测试环境_0729.ipa')

wd = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
wd.implicitly_wait(60)


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


try:
    wd.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[4]').click()
    WebDriverWait(wd, 10).until(
        lambda x: x.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[1]'))
    wd.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIATextField[1]').send_keys('3')
    wd.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[3]').click()
    time.sleep(10)

finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
