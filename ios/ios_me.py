# coding: utf-8
import random
import time

from selenium.webdriver.support.ui import WebDriverWait

from manager import random_phonenb, randomCN, log_info, double_return, slide_up, share
from ios.ios_Gossip import random_click, send_daoju


def change_myprofile(driver):
    '''
    更换头像
    '''
    pic_location = driver.find_element_by_xpath(
        '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableGroup[1]/UIAStaticText[1]').location
    pic_size = driver.find_element_by_xpath(
        '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableGroup[1]/UIAStaticText[1]').size
    #点击图片更换头像
    driver.swipe(int(pic_location['x']) + int(pic_size['height']), int(pic_location['y']) + int(pic_size['height'] * 2),
                 int(pic_location['x']) + int(pic_size['height']), int(pic_location['y']) + int(pic_size['height'] * 2))
    #从相册里选择
    driver.find_element_by_xpath(
        '//UIAApplication[1]/UIAWindow[4]/UIAActionSheet[1]/UIACollectionView[1]/UIACollectionCell[2]/UIAButton[1]').click()
    #选择第一个相册
    driver.find_element_by_xpath(
        '//UIAApplication[1]/UIAWindow[1]/UIATableView[2]/UIATableCell[1]/UIAStaticText[1]').click()
    #随机选择一个照片
    random.choice(driver.find_elements_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIACollectionView[1]/*')).click()
    driver.find_element_by_name(u'选取').click()


def change_mysignature(driver):
    '''
    更换签名
    '''
    #点击我的签名
    driver.find_element_by_xpath(
        '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableGroup[1]/UIAStaticText[2]').click()
    #清除签名
    driver.find_element_by_xpath(
        '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIATextView[1]').clear()
    #输入签名内容
    driver.find_element_by_xpath(
        '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIATextView[1]').send_keys(randomCN(20))
    #点击保存
    driver.find_element_by_name(u'保存').click()


def my_look(driver):
    '''
    我的关注页面随机选择一个人查看他的个人资料
    '''
    #点击进入我的关注页面
    driver.find_element_by_xpath(
        '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAButton[1]').click()

    log_info(
        'have ' + str(len(driver.find_elements_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/*'))) + 's ')
    #随机选择一个人
    random_click(driver, '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/')[1].click()
    #获取个人资料
    person = {'name': driver.find_element_by_xpath(
        '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableGroup[1]/UIAStaticText[1]').text,
              'follower': driver.find_element_by_xpath(
                  '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableGroup[1]/UIAStaticText[3]').text[:-3],
              'gender': driver.find_element_by_xpath(
                  '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[4]/UIAStaticText[1]').text[3:],
              'addr': driver.find_element_by_xpath(
                  '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[4]/UIAStaticText[2]').text[3:],
              'birthday': driver.find_element_by_xpath(
                  '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[4]/UIAStaticText[3]').text[3:]
    }
    log_info("His/her profile: name " + person['name'] + ", follower " + person['follower'] + ", gender " + person[
        'gender'] + ", addr " + person['addr'] + ", birthday " + person['birthday'])
    #返回到我的个人资料主页
    for i in range(2):
        driver.find_element_by_name(u'返回').click()


def message(driver):
    '''
    到我的关注页面随机给一个人发送一个私信
    '''
    #点击到我的关注页面
    driver.find_element_by_xpath(
        '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAButton[1]').click()
    #随机点击一个人
    random_click(driver, '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/')[1].click()
    #点击发送私信
    driver.find_element_by_xpath(
        '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAButton[2]').click()
    #点击输入框
    driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATextView[1]').click()
    #输入要发送内容
    driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATextView[1]').send_keys(u'你好')
    driver.find_elements_by_xpath('//UIAApplication[1]/UIAWindow[2]/*/UIAButton')[-3].click()
    #确认最后一条消息是谁发的
    #print driver.find_elements_by_xpath(
    #    '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[*]/*')[-1].location['x']
    #返回上一级
    driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[2]').click()
    for i in range(2):
        driver.find_element_by_name(u'返回').click()


def my_gossip(driver):
    '''
    我的八卦页面，随机查看一个八卦
    '''
    #我的八卦页面
    driver.find_elements_by_xpath(
        '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/*')[1].click()
    #随机选择一个八卦
    random_click(driver, '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/')[0].click()
    #发送道具
    send_daoju(driver)
    #返回到我的主页
    #double_return(driver)


def my_currency(driver):
    '''
    我的趣币页面
    '''
    #点击我的趣币
    driver.find_elements_by_xpath(
        '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/*')[2].click()
    daoju_lo = driver.find_elements_by_xpath(
        '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]/UIAButton[*]')[3].location
    daoju_size = driver.find_elements_by_xpath(
        '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]/UIAButton[*]')[3].size
    for i in range(1, 7):
        driver.find_element_by_xpath(
            '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]/UIAButton[' + str(i) + ']').click()
        #等待确认购买的输入框出来
        WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpth(
            '//UIAApplication[1]/UIAWindow[3]/UIAAlert[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]/UIATextField[1]'),
                                        message="can't find it")
        #点击输入框输入购买多少
        driver.find_element_by_xpath(
            '//UIAApplication[1]/UIAWindow[3]/UIAAlert[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]/UIATextField[1]').click()
        #输入购买数量
        driver.find_element_by_xpath(
            '//UIAApplication[1]/UIAWindow[3]/UIAAlert[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]/UIATextField[1]').send_keys(
            '3')
        #点击购买
        driver.find_element_by_xpath(
            '//UIAApplication[1]/UIAWindow[3]/UIAAlert[1]/UIACollectionView[1]/UIACollectionCell[2]/UIAButton[1]').click()
        if i % 5 == 0:
            #向右滑动一下
            driver.swipe(int(daoju_lo['x']), int(daoju_lo['y']) + 20,
                         int(daoju_lo['x']) - int(daoju_size['width']), int(daoju_lo['y']) + 20)
            #返回到我的个人主页
    driver.find_element_by_name(u'返回').click()


