# -*- coding: utf-8 -*-

import requests
import unittest

url_test = 'http://node.cecook.net/vir/staff'  #测试环境
url_dev = 'http://smzy.cecook.cn/vir/staff'  #开发环境

url1= url_test+ '/setting/page?cid=1'       #获取登录页面配置

print("url1:", url1)
r= requests.get(url1)
print(r.text)