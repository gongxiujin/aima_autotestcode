# coding: utf-8
import time, random
from selenium.webdriver.support.ui import WebDriverWait
from manager import log_info, save_path, log_error, print_erro_picture, slide_up, random_phonenb


daoju_dirt = {1: u'泼冷水', 2: u'包子', 3: u'糖果', 4: u'鲜花', 5: u'钻石', 6: u'屎盆子'}
Gossip_in_Gossip = {u'爆料': '2', u'娱评': '3', u'趣事': '4', u'追星': '5'}


def send_daoju(driver):
    '''
    ::driver 发送当前页面的driver
    在八卦详情页面，赠送道具
    '''
    #点击评论上方的道具
    driver.find_element_by_xpath(
        '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAButton[1]').click()
    #总共6种道具 依次点击赠送
    for i in range(1, 7):
        if i % 4 == 0:
            print u'要开始滑了'
            time.sleep(2)
            #往左拉一点
            driver.swipe(246, 384, 90, 384)
            time.sleep(2)
            #选中道具
        driver.find_element_by_xpath(
            '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAButton[' + str(i) + ']').click()
        #点击赠送
        driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAButton[3]').click()
        #判断之前有没有该道具
        if driver.find_element_by_xpath(
                '//UIAApplication[1]/UIAWindow[4]/UIAAlert[1]/UIAScrollView[1]/UIAStaticText[1]') and \
                        driver.find_element_by_xpath(
                                '//UIAApplication[1]/UIAWindow[4]/UIAAlert[1]/UIAScrollView[1]/UIAStaticText[1]').text[
                        -4:] == u'数量不够':
            #如果没有点击确定购买
            driver.find_element_by_xpath(
                '//UIAApplication[1]/UIAWindow[4]/UIAAlert[1]/UIACollectionView[1]/UIACollectionCell[2]').click()
            #等待购买成功
        try:
            WebDriverWait(driver, 10).until(
                lambda x: x.find_element_by_xpath(
                    ' //UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAButton[4]'))
            #log_info(driver.find_element_by_xpath(
            #    '//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAStaticText[1]').text + u'页面' +
            #         daoju_dirt[i] + u'购买成功')
            log_info('buy daoju sucess')
        except:
            #log_error(driver.find_element_by_xpath(
            #    '//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAStaticText[1]').text + u'页面' +
            #          daoju_dirt[i] + u'购买失败')
            log_error('buy daoju error')
            print_erro_picture(driver, save_path=save_path)

    #去除下面显示的道具
    driver.swipe(180, 200, 180, 180)


def gossip_comment(driver, comment):
    '''
    八卦详情页面点击评论
    '''
    #随机打开一个八卦
    random_click(driver, '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIATableView[1]/')[1].click()
    #八卦详情页面点击评论
    driver.find_element_by_xpath(
        '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAButton[7]').click()
    #点击评论输入框
    driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATextView[1]').click()
    #输入评论内容
    driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATextView[1]').send_keys(comment)
    #点击发送
    driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAButton[3]').click()
    #发送成功返回主页面
    driver.find_element_by_name(u'返回').click()


