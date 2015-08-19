# coding: utf-8
from selenium.webdriver.support.ui import WebDriverWait

from ios.ios_Gossip import random_click
from manager import randomCN, time, slide_up


def guess_view(driver):
    driver.find_element_by_name(u'竞猜').click()


def create_guss(driver):
    '''
    创建竞猜

    '''
    #点击发起竞猜按钮
    driver.find_element_by_name(u'发起竞猜').click()
    #点击竞猜标题输入区
    driver.find_element_by_xpath(
        '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIATextView[1]').click()
    driver.find_element_by_xpath(
        '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIATextView[1]').send_keys(u'自动化测试')
    #点击并输入内容
    driver.find_element_by_xpath(
        '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]/UIATextView[1]').click()
    driver.find_element_by_xpath(
        '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]/UIATextView[1]').send_keys(randomCN(10))
    #循环添加两次答案
    for i in range(2):
        #点击添加答案
        driver.find_element_by_xpath(
            '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableGroup[6]/UIAStaticText[1]').click()
        #弹出框内输入答案
        driver.find_element_by_xpath(
            '//UIAApplication[1]/UIAWindow[3]/UIAAlert[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]/UIATextField[1]').click()
        driver.find_element_by_xpath(
            '//UIAApplication[1]/UIAWindow[3]/UIAAlert[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]/UIATextField[1]').send_keys(
            randomCN(3))
        #点击确定
        driver.find_element_by_name(u'确定').click()
    #选择一个答案
    driver.find_element_by_xpath(
        '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[3]/UIAButton[1]').click()
    #使用相册
    #driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[5]/UIAButton[2]').click()
    #随机选择一个相册
    #random_click(driver, '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/*')[0].click()
    #随机选择一张照片
    #random.choice(driver.find_elements_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIACollectionView[1]/*')).click()
    #选取内容
    #driver.find_element_by_name(u'选取').click()
    #拍照方式
    driver.find_element_by_xpath(
        '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[5]/UIAButton[1]').click()
    #点击取景按钮拍照
    time.sleep(1)
    driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAButton[6]').click()
    #选择照片
    driver.find_element_by_name(u'使用照片').click()
    #向上滑动
    slide_up(driver)
    #选择预计开奖时间
    driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[6]/UIAStaticText[1]').click()
    time.sleep(2)
    #点击确定
    driver.swipe(295, 333, 295, 333)
    #点击并发布
    driver.find_element_by_name('支付并发布').click()
    #等待发布成功并回到竞猜主页面
    WebDriverWait(driver, 20).until(
        lambda x: x.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAStaticText[1]'))


def participation_guess(driver, by):
    '''
    随机选择一个竞猜然后点击进入到竞猜详情页面
    by  购买、合买、跟单
    运行完之后返回到竞猜列表页面
    '''
    #随机选中一个
    random_click(driver, '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/')[0].click()
    #等待竞猜页面加载出来
    WebDriverWait(driver, 20).until(lambda x: x.find_element_by_xpath(
        '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableGroup[2]/UIAStaticText[1]'))
    if by == u'购买':
        #随机选择一个
        driver.find_element_by_xpath(
            '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[4]/UIATextField[1]').click()
        driver.find_element_by_xpath(
            '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[4]/UIATextField[1]').send_keys('3')
        #上划一下
        driver.swipe(100, 145, 100, 120)
        #点击竞猜
        driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIAButton[1]').click()

    elif by == u'合买':
        #点击合买按钮
        driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAButton[1]').click()
        #填写发起的份数
        driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATextField[1]').click()
        driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATextField[1]').send_keys('300')
        #填写认购的份数
        driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATextField[2]').click()
        driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATextField[2]').send_keys('32')
        #上划一下
        driver.swipe(177, 404, 177, 350)
        #点击支付
        driver.find_element_by_name(u'支   付').click()

    elif by == u'跟单':
        #点击跟单
        driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAButton[4]').click()
        if driver.find_elements_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/*'):
            for i in range(1,
                           len(driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/*')) + 1):
            #随机跟单一个
                driver.find_element_by_xpath(
                    '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[' + str(
                        i) + ']/UIATextField[1]').click()
                driver.find_element_by_xpath(
                    '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[' + str(
                        i) + ']/UIATextField[1]').send_keys('3')
        else:
            #返回到竞猜列表页面
            driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[1]').click()
            participation_guess(driver, by)
            #上划一下
        driver.swipe(100, 145, 100, 120)
        #点击支付
        driver.find_element_by_name(u'支   付').click()
        #点击确认购买
    driver.find_element_by_name(u'购买').click()
    #等待购买成功
    driver.find_element_by_name(u'返回').click()

    #返回到竞猜列表页面
    driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[1]').click()







