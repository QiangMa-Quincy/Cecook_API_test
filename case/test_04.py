# -*- coding: utf-8 -*-
'''每次调用最高调用此时间往前的10条'''

import json
import requests
import unittest
from common import tokenfile

class getMemberInfo (unittest.TestCase):
    '''会员读取接口'''

    def setUp(self):
        self.url = 'https://api.cecook.net/v1/scrm/standard/findMemberInfoList'
        self.headers = {"authorization": tokenfile.token}

    def test_getMemberInfo_ok(self):
        payload ={
            "cid":31
        }
        r = requests.get(url=self.url, headers=self.headers, params=payload)
        '''get方法传参用params'''
        print(r)
        result = r.json()           #'str' object has no attribute 'items'
        print(result)
        print(result.get('status'))
        print(result.get('data')[0]['name'])
        print(result.get('data')[1]['name'])
        print(result.get('data')[2]['name'])
        print(result.get('data')[3]['name'])
        print(result.get('data')[4]['name'])
        print(result.get('data')[5]['name'])
        print(result.get('data')[6]['name'])
        print(result.get('data')[7]['name'])
        print(result.get('data')[8]['name'])
        print(result.get('data')[9]['name'])
        self.assertEqual(result['status'], '200')

    def test_getMemberInfo_Null(self):
        payload ={
            "cid":''
        }
        r = requests.get(url=self.url, headers=self.headers, params=payload)
        '''get方法传参用params'''
        print(r)
        result = r.json()           #'str' object has no attribute 'items'
        print(result)
        self.assertEqual(result['status'], '502')
        self.assertEqual(result['message'],'请求参数错误，cid不能为空')

if __name__ == '__main__':
    unittest.main
