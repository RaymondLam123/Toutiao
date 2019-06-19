from Base.Read_data import ret_config_data
import os
data = ret_config_data()
print(type(data))
print(data)
d=data['Remote']
print(d)