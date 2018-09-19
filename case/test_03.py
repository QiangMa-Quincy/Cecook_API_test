# -*- coding: utf-8 -*-
'''需要限制第三方应用每天的接口请求次数，每个手机号每天最高更新5次'''

import json
import requests
import unittest
from common import tokenfile

class updateMemberInfo (unittest.TestCase):
    '''会员更新接口'''


    def setUp(self):
        self.url = 'https://api.cecook.net/v1/scrm/standard/updateMemberInfo'
        self.headers = {"authorization": tokenfile.token,'Content-Type': 'application/json'}

    def test_updateMemberInfo_ok(self):
        payload ={
            "cid": 31,
            "phone": "13800138000",
            "qq": 12345
        }
        r = requests.post(url=self.url, headers = self.headers, data= json.dumps(payload))
        result = r.json()
        print(result)
        code = result['status']

        if code == '200':
            return self.assertEqual(result['message'], '请求成功')
        else:
            return self.assertEqual(result['message'], '请求参数错误，会员修改次数已用完5次')

    def test_updateMemberInfo_noMember(self):
        payload ={
            "cid": 31,
            "phone": "13000000012",
            "qq": 12345
        }
        r = requests.post(url=self.url, headers = self.headers, data= json.dumps(payload))
        result = r.json()
        print(result)
        self.assertEqual(result['status'],'502')
        self.assertEqual(result['message'], '该会员不存在')

    def test_updateMemberInfo_errorPhone(self):
        payload ={
            "cid": 31,
            "phone": "1380013800",
            "qq": 12345
        }
        r = requests.post(url=self.url, headers = self.headers, data= json.dumps(payload))
        result = r.json()
        print(result)
        self.assertEqual(result['status'],'502')
        self.assertEqual(result['message'], '请求参数错误，手机号不正确')

if __name__ == '__main__':
    unittest.main
