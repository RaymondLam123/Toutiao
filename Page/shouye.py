'''
首页
'''
import Page
from Base.Base import Base


class shouye_po(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)
    #点击发布
    def click_deploy_button(self):
        self.click_element(Page.deploy_button);
    #点击发图文按钮
    def click_send_imageAndtext_button(self):
        self.click_element(Page.send_imageAndtext_button)
    #点击搜索按钮
    def click_search_input_button(self):
        self.click_element(Page.search_input_button)
    #输入搜索内容
    def send(self,text):
        self.send_keys(Page.search_input_button2, text)
    #点击搜索按钮
    def click_search_button(self):
        self.click_element(Page.search_button)


