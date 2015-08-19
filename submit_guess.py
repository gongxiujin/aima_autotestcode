# coding: utf-8
from selenium import webdriver
from manager import log_info, log_error


def find_guess(driver, guess_title):
    for i in driver.find_elements_by_xpath('/html/body/div[1]/div/div[5]/table/tbody/tr[*]/td[1]/div/a'):
        if i.text == guess_title:
            return i.find_element_by_xpath('../../..')


class submit_guess():
    def __init__(self, guess_title, url):
        self.guess_title = guess_title
        self.url = url

    def modify_guess(self):
        save_path = '/Users/lonres/Pictures/resultpic/'
        driver = webdriver.PhantomJS()
        self.accept_next_alert = True
        driver.maximize_window()
        driver.get(self.url)
        driver.find_element_by_xpath('//*[@id="wrap"]/nav/div/div[2]/div/a').click()
        driver.find_element_by_id('login').send_keys('aima')
        driver.find_element_by_id('password').send_keys('aima')
        driver.find_element_by_id('submit').click()
        driver.find_element_by_xpath('//*[@id="wrap"]/div/div[1]/ul/li[2]/a').click()
        driver.find_element_by_xpath('//*[@id="wrap"]/div/div[4]/ul/li[2]/a').click()
        submit_list = find_guess(driver, self.guess_title).find_elements_by_id('submit')
        if len(submit_list) == 4:
            log_info("Guess issued failed, it's issued!!!")
        elif len(submit_list) == 3:
            submit_list[0].click()
        driver.get_screenshot_as_file(save_path+'screen_hires_success.png')
        driver.quit()
