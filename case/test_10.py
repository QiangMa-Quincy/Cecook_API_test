# -*- coding: utf-8 -*-

#反核销记录表  coupon_reverse_record

import json
import requests
import unittest
from common import tokenfile

class standardReverseWriteoff (unittest.TestCase):
    '''优惠券反核销接口'''

    def setUp(self):
        self.url = 'https://api.cecook.net/v1/scrm/standard/standardReverseWriteoff'
        self.headers = {"authorization": tokenfile.token,'Content-Type': 'application/json'}

    def test_standardReverseWriteoff_ok(self):
        payload ={
	"cid": "31",
	"couponCode": "0V01700578314"
}
        r = requests.post(url=self.url, headers = self.headers, data= json.dumps(payload))
        result = r.json()
        print(result)
        self.assertEqual(result['status'], '200')
        self.assertEqual(result['message'],'反核销成功')

    def test_standardReverseWriteoff_error_code(self):
        payload ={
	"cid": "31",
	"couponCode": "0V0170060926"
}
        r = requests.post(url=self.url, headers = self.headers, data= json.dumps(payload))
        result = r.json()
        print(result)
        self.assertEqual(result['status'], '502')
        self.assertEqual(result['message'],'优惠券不存在')

    def test_standardReverseWriteoff_Null(self):
        payload ={
	"cid": "",
	"couponCode": ""
}
        r = requests.post(url=self.url, headers = self.headers, data= json.dumps(payload))
        result = r.json()
        print(result)
        self.assertEqual(result['status'], '502')
        self.assertEqual(result['message'],'参数请求错误')

if __name__ == '__main__':
    unittest.main