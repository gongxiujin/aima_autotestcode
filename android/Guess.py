# coding: utf-8
from selenium.webdriver.support.ui import WebDriverWait
import random
from submit_guess import *
from manager import time, slide_up, randomStr, print_erro_picture, middle_slipe


def guess_view(driver):
    driver.find_element_by_name(u'竞猜').click()


def create_guss(driver, title='autotest_android', text=randomStr(10)):
    '''
    创建竞猜
    '''
    #点击发起竞猜按钮
    driver.find_element_by_id('com.android.ooch:id/title_img1').click()
    #点击竞猜标题输入区
    driver.find_element_by_id('com.android.ooch:id/publish_lottery_title').send_keys(title)
    #输入竞猜内容
    driver.find_element_by_id('com.android.ooch:id/publish_lottery_instr').send_keys(text)
    #循环添加两次答案
    for i in range(2):
        #点击添加答案
        driver.find_element_by_id('com.android.ooch:id/publish_lottery_add_answer').click()
        #弹出框内输入答案
        driver.find_element_by_id('android:id/custom').send_keys(randomStr(6))
        #点击确定
        driver.find_element_by_id('android:id/button1').click()
        #选择一个答案
    random.choice(driver.find_elements_by_id('com.android.ooch:id/icon')).click()
    #隐藏键盘
    driver.back()
    #driver.hide_keyboard()
    #点击添加照片
    driver.find_element_by_id('com.android.ooch:id/publish_lottery_upload').click()
    #选择添加图片
    driver.find_element_by_id('com.android.ooch:id/item_popupwindows_Photo').click()
    #随机选择一个相册
    random.choice(driver.find_elements_by_xpath(
        '//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[*]')).click()
    #随机选择一张照片
    random.choice(driver.find_elements_by_id('com.android.ooch:id/image')).click()
    #选取内容
    driver.find_element_by_id('com.android.ooch:id/finish_btn').click()
    #隐藏键盘
    #driver.back()
    #随机选择一个答案
    #random.choice(driver.find_elements_by_id('com.android.ooch:id/icon')).click()
    #选择预计开奖时间
    driver.find_element_by_id('com.android.ooch:id/publish_lottery_time').click()
    #driver.find_elements_by_id('android:id/numberpicker_input')[0].clear()
    ##随机输入一个年
    #driver.find_elements_by_id('android:id/numberpicker_input')[0].send_keys(random.choice(range(2015, 2020)))
    #if driver.find_elements_by_id('android:id/numberpicker_input')[0].text == '2015':
    #    pass
    #else:
    #    #选择月份
    #    driver.find_elements_by_id('android:id/numberpicker_input')[1].clear()
    #    driver.find_elements_by_id('android:id/numberpicker_input')[1].send_keys(random.choice(range(1, 13)))
    #    #选择日
    #    driver.find_elements_by_id('android:id/numberpicker_input')[2].clear()
    #    driver.find_elements_by_id('android:id/numberpicker_input')[2].send_keys(range(1, 31))
    #确定时间
    driver.find_element_by_id('android:id/button1').click()
    #向上滑动
    middle_slipe(driver)
    #点击并发布
    driver.find_element_by_id('com.android.ooch:id/publish_btn').click()
    time.sleep(2)
    #到web页面点击发布
    subimt_guess = submit_guess(title, 'http://123.57.239.192/admin')
    subimt_guess.modify_guess()


