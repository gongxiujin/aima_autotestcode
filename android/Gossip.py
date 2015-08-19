# coding: utf-8
import time, random
from selenium.webdriver.support.ui import WebDriverWait
from manager import *


daoju_dirt = {1: u'泼冷水', 2: u'包子', 3: u'糖果', 4: u'鲜花', 5: u'钻石', 6: u'屎盆子'}
Gossip_in_Gossip = {u'爆料': '2', u'娱评': '3', u'趣事': '4', u'追星': '5'}


def random_daoju(driver, elements):
    '''
    随机选择一个道具赠送
    '''
    #随机赠送一个
    random.choice(elements).click()
    #输入赠送数量
    driver.find_element_by_id('com.android.ooch:id/goods_send_countet').clear()
    driver.find_element_by_id('com.android.ooch:id/goods_send_countet').send_keys('1')
    #点击赠送
    driver.find_element_by_id('com.android.ooch:id/goods_send_btn').click()
    try:
        #判断之前有没有该道具
        assert driver.find_element_by_id('android:id/alertTitle')
        driver.find_element_by_id('android:id/button1').click()
        driver.find_element_by_id('com.android.ooch:id/goods_send_btn').click()
    except:
        pass
    #log_info('buy daoju sucess')


def send_daoju(driver):
    '''
    ::driver 发送当前页面的driver
    在八卦详情页面，赠送道具
    '''
    #点击评论上方的道具
    driver.find_element_by_id('com.android.ooch:id/lv_gossip_detail_flower1_tv').click()
    random_daoju(driver, driver.find_elements_by_xpath(
        '//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[1]/android.widget.LinearLayout[1]/*'))
    #滑动屏幕出现后面两个道具
    #shipen_location = driver.find_element_by_id('com.android.ooch:id/goods_shipen_rlayout').location
    #shipen_size = driver.find_element_by_id('com.android.ooch:id/goods_shipen_rlayout').size
    #driver.swipe(int(shipen_location['x']), int(shipen_location['y']) + int(shipen_size['height']) / 2,
    #             int(shipen_location['x']) - int(shipen_size['width']) * 2,
    #             int(shipen_location['y']) + int(shipen_size['height']) / 2)
    #遍历后面的俩也随机选一个
    #random_daoju(driver, driver.find_elements_by_xpath(
    #    '//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView[1]/android.widget.LinearLayout[1]/*')[
    #                     -2:])
    #退出
    #driver.find_element_by_id('com.android.ooch:id/title_left_image').click()


def gossip_comment(driver, comment=randomStr(7), ):
    '''
    八卦详情页面点击评论
    '''
    #随机打开一个八卦
    random.choice(driver.find_elements_by_id('com.android.ooch:id/lv_gossip_item_content_tv')).click()
    #随机回复一个评论
    #random.choice(driver.find_elements_by_id('com.android.ooch:id/gossip_reply_Tv')).click()
    driver.find_element_by_id('com.android.ooch:id/lv_gossip_detail_comment_ib').click()
    time.sleep(2)
    if comment == u'表情':
        driver.find_element_by_id('com.android.ooch:id/btn_face').click()
        for i in range(3):
            random.choice(driver.find_elements_by_id('com.android.ooch:id/item_iv_face')).click()
    else:
        #八卦详情页面点击评论
        driver.find_element_by_id('com.android.ooch:id/lv_gossip_detail_comment_ib').click()
        #输入评论内容
        driver.find_element_by_id('com.android.ooch:id/et_sendmessage').send_keys(comment)
        #点击发送
    driver.find_element_by_id('com.android.ooch:id/btn_send').click()
    time.sleep(1)
    #发送成功返回主页面
    #driver.find_element_by_id('com.android.ooch:id/title_left_image').click()


