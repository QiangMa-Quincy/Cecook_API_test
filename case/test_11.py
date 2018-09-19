# -*- coding: utf-8 -*-

import json
import requests
import unittest
from common import tokenfile

class ajaxCouponDetailByCode (unittest.TestCase):
    '''优惠券查询接口'''

    def setUp(self):
        self.url = 'https://api.cecook.net/v1/scrm/standard/ajaxCouponDetailByCode'
        self.headers = {"authorization": tokenfile.token,'Content-Type': 'application/json'}

    def test_ajaxCouponDetailByCode_ok(self):
        payload ={"cid": "31","couponCode": "0V01704630015"}
        r = requests.post(url=self.url, headers = self.headers, data= json.dumps(payload))
        result = r.json()
        print(result)
        self.assertEqual(result['status'], '200')
        self.assertEqual(result['data']['couponName'], '大宝贝券')
        self.assertEqual(result['data']['customerPhone'],'15652053089')

    def test_ajaxCouponDetailByCode_error_code(self):
        payload ={"cid": "31","couponCode": "0V0170463001"}
        r = requests.post(url=self.url, headers = self.headers, data= json.dumps(payload))
        result = r.json()
        print(result)
        self.assertEqual(result['status'], '201')
        self.assertEqual(result['message'],'无记录')

    def test_ajaxCouponDetailByCode_Null(self):
        payload ={"cid": "","couponCode": ""}
        r = requests.post(url=self.url, headers = self.headers, data= json.dumps(payload))
        result = r.json()
        print(result)
        self.assertEqual(result['status'], '502')
        self.assertEqual(result['message'],'请求参数出错')

if __name__ == '__main__':
    unittest.main