def participation_guess(driver, by):
    '''
    随机选择一个竞猜然后点击进入到竞猜详情页面
    by  购买、合买、跟单
    运行完之后返回到竞猜列表页面
    '''
    #随机选中一个
    driver.find_element_by_id('com.android.ooch:id/lv_lottery_item_name_tv').click()
    if by == u'购买':
        #随机选择一个
        random.choice(driver.find_elements_by_id(
            'com.android.ooch:id/buy_lottery_addIb')).click()
        #隐藏键盘
        middle_slipe(driver)
        #上划一下漏出竞猜按钮
        for i in range(2):
            middle_slipe(driver)
        #点击竞猜
        driver.find_element_by_id('com.android.ooch:id/buy_lottery_PayBtn').click()
        #确定支付
        driver.find_element_by_id('android:id/button1').click()

    elif by == u'合买':
        #随机选择一个答案
        random.choice(driver.find_elements_by_id('com.android.ooch:id/buy_lottery_nameTv')).click()
        #点击合买按钮
        driver.find_element_by_id('com.android.ooch:id/buy_lottery_hemaiBtn').click()
        #填写发起的份数
        driver.find_element_by_id('com.android.ooch:id/buy_lottery_countEt1').clear()
        driver.find_element_by_id('com.android.ooch:id/buy_lottery_countEt1').send_keys('210')
        #填写认购的份数
        driver.find_element_by_id('com.android.ooch:id/buy_lottery_countEt2').clear()
        driver.find_element_by_id('com.android.ooch:id/buy_lottery_countEt2').send_keys('21')
        #点击支付
        driver.find_element_by_id('com.android.ooch:id/buy_lottery_hemai_buyBtn').click()
        #确定支付
        driver.find_element_by_id('android:id/button1').click()
        #try:
        #    assert driver.find_element_by_id('android:id/alertTitle')
        #    #log_info(driver.find_element_by_id('android:id/message').text)
        #    driver.find_element_by_id('android:id/button1').click()
        #    #print_erro_picture(driver, 'guess_hemai_error.png')
        #    #log_error('error')
        #except:
        #    pass
            #WebDriverWait(driver, 20).until(lambda x: x.find_element_by_xpath(
            #    '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/'))
            #share_location = driver.find_element_by_xpath(
            #    ' //android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]').location()
            #driver.swipe(int(share_location['x']) + 10, int(share_location['y']) / 2,
            #             int(share_location['x']) + 10, int(share_location['y']) / 2)
    elif by == u'跟单':
        #有bug出不来
        #点击跟单
        driver.find_element_by_id('com.android.ooch:id/buy_lottery_followBtn').click()
        #查看有多少个购买的
        log_info('have ' + str(len(driver.find_elements_by_id('com.android.ooch:id/follow_lottery_nameTv'))))
        #随机点击一个跟单
        random.choice(driver.find_elements_by_id('com.android.ooch:id/follow_lottery_countEt2')).clear()
        random.choice(driver.find_elements_by_id('com.android.ooch:id/follow_lottery_countEt2')).send_keys('31')
        #隐藏键盘
        middle_slipe(driver)
        #点击提交
        driver.find_element_by_id('com.android.ooch:id/buy_lottery_folow_buyBtn').click()
    else:
        #返回到竞猜列表页面
        #driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[1]').click()
        participation_guess(driver, by)
    #time.sleep(2)
    #等待购买成功
    #driver.find_element_by_id('com.android.ooch:id/title_left_image').click()

    #返回到竞猜列表页面
    #driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[1]').click()


def shareto(driver, to):
    '''
    分享到某个页面
    '''
    #分享到qq
    if to == 'qq':
        driver.find_element_by_id('com.android.ooch:id/share_qqbtn').click()
        ##输入qq号
        #driver.find_element_by_xpath(
        #    '//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.EditText[1]').send_keys(
        #    '2980488481')
        ##输入密码
        #driver.find_element_by_id('com.tencent.mobileqq:id/password').send_keys('gongxiujin')
        ##登录
        #driver.find_element_by_id('com.tencent.mobileqq:id/login').click()
        #随机给一个朋友发送
        random.choice(driver.find_elements_by_id('android:id/text1')).click()
        driver.find_element_by_id('com.tencent.mobileqq:id/').click()
        driver.find_element_by_id('com.tencent.mobileqq:id/').click()
    elif to == 'weibo':
        driver.find_element_by_id('com.android.ooch:id/share_sinabtn').click()
        driver.find_element_by_id('com.sina.weibo:id/titleSave').click()

    #share_location = driver.find_element_by_xpath(
    #    ' //android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]').location()
    #driver.swipe(int(share_location['x']) / 2, int(share_location['y']) / 2,
    #             int(share_location['x']) / 2, int(share_location['y']) / 2)


def search_guess(driver, guess_title):
    #点击搜索按钮
    driver.find_element_by_id('com.android.ooch:id/title_right_image').click()
    #输入搜索内容
    driver.find_element_by_id('com.android.ooch:id/gossip_search_et').send_keys(guess_title)
    #点击搜索按钮
    driver.find_element_by_id('com.android.ooch:id/gossip_search_ib').click()
    #点击竞猜列
    driver.find_element_by_id('com.android.ooch:id/result_lotteries_tv').click()
    #返回到我的竞猜列表页面
    #driver.find_element_by_id('com.android.ooch:id/gossip_search_back_ib').click()