def search_gossip(driver, search_string):
    '''
    输入搜索内容到达搜索出结果页面
    '''
    #点击搜索按钮
    driver.find_element_by_id('com.android.ooch:id/gossip_search_btn').click()
    #输入搜索内容
    driver.find_element_by_id('com.android.ooch:id/gossip_search_et').send_keys(
        search_string)
    driver.find_element_by_id('com.android.ooch:id/gossip_search_ib').click()
    #等待搜索的结果的view出来
    time.sleep(2)
    #查找搜索出来的结果
    #log_info("gossip page by " + search_string + " have " + str(
    #    len(driver.find_elements_by_id('com.android.ooch:id/lv_search_gossip_item_content_tv'))))


def share_gossip(driver, to):
    '''
    分享八卦
    to  qq、微博  微信、朋友圈暂不开放
    分享完成之后返回到八卦页面
    '''
    #fenxiang = {u'朋友圈': '1', u'微信': '2', u'微博': '4'}
    phone_size = driver.get_window_size()
    #随机选择一个八卦并点击分享
    random.choice(driver.find_elements_by_id('com.android.ooch:id/lv_gossip_item_repost_ib')).click()
    if to == u'微博':
        #点击分享按钮
        driver.find_element_by_id('com.android.ooch:id/share_sinabtn').click()
        driver.find_element_by_id('com.sina.weibo:id/titleSave').click()
        #点击分享按钮
    elif to == u'qq':
        driver.find_element_by_id('com.android.ooch:id/share_qqbtn').click()
        random.choice(driver.find_elements_by_id('android:id/text1')).click()
        driver.find_element_by_id('com.tencent.mobileqq:id/dialogRightBtn').click()
        driver.find_element_by_id('com.tencent.mobileqq:id/dialogLeftBtn').click()
    #middle_click(driver)


def report(driver):
    '''
    举报八卦
    '''
    #点击右上角下拉框
    driver.find_element_by_id('com.android.ooch:id/title_right_image').click()
    #点击举报按钮
    #driver.


def collect_gossip(driver):
    '''
    收藏八卦
    会先判断当前所在页面的位置，如果在八卦详情页面就直接点收藏
    如果是在八卦主页，随机点一个收藏
    点击完收藏返回到八卦主页
    '''
    try:
        assert driver.find_element_by_id('com.android.ooch:id/title_text')
        driver.find_element_by_id('com.android.ooch:id/lv_gossip_detail_praise_ib').click()
        #driver.find_element_by_id('com.android.ooch:id/title_left_image').click()
    except:
        random.choice(driver.find_elements_by_id('com.android.ooch:id/lv_gossip_item_praise_ib')).click()


def create_gossip(driver, gissip_text=randomStr(5), with_pic=u'yes', biaoqing_mount=2):
    '''
    gissip_text string、'biaoqing'判断要发布的内容，如果不输入就不发布八卦内容
    biaoqing_mount  要发送几个表情
    gissip_type 要发布的八卦的类型，如果不输入则随机选择一种类型发布
    with_pic    是否要发布图片默认是带图片的,如果需要图片则以拍照和从相册选择的方式选择两张照片
    返回到八卦页面
    '''
    #进入到新建八卦页面
    driver.find_element_by_id('com.android.ooch:id/gossip_edit_btn').click()
    #随机选择一种类型八卦
    random.choice(driver.find_elements_by_xpath(
        '//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/*')).click()
    if not gissip_text == u'表情':
        driver.find_element_by_id('com.android.ooch:id/gossip_send_content_et').send_keys(gissip_text)
        #是否是含表情
    elif gissip_text == u'表情':
        #点击表情按钮
        driver.find_element_by_id('com.android.ooch:id/btn_face').click()
        #随机选择一个表情
        driver.find_element_by_id('com.android.ooch:id/btn_face').click()
        for i in range(biaoqing_mount):
            random.choice(driver.find_elements_by_id('com.android.ooch:id/item_iv_face')).click()
    if with_pic == u'yes':
        #选择照片
        driver.find_element_by_id('com.android.ooch:id/item_grid_image').click()
        #从相册中选择方式
        driver.find_element_by_id('com.android.ooch:id/item_popupwindows_Photo').click()
        #随机选择一个相册
        random.choice(driver.find_elements_by_id('com.android.ooch:id/info_layout')).click()
        #随机选择一张图片
        random.choice(driver.find_elements_by_id('com.android.ooch:id/image_selected_bg')).click()
        #选中图片
        driver.find_element_by_id('com.android.ooch:id/finish_btn').click()
        #点击确定发布八卦
    driver.find_element_by_id('com.android.ooch:id/gossip_send_btn').click()


