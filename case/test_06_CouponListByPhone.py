# -*- coding: utf-8 -*-
'''只做新会员的录入，老会员不支持'''
import json
import requests
import unittest
from common import tokenfile

class ajaxCouponListByPhone (unittest.TestCase):
    '''会员优惠券列表查询'''

    def setUp(self):
        self.url = 'https://api.cecook.net/v1/scrm/standard/ajaxCouponListByPhone'
        self.headers = {"authorization": tokenfile.token,'Content-Type': 'application/json'}

    def test_ajaxCouponListByPhone_ok(self):
        payload ={
            "cid": 31,
            "customerPhone": "15652053089"
        }
        r = requests.post(url=self.url, headers=self.headers, data= json.dumps(payload))
        result = r.json()
        print(result)
        self.assertEqual(result['status'], '200')
        self.assertEqual(result['message'],'成功')
        print(result['data'][0]['couponName'])
        print(result['data'][0]['expire'])
        print(result['data'][0]['couponTemplateId'])
        print(result['data'][0]['customerPhone'])


    def test_ajaxCouponListByPhone_errorPhone(self):
        payload = {
            "cid": 31,
            "customerPhone": "1565205308"
        }
        r = requests.post(url=self.url, headers=self.headers, data=json.dumps(payload))
        result = r.json()
        print(result)
        self.assertEqual(result['status'], '502')  #'message': '分页数据返回为空', 'status': '300'

if __name__ == '__main__':
    unittest.main