def search_gossip(driver, search_string):
    '''
    输入搜索内容到达搜索出结果页面
    '''
    #点击搜索按钮
    driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[4]').click()
    #输入搜索内容
    driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIATextField[1]').send_keys(
        search_string)
    driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[3]').click()
    #等待搜索的结果的view出来
    WebDriverWait(driver, 10).until(
        lambda x: x.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]'))
    #查找搜索出来的结果
    print len(driver.find_elements_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[*]'))


def random_click(driver, xpath):
    '''
    搜索八卦
    :xpath  需要查找的元素，比如需要查找某个path下所有的UIAButton
    :return 返回随机查找的元素
    '''
    random_num = random.choice(range(1, (len(driver.find_elements_by_xpath(xpath + 'UIATableCell[*]')) + 1)))
    print xpath + 'UIATableCell[' + str(random_num) + ']/'
    return driver.find_elements_by_xpath(xpath + 'UIATableCell[' + str(random_num) + ']/*')


def share_gossip(driver, to):
    '''
    分享八卦
    to  朋友圈、微信、微博  暂不开放qq太恶心了
    分享完成之后返回到八卦页面
    '''
    fenxiang = {u'朋友圈': '1', u'微信': '2', u'微博': '4'}
    phone_size = driver.get_window_size()
    #随机选择一个八卦并点击分享
    random_click(driver, '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIATableView[1]/')[-1].click()
    #获得本应用context
    woqu = driver.current_context
    driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAButton[' + fenxiang[to] + ']').click()
    driver.switch_to.context('NATIVE_APP')
    time.sleep(5)
    if to == u'朋友圈' or to == u'微博':
        #点击分享按钮
        driver.swipe(int(phone_size['width']) * 29 / 32, int(phone_size['height']) * 21 / 284,
                     int(phone_size['width']) * 29 / 32, int(phone_size['height']) * 21 / 284)
    elif to == u'微信':
        #选择一个聊天并发送
        driver.swipe(int(phone_size['width']) * 7 / 32, int(phone_size['height']) * 125 / 284,
                     int(phone_size['width']) * 7 / 32, int(phone_size['height']) * 125 / 284)
        #点击发送
        driver.swipe(int(phone_size['width']) * 203 / 320, int(phone_size['height']) * 91 / 142,
                     int(phone_size['width']) * 203 / 320, int(phone_size['height']) * 91 / 142)
        #点击返回卧趣
        driver.swipe(int(phone_size['width']) * 1 / 2, int(phone_size['height']) * 329 / 568,
                     int(phone_size['width']) * 1 / 2, int(phone_size['height']) * 329 / 568)
    driver.switch_to.context(woqu)
    driver.find_element_by_name(u'返回').click()

def report(driver):
    '''
    举报八卦
    '''
    #点击右上角下拉框
    driver.find_elements_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/*')[-1].click()
    #点击举报按钮
    driver.find_element_by_name(u'举报').click()
    #返回到八卦主页
    driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATextField[1]').click()
    #输入联系人电话
    driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATextField[1]').send_keys(random_phonenb())
    #点击提交
    driver.find_element_by_name(u'提   交')
    #返回八卦主页
    driver.find_element_by_name(u'返回').click()



def collect_gossip(driver, location):
    '''
    收藏八卦
    location  当前页面的位置  main or gossip
    点击玩收藏返回到八卦主页
    '''
    if location == u'main':
        #随机选择一个八卦并点击收藏
        random_click(driver, '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIATableView[1]/')[-3].click()
    elif location == u'gossip':
        driver.find_element_by_xpath(
            '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAButton[5]').click()
        driver.find_element_by_name(u'返回').click()


def create_gossip(driver, gissip_text=None, gissip_type=None, with_pic=u'yes'):
    '''
    gissip_text string、'biaoqing'判断要发布的内容，如果不输入就不发布八卦内容
    gissip_type 要发布的八卦的类型，如果不输入则随机选择一种类型发布
    with_pic    是否要发布图片默认是带图片的,如果需要图片则以拍照和从相册选择的方式选择两张照片
    返回到八卦页面
    '''
    #是否是在发布八卦页面
    #try:
    #    assert driver.find_element_by_name(u'发布八卦')
    #except:
    #    raise Exception('Not in create gossip page!!!!')
        #是否给出了要发布的八卦内容，没有则不发
    if gissip_text != None and gissip_text != u'表情':
        driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATextView[1]').click()
        driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATextView[1]').send_keys(
            gissip_text)
        #划一下关掉评论键盘
        driver.swipe(160, 264, 160, 253)

        #是否是含表情
    elif gissip_text == u'表情':
        #点击输入框
        driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATextView[1]').click()
        #点击表情按钮
        driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAButton[1]').click()
        #点击最近按钮
        driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[2]/UIAButton[1]').click()
        #判断最近里面是否有表情
        if len(driver.find_elements_by_xpath('//UIAApplication[1]/UIAWindow[2]/UIAScrollView[1]/*')) > 1:
            #随机选择一种表情
            random.choice(driver.find_elements_by_xpath('//UIAApplication[1]/UIAWindow[2]/*')[1:]).click()
        else:
            #除了最近的类型
            random.choice(driver.find_elements_by_xpath('//UIAApplication[1]/UIAWindow[2]/UIAButton[*]'[2:])).click()
            #随机选择一个表情
        #random.choice(driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[2]/UIAScrollView[1]/UIAButton[4]'))
        random.choice(driver.find_elements_by_xpath('//UIAApplication[1]/UIAWindow[2]/UIAScrollView[1]/*')).click()
        print u'随机选择一个表情成功'
        #滑动页面选择下一页表情
        driver.swipe(270, 414, 2, 414)
        #在选择一个表情
        random.choice(driver.find_elements_by_xpath('//UIAApplication[1]/UIAWindow[2]/UIAScrollView[1]/*')).click()
        print u'划到下一页后点击成功'
        #划一下关掉表情键盘
        driver.swipe(160, 264, 160, 253)
        #是否给出指定的八卦类型，如果没有随机选择一种类型
    if gissip_type == None:
        gissip_type = random.choice(Gossip_in_Gossip.values())
        driver.find_element_by_xpath(
            '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAButton[' + gissip_type + ']').click()
    else:
        driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAButton[' + Gossip_in_Gossip[
            gissip_type] + ']').click()
    if with_pic == u'yes':
        #选择照片
        driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAButton[1]').click()
        #选择拍照方式
        driver.find_element_by_xpath(
            '//UIAApplication[1]/UIAWindow[4]/UIAActionSheet[1]/UIACollectionView[1]/UIACollectionCell[1]/UIAButton[1]').click()
        #点一下拍照按钮
        driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAButton[6]').click()
        #确定所拍摄的照片
        driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAButton[4]').click()
        #选择照片
        driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAButton[1]').click()
        #从相册中选择方式
        driver.find_element_by_xpath(
            '//UIAApplication[1]/UIAWindow[4]/UIAActionSheet[1]/UIACollectionView[1]/UIACollectionCell[2]/UIAButton[1]').click()
        #随机选择一张图片
        random.choice(driver.find_elements_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIACollectionView[1]/*')).click()
        #确定选中的照片
        driver.find_element_by_name(u'完成').click()
        #选择照片
        driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAButton[1]').click()
        #取消
        driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[4]/UIAActionSheet[1]/UIAButton[1]').click()
        #点击确定发布八卦
    driver.find_element_by_name(u'完成').click()
    #等待发送成功回到八卦列表页面
    #WebDriverWait(driver, 10).until(
    #    lambda x: x.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[2]'))


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


def board(driver, mount=0, name=''):
    '''
    根据人名点击签到未完成
    在八卦页面进入到艺人榜，并搜索name艺人并关注，如果已经关注了则不作任何操作
    如果name为空，随机选择一个艺人关注
    '''
    if mount == 0:
        mount = board_paging_display(driver, '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/./*') * 2
    driver.find_element_by_name("艺人榜").click()
    if name:
        #查找当前页面有没有叫name的艺人
        mount_t = len(driver.find_elements_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/*/UIAStaticText'))
        if filter(lambda x: x == name, map(lambda x: x.text, driver.find_elements_by_xpath(
                '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/*/UIAStaticText'))):
            #遍历整个页面查找这个艺人的名字
            for i in driver.find_elements_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/*/UIAStaticText'):
                if i.text == name:
                    #判断签到按钮是否可以点击
                    if driver.find_elements_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/*/UIAButton')[
                                int(i.id) % mount_t].is_enabled():
                    #如果可以点击，点击
                        print int(driver.find_elements_by_xpath(
                            '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/*/UIAButton')[
                            int(i.id) % mount_t].id) % mount_t
                        driver.find_elements_by_xpath(
                            '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/*/UIAButton')[int(i.id) % mount_t].click()
                        log_info(name + ' Sign in successfully')
                        driver.find_element_by_name('返回').click()
                        break
                    else:
                        #如果不可以点击打印log
                        print driver.find_elements_by_xpath(
                            '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/*/UIAButton')[int(i.id) % mount_t].id
                        print i.text
                        log_info(name + ' Have already signed in')
                        break
        #如果没有这个人，而且没有加载出全部数据的话滑动加载出下一页
        elif not mount_t == mount:
            slide_up(driver)
            board(driver, mount, name)
        else:
            log_info('The board has not been created!!!')
    else:
        #mount = board_paging_display(driver)
        while True:
            mount_t = len(driver.find_elements_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/*/UIAButton'))
            if mount_t == mount:
                break
            else:
                slide_up(driver)
        while True:
            random_element = random.choice(
                driver.find_elements_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/*/UIAButton'))
            try:
                if random_element.text == u'签到':
                    random_element.click()
                    log_info(str((int(random_element.id) % mount) / 2) + "'s  signed in successfully")
                    driver.find_element_by_name('返回').click()
                    break
            except:
                continue