def board_paging_display(driver, xpaths, page={}):
    '''
    判断艺人榜上有的几页内容，每页有多少有记录
    返回艺人总数
    '''
    #如果第一次进入先添加第一页有多少个记录
    if not page:
        page[1] = len(driver.find_elements_by_xpath(xpaths))
        board_paging_display(driver, xpaths, page)
    #不是第一次进入且最后一页和倒数第二页的数量是否相同，如果相同就加载了所有的记录，并返回到八卦页面
    else:
        if len(page) > 1 and page[max(page.keys())] == len(
                driver.find_elements_by_xpath(xpaths)):
            log_info("There's " + str(max(page.keys())) + " pages in board!")
            for i in page:
                log_info('page ' + str(i) + ' : ' + str(page[i]))
            driver.find_element_by_name('返回').click()
        #如果没有全加载出来继续翻页并且递归调用
        else:
            slide_up(driver)
            page[max(page.keys()) + 1] = len(
                driver.find_elements_by_xpath(xpaths))
            board_paging_display(driver, xpaths=xpaths, page=page)
    return page[max(page.keys())]

#def get_board_xpath()

def slide(driver):
    start_location = driver.find_elements_by_xpath(
        '//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/*')[
        -1].location
    start_size = driver.find_elements_by_xpath(
        '//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/*')[
        -1].size
    driver.swipe(start_size['width'] / 2, start_location['y'], start_size['width'] / 2, start_size['height'])


def board(driver, name=''):
    '''
    在八卦页面进入到艺人榜，并搜索name艺人并关注，如果已经关注了不操作
    如果name为空，随机选择一个艺人关注
    '''
    #try:
    #    assert driver.find_element_by_id('com.android.ooch:id/title_text')
    #except:
    #进入到艺人榜页面
    driver.find_element_by_id('com.android.ooch:id/gossip_startlist_tv').click()
    mount_t = len(driver.find_elements_by_id('com.android.ooch:id/lv_star_item_name_tv'))
    if name:
        #查找当前页面有没有叫name的艺人
        if filter(lambda x: x == name,
                  map(lambda x: x.text, driver.find_elements_by_id('com.android.ooch:id/lv_star_item_name_tv'))):
            #遍历整个页面查找这个艺人的名字
            for i in driver.find_elements_by_id('com.android.ooch:id/lv_star_item_name_tv'):
                if i.text == name:
                    #判断签到按钮是否可以点击
                    if driver.find_elements_by_id('com.android.ooch:id/lv_star_item_sign_btn')[
                                (int(i.id) - 5) % mount_t].text == u'签到':
                    #如果可以点击，点击
                        driver.find_elements_by_id('com.android.ooch:id/lv_star_item_sign_btn')[
                            (int(i.id) - 5) % mount_t].click()
                        driver.find_element_by_name('返回').click()
                        break
                    else:
                        #如果不可以点击打印log
                        print i.text
                        log_info(name + ' Have already signed in')
                        break
        #如果没有这个人，而且没有加载出全部数据的话滑动加载出下一页
        else:
            slide(driver)
            board(driver)
    else:
        while True:
            elementr = random.choice(driver.find_elements_by_id('com.android.ooch:id/lv_star_item_name_tv'))
            if driver.find_elements_by_id('com.android.ooch:id/lv_star_item_sign_btn')[
                        (int(elementr.id) - 5) % mount_t].text == u'签到':
                driver.find_elements_by_id('com.android.ooch:id/lv_star_item_sign_btn')[
                    (int(elementr.id) - 5) % mount_t].click()
                #log_info(elementr.text+ u' signed in sucessfully')
                return elementr.text
            if random.choice(range(4)) == 0:
                slide(driver)










