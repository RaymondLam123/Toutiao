'''
统一入口页面
'''
from Page.fabuye import fabuye_po
from Page.shouye import shouye_po


class Page:
    def __init__(self,driver):
        self.driver = driver
    #返回首页对象
    def ret_shouye_po(self):
        return shouye_po(self.driver)
    #返回发布页对象
    def ret_fabuye_po(self):
        return fabuye_po(self.driver)
