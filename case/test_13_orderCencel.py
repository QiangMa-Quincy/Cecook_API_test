# -*- coding: utf-8 -*-

import json
import requests
import unittest
from common import tokenfile

class orderCencel (unittest.TestCase):
    '''订单撤销接口'''

    def setUp(self):
        self.url = ' https://api.cecook.net/v1/scrm/standard/orderCencel'
        self.headers = {"authorization": tokenfile.token,'Content-Type': 'application/json'}

    def test_orderCencel_ok(self):
        payload ={
	"orderNumber": "MHX130063703",
	"cid": 4,
	"consumerPhone": "15652053089"
}
        r = requests.post(url=self.url, headers = self.headers, data= json.dumps(payload))
        result = r.json()
        print(result)
        code = result['status']
        print(code)

        if code == '200':
            return self.assertEqual(result['message'], '请求成功，订单取消成功')
        else:
            return self.assertEqual(result['message'], '请求参数错误，订单已取消')

    def test_orderCencel_noOrder(self):
        payload ={
	"orderNumber": "MHX130063703",
	"cid": 31,
	"consumerPhone": "15652053089"
}
        r = requests.post(url=self.url, headers = self.headers, data= json.dumps(payload))
        result = r.json()
        print(result)
        code = result['status']
        print(code)
        #self.assertEqual(code, '502')
        self.assertEqual(result['message'], '请求参数错误，订单不存在')

    def test_orderCencel_error_phone(self):
        payload ={
	"orderNumber": "MHX130063703",
	"cid": 31,
	"consumerPhone": "1565205308"
}
        r = requests.post(url=self.url, headers = self.headers, data= json.dumps(payload))
        result = r.json()
        print(result)
        code = result['status']
        print(code)
        self.assertEqual(code, '502')
        self.assertEqual(result['message'], '请求参数错误，手机号不正确')

    def test_orderCencel_Null(self):
        payload ={
	"orderNumber": "",
	"cid": '',
	"consumerPhone": ""
}
        r = requests.post(url=self.url, headers = self.headers, data= json.dumps(payload))
        result = r.json()
        print(result)
        code = result['status']
        print(code)
        self.assertEqual(code, '502')
        self.assertEqual(result['message'], '请求参数错误，cid不能为空')


if __name__ == '__main__':
    unittest.main