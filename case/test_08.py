# -*- coding: utf-8 -*-

import json
import requests
import unittest
from common import tokenfile

class handleCoupon (unittest.TestCase):
    '''优惠券生成接口'''

    def setUp(self):
        self.url = 'https://api.cecook.net/v1/scrm/standard/handleCoupon'
        self.headers = {"authorization": tokenfile.token,'Content-Type': 'application/json'}

    def test_handleCoupon_ok(self):
        payload ={	"id":"1021309314416250880",  #查询优惠券模板id：coupon_user_defined_template
                      "cid":"31","customers":{"15652053089":"zhangsan"}}
        r = requests.post(url=self.url, headers = self.headers, data= json.dumps(payload))
        result = r.json()
        print(result)
        couponCode= result['data'][0]['couponCode']
        self.assertEqual(result['status'], '200')
        print(result['data'][0]['couponName'])     #模板id对应：大宝贝券
        self.assertEqual(result['data'][0]['couponName'],'大宝贝券')
        print(couponCode)      #打印coupon code

    def test_handleCoupon_errorPhone(self):
        payload ={	"id":"1021309314416250880",  #查询优惠券模板id：coupon_user_defined_template
                      "cid":"31","customers":{"1565205308":"zhangsan"}}
        r = requests.post(url=self.url, headers = self.headers, data= json.dumps(payload))
        result = r.json()
        print(result)
        self.assertEqual(result['status'], '502')
        self.assertEqual(result['message'],'手机号格式不正确')

    def test_handleCoupon_error_id(self):
        payload ={	"id":"102130931441625088",  #查询优惠券模板id：coupon_user_defined_template
                      "cid":"31","customers":{"15652053089":"zhangsan"}}
        r = requests.post(url=self.url, headers = self.headers, data= json.dumps(payload))
        result = r.json()
        print(result)
        self.assertEqual(result['status'], '503')
        self.assertEqual(result['message'],'模板不存在')

    def test_handleCoupon_error_cid(self):
        payload ={	"id":"1021309314416250880",  #查询优惠券模板id：coupon_user_defined_template
                      "cid":"1","customers":{"15652053089":"zhangsan"}}
        r = requests.post(url=self.url, headers = self.headers, data= json.dumps(payload))
        result = r.json()
        print(result)
        self.assertEqual(result['status'], '503')
        self.assertEqual(result['message'],'模板不存在')

if __name__ == '__main__':
    unittest.main