#! /usr/bin/env python


import time
from itertools import cycle

from selenium.common import exceptions

import settings
from auto_like import AutoLike


class Hufen:
    def __init__(self):
        self.al = AutoLike()
        self.content = settings.CONTENT


    def sendContent(self, url):
        d = self.driver
        d.get(url)
        try:
            d.find_element_by_xpath('//textarea').send_keys(self.content)
            time.sleep(2)
            d.find_element_by_xpath('//a[@node-type="submit"]').click()
        except Exception:
            time.sleep(10)
            self.sendContent(url)
        return self


    def start(self):
        self.driver = self.al.browserOpen().driver
        self.al.login(self.driver)
        for groupurl in cycle(settings.CHATGROUPURLS):
            self.sendContent(groupurl)
            time.sleep(5)


if __name__ == "__main__":
    a = Hufen()
    a.start()
