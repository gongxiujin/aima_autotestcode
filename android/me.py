# coding: utf-8
from manager import *
from Gossip import *


def welcome(driver):
    '''
    当app启动的时候判断是在哪个页面
    '''
    try:
        time.sleep(0.1)
        #加断言查看是否是跳过页面如果不是则滑动页面登录
        assert driver.find_element_by_id('com.android.ooch:id/main_skipt')
        driver.find_element_by_id('com.android.ooch:id/main_skipt').click()
    except:
        #滑动页面翻页
        for i in range(2):
            driver.swipe(611, 693, 1, 693, duration=1)


def login(driver, name, passwd):
    '''
    登录
    '''
    #判断是否已经登录了
    islogined(driver)
    #输入登录用户名
    driver.find_element_by_id('com.android.ooch:id/edit_id').send_keys(name)
    #输入登录密码
    driver.find_element_by_id('com.android.ooch:id/edit_password').send_keys(passwd)
    #点击登录按钮
    driver.find_element_by_id('com.android.ooch:id/button_login').click()
    try:
        #如果登录失败
        assert driver.find_element_by_id('android:id/alertTitle')
        #打印error日志
        log_error(driver.find_element_by_id('android:id/message').text)
        print driver.find_element_by_id('android:id/message').text
        #点击确定按钮
        driver.find_element_by_id('android:id/button1').click()
    except:
        #如果登录成功了打印成功的日志
        log_info(driver.find_element_by_id('com.android.ooch:id/me_nickname_text').text + u' login sucess')


def islogin(driver):
    #点击个人资料页面
    driver.find_element_by_id('com.android.ooch:id/me_image').click()
    try:
        assert driver.find_element_by_id('com.android.ooch:id/me_nickname_text')
    except:
        login(driver, u'gong', u'123456')


def islogined(driver):
    '''
    判断是否已经登录，如果登录了就退出
    '''
    try:
        #加个断言确定已经登录了
        assert driver.find_element_by_id('com.android.ooch:id/me_nickname_text')
        #点击设置按钮
        driver.find_element_by_id('com.android.ooch:id/title_right_image').click()
        #点击退出按钮
        driver.find_element_by_xpath(
            '//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]').click()
    except:
        pass


def three_login(driver, by):
    '''
    by 通过第三方登录：qq weibo （微信登录作废，太恶心）
    '''
    islogined(driver)
    if by == 'qq':
        #如果是qq登录点击qq登录
        driver.find_element_by_id('com.android.ooch:id/button_qq').click()
        #登录
        driver.find_element_by_id('com.tencent.mobileqq:id/name').click()
        #等待它自动登录成功
        #WebDriverWait(driver, 20).until(lambda x: x.find_element_by_id('com.android.ooch:id/me_nickname_text'))
        time.sleep(3)
    elif by == 'weibo':
        #如果是微博登录，点击微博登录按钮
        driver.find_element_by_id('com.android.ooch:id/button_sina').click()
        driver.find_element_by_id('com.android.ooch:id/button_sina')
        time.sleep(3)
        #确定微博登录
        driver.find_element_by_id('com.sina.weibo:id/bnLogin').click()
    elif by == 'weixin':
        #微信作废
        driver.find_element_by_id('com.android.ooch:id/button_wechat').click()
        WebDriverWait(driver, 20).until(lambda x: x.find_element_by_id('com.android.ooch:id/me_nickname_text'))