def my_fans(driver):
    '''
    我的粉丝页面随机选择一个人发送私信
    '''
    #点击我的粉丝
    driver.find_elements_by_xpath(
        '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/*')[3].click()
    #随机选择一个人
    random_click(driver, '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/')[1].click()
    #获取个人资料
    person = {'name': driver.find_element_by_xpath(
        '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableGroup[1]/UIAStaticText[1]').text,
              'follower': driver.find_element_by_xpath(
                  '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableGroup[1]/UIAStaticText[3]').text[:-3],
              'gender': driver.find_element_by_xpath(
                  '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[4]/UIAStaticText[1]').text[3:],
              'addr': driver.find_element_by_xpath(
                  '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[4]/UIAStaticText[2]').text[3:],
              'birthday': driver.find_element_by_xpath(
                  '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[4]/UIAStaticText[3]').text[3:]
    }
    log_info("His/her profile: name " + person['name'] + ", follower " + person['follower'] + ", gender " + person[
        'gender'] + ", addr " + person['addr'] + ", birthday " + person['birthday'])
    #点击发送私信
    driver.find_element_by_xpath(
        '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAButton[2]').click()
    #点击输入框
    driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATextView[1]').click()
    #输入要发送内容
    driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATextView[1]').send_keys(u'你好')
    driver.find_elements_by_xpath('//UIAApplication[1]/UIAWindow[2]/*/UIAButton')[-3].click()
    #print driver.find_elements_by_xpath(
    #    '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[*]/*')[-1].location['x']
    #返回上一级
    driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[2]').click()
    #返回到我的个人页面
    for i in range(2):
        driver.find_element_by_name(u'返回').click()


def my_guess(driver):
    '''
    我的竞猜获取竞猜内容
    '''
    #点击我的竞猜按钮
    driver.find_elements_by_xpath(
        '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/*')[4].click()
    while True:
        try:
            #随机点击一个我参与的竞猜
            random_click(driver, '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/')[0].click()
            #向上滑动
            slide_up(driver)
            #选择竞猜一个
            #driver.find_element_by_xpath(
            #    '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[' + str(len(driver.find_elements_by_xpath(
            #        '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[*]'))) + ']/UIATextField[1]').click()
            driver.find_element_by_xpath(
                '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[' + str(
                    len(driver.find_elements_by_xpath(
                        '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[*]'))) + ']/UIATextField[1]').send_keys(
                '3')
            #向上滑动取消竞猜
            driver.swipe(100, 145, 100, 120)
            #点击竞猜
            driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIAButton[1]').click()
            #点击确认购买
            driver.find_element_by_name(u'购买').click()
            break
        except:
            driver.find_element_by_xpath(u'返回').click()
            continue
            #等待购买成功
    time.sleep(3)
    share(driver, to=random.choice([u'朋友圈', u'微信', u'微博']))
    driver.find_element_by_name(u'返回').click()
    #返回上一级
    driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[1]').click()


