import os

import yaml
#读取设备的配置
def ret_config_data():
    file_path = os.getcwd() + os.sep + 'device_config' + '.yaml'
    with open(file_path,'r') as f:
        return yaml.load(f)



