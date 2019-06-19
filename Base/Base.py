from selenium.webdriver.support.wait import WebDriverWait

from Base.Init__driver import Init_driver


class Base(object):
    def __init__(self,driver):
        self.driver = driver
    #查找元素
    def find_element(self,loc,timeout=20):
        return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element(*loc));
    #点击操作
    def click_element(self,loc):
        self.find_element(loc).click()
    #输入文本
    def send_keys(self,loc,text):
        self.fm=self.find_element(loc)
        self.fm.clear()
        self.fm.send_keys(text)

