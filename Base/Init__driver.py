
from appium import webdriver
from Base.Read_data import ret_config_data
#获取驱动
def Init_driver():
    #读取配置文件
    config_data = ret_config_data()
    print('config_data:',config_data)
    desired_caps = config_data['Devices']
    driver = webdriver.Remote(config_data['Remote'], desired_caps)
    return driver

