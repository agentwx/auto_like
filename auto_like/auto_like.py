#! /usr/bin/env python


import time

from selenium import webdriver
from selenium.common import exceptions

import settings


class AutoLike:
    def __init__(self):
        ...


    def browserOpen(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()


    def login(self):
        d = self.driver
        d.get('https://weibo.com/login.php')
        try:
            d.find_element_by_id('loginname').send_keys(settings.USERNAME)
            d.find_element_by_xpath('//input[@type="password"]').send_keys(settings.PASSWORD)
        except exceptions.StaleElementReferenceException:
            pass
        d.execute_script('alert("请手动登录");')
        alt = d.switch_to.alert
        time.sleep(2)
        try:
            alt.accept()
        except exceptions.NoAlertPresentException:
            pass

        while True:
            if 'bpfilter="page_frame"' in d.page_source:
                break
            elif 'nguide/interests' in d.current_url:
                d.get('https://weibo.com')
            else:
                time.sleep(0.5)

        print('login successful')


    def clickLike(self, url):
        d = self.driver
        d.get(url)
        while 'class="S_txt1 curr"' not in d.page_source:
            time.sleep(0.5)
        d.find_element_by_link_text('按时间').click()

        while True:
            comments = d.find_elements_by_xpath('//a[@action-type="fl_like"]')
            if len(comments) > 1:
                break
            else:
                time.sleep(0.5)

        for c in comments[1:]:
            c.click()
            time.sleep(1)


    def start(self):
        self.browserOpen()
        self.login()
        for w in settings.URLS:
            self.clickLike(w)


if __name__ == "__main__":
    a = AutoLike()
    a.start()
