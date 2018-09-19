# -*- coding: utf-8 -*-

import json
import requests
import unittest
from common import tokenfile

class fineMemberInfo (unittest.TestCase):
    '''会员查询接口'''

    def setUp(self):
        self.url = 'http://api.cecook.net/v1/scrm/standard/findMemberInfo'
        self.headers = {"authorization": tokenfile.token,'Content-Type': 'application/json'}

    def test_findMemberInfo_ok(self):
        payload ={"cid": 31,"phone": "15652053089"}
        #headers = {"authorization": tokenfile.token}
        r = requests.post(url=self.url,headers =self.headers, data=json.dumps(payload))
        result = r.json()
        print(result)
        self.assertEqual(result['status'], '200')

    def test_findMemberInfo_errroPhone(self):
        payload ={"cid": 31,"phone": "1565205308"}
        #headers = {"authorization": tokenfile.token}
        r = requests.post(url=self.url,headers =self.headers, data=json.dumps(payload))
        result = r.json()
        print(result)
        self.assertEqual(result['status'], '502')
        self.assertEqual(result['message'],'请求参数错误，手机号不正确')

    def test_findMemberInfo_Null_cid(self):
        payload ={"cid":'' ,"phone": ""}
        #headers = {"authorization": tokenfile.token}
        r = requests.post(url=self.url,headers =self.headers, data=json.dumps(payload))
        result = r.json()
        print(result)
        self.assertEqual(result['status'], '502')
        self.assertEqual(result['message'], '请求参数错误，cid不能为空')

    def test_findMemberInfo_Null_phone(self):
        payload ={"cid":31,"phone": ""}
        #headers = {"authorization": tokenfile.token}
        r = requests.post(url=self.url,headers =self.headers, data=json.dumps(payload))
        result = r.json()
        print(result)
        self.assertEqual(result['status'], '502')
        self.assertEqual(result['message'], '请求参数错误，phone不能为空')

if __name__ == '__main__':
    unittest.main

