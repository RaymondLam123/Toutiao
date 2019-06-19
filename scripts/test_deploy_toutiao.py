# -*- coding: utf-8 -*-
#发布头条
import sys, os
sys.path.append(os.getcwd())

import pytest
import time

from Base.Init__driver import Init_driver
from Page.Page import Page

#贼坑，记住已定义要大写
class Test_deploy_toutiao:
    def setup_class(self):
        #获取驱动
        self.driver=Init_driver()
        #获取统一页面入口对象
        self.page=Page(self.driver)
        self.shouye_po=self.page.ret_shouye_po()
        self.fabuye_po=self.page.ret_fabuye_po()

    @pytest.mark.skipif(condition=2 > 1, reason="跳过该函数")
    def test01(self):
        '''
        1、进入【首页】，点击发布
        2、点击发图文按钮
        3、进入，【发布页面】，输入文本（上传图片）
        4、点击发布
        '''
        #点击发布
        self.shouye_po.click_deploy_button()
        #点击发图文按钮
        self.shouye_po.click_send_imageAndtext_button()
        #发布内容
        text='你好，我是诸葛维琪'
        self.fabuye_po.send(text)

    def test02(self):
        '''
        搜索头条，发布头条
        :return:
        '''
        #点击输入框
        self.shouye_po.click_search_input_button()
        #输入搜索内容
        self.shouye_po.send('林峰')
        #点击搜索按钮
        self.shouye_po.click_search_button()
        time.sleep(5)

    def teardown_class(self):
        self.driver.quit()
if __name__ == '__main__':
    
    #pytest.main(['-s', 'test_deploy_toutiao.py'])
    pytest.main("-s --alluredir report test_deploy_toutiao.py")