def change_mypic(driver):
    '''
    更换头像
    '''
    #点击图片更换头像
    driver.find_element_by_id('com.android.ooch:id/me_frame_image').click()
    #从相册里选择
    driver.find_element_by_id('com.android.ooch:id/item_popupwindows_Photo').click()
    #选择第一个相册
    driver.find_element_by_xpath(
        '//UIAApplication[1]/UIAWindow[1]/UIATableView[2]/UIATableCell[1]/UIAStaticText[1]').click()
    #随机选择一个照片
    random.choice(driver.find_elements_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIACollectionView[1]/*')).click()
    driver.find_element_by_name(u'选取').click()
    time.sleep(2)


def change_mysignature(driver):
    '''
    更换签名
    '''
    #输入签名内容
    driver.find_element_by_id('com.android.ooch:id/me_introduce_text').send_keys(randomStr(5))
    #点击别的地方保存
    driver.find_element_by_id('com.android.ooch:id/me_nickname_text').click()


def my_look_fans(driver, page):
    '''
    我的关注页面随机选择一个人查看他的个人资料
    '''
    if page == 'look':
        #点击进入我的关注页面
        driver.find_element_by_id('com.android.ooch:id/me_first_llayout').click()
    elif page == 'fans':
        #点击进入我的粉丝页面
        driver.find_element_by_id('com.android.ooch:id/me_second_llayout').click()
        #查看关注或被关注了多少个人
    #log_info(
    #    'have ' + str(len(driver.find_elements_by_xpath(
    #        '//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[*]'))) + 's ')
    #随机选择一个人
    random.choice(driver.find_elements_by_xpath(
        '//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[*]')).click()
    time.sleep(1)
    #获取个人资料
    #person = {'name': driver.find_element_by_id('com.android.ooch:id/other_nickname_text').text,
    #          'gender': driver.find_element_by_id('com.android.ooch:id/other_gender_text').text[3:],
    #          'addr': driver.find_element_by_id('com.android.ooch:id/other_district_text').text[3:],
    #          'birthday': driver.find_element_by_xpath('com.android.ooch:id/other_country_text').text[3:]
    #}
    #log_info("His/her profile: name " + person['name'] + ", gender " + person[
    #    'gender'] + ", addr " + person['addr'] + ", birthday " + person['birthday'])
    #给这个粉丝发送私信
    #my_message(driver)
    #返回到我的个人资料主页
    #for i in range(2):
    #    driver.find_element_by_id('com.android.ooch:id/title_left_image').click()


def my_message(driver):
    '''
    到我的关注页面随机给一个人发送一个私信
    '''
    try:
        #看是不是在我的个人主页，如果在就进入到趣聊页面
        #assert driver.find_element_by_id('com.android.ooch:id/me_third_llayout')
        #点击个人资料页面
        #driver.find_element_by_id('com.android.ooch:id/me_image').click()
        driver.find_element_by_id('com.android.ooch:id/me_third_llayout').click()
        #随机选择一个人进入到
        random.choice(driver.find_elements_by_xpath(
            '//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]')).click()
    except:
        #如果不是的话就在我的关注或粉丝页面进入的点击发送私信
        driver.find_element_by_id('com.android.ooch:id/tochat_iv').click()
        #输入要发送内容
    driver.find_element_by_id('com.android.ooch:id/conversation_message_bar_edit').send_keys(randomStr(4))
    #点击发送
    driver.find_element_by_id('com.android.ooch:id/conversation_message_bar_send_btn').click()
    #确认最后一条消息是谁发的
    #print driver.find_elements_by_xpath(
    #    '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[*]/*')[-1].location['x']
    #返回我的粉丝或关注页面
    #driver.find_element_by_id('com.android.ooch:id/title_left_image').click()
    #driver.find_element_by_id('com.android.ooch:id/title_left_image').click()


def my_gossip(driver):
    '''
    我的八卦页面，随机查看一个八卦
    '''
    #我的八卦页面
    driver.find_element_by_id('com.android.ooch:id/me_4_llayout').click()
    #随机选择一个八卦
    random.choice(driver.find_elements_by_id('com.android.ooch:id/lv_gossip_item_content_tv')).click()
    #发送道具
    send_daoju(driver)
    #返回到我的主页
    #driver.find_element_by_id('com.android.ooch:id/title_left_image').click()


def my_currency(driver):
    '''
    我的趣币页面
    '''
    #点击我的趣币
    driver.find_element_by_id('com.android.ooch:id/me_5_llayout').click()
    #daoju_lo = driver.find_elements_by_xpath(
    #    '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]/UIAButton[*]')[3].location
    #daoju_size = driver.find_elements_by_xpath(
    #    '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]/UIAButton[*]')[3].size
    time.sleep(1)
    driver.find_element_by_xpath(
        '//android.view.View[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.view.View[1]/android.view.View[8]/android.widget.Image[3]').click()
    time.sleep(1)
    #等待确认购买的输入框出来
    #WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id(
    #    'android:id/alertTitle'),
    #                                message="can't find it")
    #点击输入框输入购买多少
    driver.find_element_by_id('android:id/custom').send_keys('3')
    #点击购买
    driver.find_element_by_id('android:id/button1').click()
    #返回到我的个人主页
    #driver.find_element_by_xpath('//android.view.View[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.webkit.WebView[1]/android.view.View[1]/android.widget.Button[1]').click()


def my_guess(driver):
    '''
    我的竞猜获取竞猜内容
    '''
    #点击我的竞猜按钮
    driver.find_element_by_id('com.android.ooch:id/me_6_llayout').click()
    while True:
        try:
            #随机点击一个我参与的竞猜
            random.choice(driver.find_elements_by_id('com.android.ooch:id/lv_lottery_item_name_tv')).click()
            break
        except:
            #driver.find_element_by_xpath(u'返回').click()
            continue
            #等待购买成功
    time.sleep(3)
    #share(driver, to=random.choice([u'朋友圈', u'微信', u'微博']))
    #driver.find_element_by_name(u'返回').click()
    #返回上一级
    #driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[1]').click()


def my_profile(driver):
    '''
    修改我的个人资料
    '''
    #点击我的资料进入到我的资料修改页面
    driver.find_element_by_id('com.android.ooch:id/me_9_llayout').click()
    #查看是否有历史头像
    #if driver.find_elements_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]/*'):
    #    log_info('have history picture')
    #else:
    #    log_info('no history picture')
        #点击修改个人昵称
    driver.find_element_by_id('com.android.ooch:id/mydetail_nickname_ctext').click()
    #清除个人昵称
    driver.find_element_by_id('com.android.ooch:id/change_edit').clear()
    #输入修改的个人昵称
    driver.find_element_by_id('com.android.ooch:id/change_edit').send_keys(randomStr(3))
    #保存修改
    driver.find_element_by_id('com.android.ooch:id/ctitle_right_btn').click()
    #点击修改个性签名
    driver.find_element_by_id('com.android.ooch:id/mydetail_sign_ctext').click()
    #清除个性签名
    driver.find_element_by_id('com.android.ooch:id/change_edit').clear()
    #输入个性签名
    driver.find_element_by_id('com.android.ooch:id/change_edit').send_keys(randomStr(5))
    #点击确定
    driver.find_element_by_id('com.android.ooch:id/ctitle_right_btn').click()
    time.sleep(2)
    #点击返回
    #driver.find_element_by_id('com.android.ooch:id/title_left_image').click()


def my_collect(driver):
    '''
    点击我的收藏页面
    '''
    #点击我的收藏
    driver.find_element_by_id('com.android.ooch:id/me_7_llayout').click()
    #随机选择一个八卦
    random.choice(driver.find_elements_by_id('com.android.ooch:id/lv_gossip_item_content_tv')).click()
    #发送道具
    #send_daoju(driver)
    #返回到我的主页
    #double_return(driver)


def resgister(wd, resgister_name, resgister_pwd, method=True):
    '''
    注册
    '''
    #判断是否登录，如果登录了就退出
    islogined(wd)
    #点击注册按钮
    wd.find_element_by_id("com.android.ooch:id/text_register").click()
    #输入注册的用户名
    wd.find_element_by_id("com.android.ooch:id/user_id").send_keys(resgister_name)
    #输入注册的密码
    wd.find_element_by_id("com.android.ooch:id/password").send_keys(resgister_pwd)
    #确认密码
    wd.find_element_by_id("com.android.ooch:id/confirm_pwd").send_keys(resgister_pwd)
    #输入验证码
    wd.find_element_by_id("com.android.ooch:id/identify_code").send_keys("1234")
    #输入随机的电话号码
    wd.find_element_by_id('com.android.ooch:id/ph_num').send_keys(random_phonenb())
    #隐藏键盘
    wd.hide_keyboard()
    #输入随机的4邮箱
    #wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[3]").send_keys(randomStr(4) + "@qq.com")
    #提交注册表单
    wd.find_element_by_id('com.android.ooch:id/submit_btn').click()
    #if method == False:
    #    try:
    #        assert wd.find_element_by_id('android:id/alertTitle').text
    #        if not wd.find_element_by_id('android:id/alertTitle').text == u'错误':
    #            pass
    #        else:
    #            raise Exception('error!!!')
    #    except:
    #        raise Exception('error!!!')
    return resgister_name





