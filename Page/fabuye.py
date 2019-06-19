'''
首页
'''
import time

import Page
from Base.Base import Base


class fabuye_po(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)
    #发布内容
    def send(self,text):
        self.send_keys(Page.input_text.text)
        time.sleep(2)
        self.click_element(Page.send_button)


