# -*- coding: utf-8 -*-

import json
import requests
import unittest
from common import tokenfile

class ajaxCouponListByPhone (unittest.TestCase):
    '''商户优惠券表查询接口'''

    def setUp(self):
        self.url = 'https://api.cecook.net/v1/scrm/standard/couponModelListByCid'
        self.headers = {"authorization": tokenfile.token,'Content-Type': 'application/json'}

    def test_ajaxCouponListByPhone_ok(self):
        payload ={
            "cid": 31
        }
        r = requests.post(url=self.url, headers = self.headers, data= json.dumps(payload))
        result = r.json()
        print(result)
        self.assertEqual(result['status'], '200')

    def test_ajaxCouponListByPhone_Null_cid(self):
        payload ={
            "cid": ''
        }
        r = requests.post(url=self.url, headers = self.headers, data= json.dumps(payload))
        result = r.json()
        print(result)
        self.assertEqual(result['status'], '502')
        self.assertEqual(result['message'],'请求参数出错')

    def test_ajaxCouponListByPhone_all_data(self):
        payload ={
            	"cid":31,
	            "startTime":"2017-02-01",
	            "endTime":"2018-09-03",
	            "index":"1",        # 当数据不足分页时，返回'message': '分页数据返回为空', 'status': '300'
	            "size":"10",
	            "isExpired":"",
                "type":"",
                "status":"1"
        }
        r = requests.post(url=self.url, headers = self.headers, data= json.dumps(payload))
        result = r.json()
        print(result)
        self.assertEqual(result['status'], '200')
        self.assertEqual(result['message'],'成功')

if __name__ == '__main__':
    unittest.main