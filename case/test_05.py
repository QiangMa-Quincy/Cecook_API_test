# -*- coding: utf-8 -*-
'''只做新会员的录入，老会员不支持'''

import json
import requests
import unittest
from common import tokenfile
from common import mqlmember

class createMember (unittest.TestCase):
    '''写入会员接口'''

    def setUp(self):
        self.url = 'https://api.cecook.net/v1/scrm/standard/createMemberInfo'
        self.headers = {"authorization": tokenfile.token,'Content-Type': 'application/json'}

    def test_createMember_ok(self):
        payload ={
            "cid": 31,
            "name": "12@#$%",
            "phone": "13010000124",
            "storeId": 1024491832178921472
        }
        r = requests.post(url=self.url, headers = self.headers, data= json.dumps(payload))
        result = r.json()
        print(result)
        code = result['status']

        if code=='200':
            return self.assertEqual(result['status'], '200')
        else:
            return self.assertEqual(result['message'],'该会员已存在')
        print(result['data']['name'], mqlmember.lastest_member_name)   #返回的结果与数据库比对

    def test_createMember_errorPhone(self):
        payload ={
            "cid": 31,
            "name": "12345",
            "phone": "1565205308",
            "storeId": 1024491832178921472
        }
        r = requests.post(url=self.url, headers = self.headers, data= json.dumps(payload))
        result = r.json()
        print(result)
        self.assertEqual(result['status'], '502')
        self.assertEqual(result['message'],'请求参数错误，手机号不正确')

    def test_createMember_Null_cid(self):
        payload ={
            "cid": '',
            "name": "",
            "phone": "",
            "storeId": ''
        }
        r = requests.post(url=self.url, headers = self.headers, data= json.dumps(payload))
        result = r.json()
        print(result)
        self.assertEqual(result['status'], '502')
        self.assertEqual(result['message'],'请求参数错误，cid不能为空')

    def test_createMember_Null_name(self):
        payload ={
            "cid": 31,
            "name": "12@#$%",
            "phone": "",
            "storeId": ''
        }
        r = requests.post(url=self.url, headers = self.headers, data= json.dumps(payload))
        result = r.json()
        print(result)
        self.assertEqual(result['status'], '502')
        self.assertEqual(result['message'],'请求参数错误，所属门店id不能为空')

    def test_createMember_Null_storeId(self):
        payload ={
            "cid": 31,
            "name": "12@#$%",
            "phone": "",
            "storeId": ''
        }
        r = requests.post(url=self.url, headers = self.headers, data= json.dumps(payload))
        result = r.json()
        print(result)
        self.assertEqual(result['status'], '502')
        self.assertEqual(result['message'],'请求参数错误，所属门店id不能为空')

    def test_createMember_Null_phone(self):
        payload ={
            "cid": 31,
            "name": "12@#$%",
            "phone": "",
            "storeId": 31123
        }
        r = requests.post(url=self.url, headers = self.headers, data= json.dumps(payload))
        result = r.json()
        print(result)
        self.assertEqual(result['status'], '502')
        self.assertEqual(result['message'],'请求参数错误，手机号不能为空')


if __name__ == '__main__':
    unittest.main