def my_profile(driver):
    #点击我的资料进入到我的资料修改页面
    driver.find_elements_by_xpath(
        '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/*')[5].click()
    #查看是否有历史头像
    if driver.find_elements_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]/*'):
        log_info('have history picture')
    else:
        log_info('no history picture')
        #修改个人昵称
    driver.find_element_by_xpath(
        '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[3]/UIAStaticText[2]').click()
    #输入修改的个人昵称
    driver.find_element_by_xpath(
        '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIATextField[1]').send_keys(randomCN(3))
    #保存修改
    driver.find_element_by_name(u'保存').click()
    #点击修改个性签名
    #qm = driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[4]').location
    #qm_s = driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[4]').size
    #driver.swipe(int(qm['x']) + (int(qm_s['width']) / 2), int(qm['y']) + (int(qm_s['height']) / 2),
    #             int(qm['x']) + (int(qm_s['width']) / 2), int(qm['y']) + (int(qm_s['height']) / 2))
    #输入个性签名
    #driver.find_element_by_xpath(
    #    '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIATextView[1]').send_keys(randomCN(10))
    #点击保存
    #driver.find_element_by_name(u'保存').click()
    time.sleep(2)
    #随机选择性别
    random.choice(driver.find_elements_by_xpath(
        '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[5]/UIAButton[*]')).click()
    #点击返回
    driver.find_element_by_name(u'返回').click()


def my_message(driver):
    #点击我的趣聊
    driver.find_elements_by_xpath(
        '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/*')[6].click()
    #随机点击一个人
    random_click(driver, '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/')[1].click()
    #点击输入框
    driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATextView[1]').click()
    #输入要发送内容
    driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATextView[1]').send_keys(u'你好')
    driver.find_elements_by_xpath('//UIAApplication[1]/UIAWindow[2]/*/UIAButton')[-3].click()
    #返回上一级
    driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[2]').click()
    #返回我的个人主页
    driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[2]').click()


def my_collect(driver):
    #点击我的收藏
    driver.find_elements_by_xpath(
        '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/*')[7].click()
    #随机选择一个八卦
    random_click(driver, '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/')[0].click()
    #发送道具
    send_daoju(driver)
    #返回到我的主页
    double_return(driver)


def is_loged(wd):
    '''
    如果已经登录了退出
    '''

    #如果已经登录了
    if wd.find_element_by_xpath(
            '//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAStaticText[1]').text == u'个人主页':
        #点击个人设置
        wd.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[2]').click()
        #退出当前账户
        wd.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[4]').click()
        #弹出框确认退出？
        if wd.find_element_by_xpath(
                '//UIAApplication[1]/UIAWindow[4]/UIAAlert[1]/UIAScrollView[1]/UIAStaticText[2]').text == u'确定要退出?':
            #点击确认
            wd.find_element_by_xpath(
                '//UIAApplication[1]/UIAWindow[4]/UIAAlert[1]/UIACollectionView[1]/UIACollectionCell[2]/UIAButton[1]').click()
        else:
            #否则取消
            wd.find_element_by_xpath(
                '//UIAApplication[1]/UIAWindow[4]/UIAAlert[1]/UIACollectionView[1]/UIACollectionCell[1]/UIAButton[1]').click()
        WebDriverWait(wd, 10).until(lambda x: x.find_element_by_name(u'登录'))

    else:
        pass


def resgister(wd, resgister_name, resgister_pwd):
    '''
    注册
    '''
    #判断是否登录，如果登录了就退出
    is_loged(wd)
    #点击注册按钮
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[5]").click()
    #输入注册的用户名
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[1]").send_keys(resgister_name)
    #输入注册的密码
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIASecureTextField[1]").send_keys(resgister_pwd)
    #确认密码
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIASecureTextField[2]").send_keys(resgister_pwd)
    #输入验证码
    wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[2]").send_keys("1234")
    #输入随机的电话号码
    wd.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATextField[4]').send_keys(random_phonenb())
    #输入随机的4邮箱
    #wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[3]").send_keys(randomStr(4) + "@qq.com")
    #提交注册表单
    wd.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAButton[3]').click()


def login(wd, login_name, login_pw):
    '''
    登录操作
    '''
    #点击个人页面
    wd.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATabBar[1]/UIAButton[3]').click()
    if wd.find_element_by_xpath(
            '//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAStaticText[1]').text == u'个人主页' and wd.find_element_by_xpath(
            '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableGroup[1]/UIAStaticText[1]').text == login_name:
        pass
    #如果已经登录了，退出登录
    elif wd.find_element_by_xpath(
            '//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAStaticText[1]').text == u'个人主页' and wd.find_element_by_xpath(
            '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableGroup[1]/UIAStaticText[1]').text != login_name:
        is_loged(wd)
    else:
        #如果没有登录点击
        #wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATabBar[1]/UIAButton[3]").click()
        wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[1]").send_keys(login_name)
        wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIASecureTextField[1]").send_keys(login_pw)
        wd.find_element_by_name("登    录").click()
    if wd.find_element_by_xpath(
            '//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAStaticText[1]').text == u'个人主页':
        #返回八卦页面
        wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATabBar[1]/UIAButton[1]").click()
    else:
        resgister(wd, login_name, login_pw)


