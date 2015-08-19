# coding: utf-8
import time, random
import BeautifulSoup
from PIL import Image
from selenium.webdriver.support.ui import WebDriverWait
import logging, os, traceback


save_path = '/Users/lonres/Pictures/phone_error_picures/'
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='/Users/lonres/Documents/log/log.log',
                    filemode='w')


def randomCN(amount):
    number = u''
    for i in range(amount):
        head = random.randint(0xB0, 0xCF)
        body = random.randint(0xA, 0xF)
        tail = random.randint(2, 0xF)
        val = ( head << 8 ) | (body << 4) | tail
        str = "%x" % val
        try:
            number = number + str.decode('hex').decode('gb2312')
        except UnicodeDecodeError as e:
            number = number + randomCN(1)
    return number


def randomStr(amount):
    lists = range(65, 91) + range(97, 123)
    number = ''
    for i in range(amount):
        number = number + chr(random.choice(lists))
    return number


def random_phonenb():
    return str(random.choice(range(13562773362, 13570000000)))


def random_email():
    adr = ['']


def double_return(driver, tips=2):
    for i in range(tips):
        driver.find_element_by_name(u'返回').click()


def print_error(lists):
    result = []
    for log_l in lists:
        for i in log_l.keys():
            if u'message' == i:
                result.append(log_l[i])
    if u'Login failed.' in result:
        log_error(result.index())


def get_pic_path(picname):
    return '/Users/lonres/Documents/log/results/pic/' + picname + '.png'


def middle_slipe(driver):
    screen_location = driver.get_window_size()
    driver.swipe(int(screen_location['width']) / 2, int(screen_location['height']*2/3),
                 int(screen_location['width']) / 2, int(screen_location['height']/4))


def middle_click(driver):
    screen_location = driver.get_window_size()
    driver.swipe(int(screen_location['width']) / 2, int(screen_location['height']) / 2,
                 int(screen_location['width']) / 2, int(screen_location['height']) / 2)


def f_xpath(driver, xpath):
    return driver.find_element_by_xpath(xpath)


def log_info(*string):
    #logg = BeautifulSoup.BeautifulSoup(string, fromEncoding='utf-8')
    logging.info(string)


def log_error(*string):
    logging.error(traceback.format_exc())
    logging.error(string)
    raise Exception('test fail!!!')


def is_enable(driver, xpaths, index):
    return driver.find_elements_by_xpath(xpaths)[index].is_enabled()


def share(driver, to):
    '''
    分享八卦
    to  朋友圈、微信、微博  暂不开放qq太恶心了
    分享完成之后返回到八卦页面
    '''
    fenxiang = {u'朋友圈': '1', u'微信': '2', u'微博': '4'}
    phone_size = driver.get_window_size()
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


def print_erro_picture(driver, picname):
    if picname[-4:] == '.png':
        driver.get_screenshot_as_file(save_path + picname)
    else:
        driver.get_screenshot_as_file(save_path + picname + '.png')


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


def discern_image(filename, *tuple):
    '''
    :filename   需要处理的图片的完整路径
    :*tuple     需要截取图片的4点矩形
    截取图片
    '''
    #处理截图
    image = Image.open(filename)
    newimage = image.crop(tuple)
    save_path = filename[:filename.rfind('/') + 1] + filename[filename.rfind('/') + 1:filename.rfind('.')] + '_sn.png'
    newimage.save(save_path)
    return save_path


def slide_up(driver):
    screen_img = driver.get_window_size()
    driver.swipe(int(screen_img['x']) / 2, int(screen_img['y']) - 10, int(screen_img['x']) / 2, 10)
    driver.swipe(int(screen_img['x']) / 2, int(screen_img['y']) - 10, int(screen_img['x']) / 2, 10)
    time.sleep(0.1)


