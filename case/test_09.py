# -*- coding: utf-8 -*-

'''
判断：
1、是否满足最低消费需求
2、优惠卷是否过期或未开始
3、是否满足核销的时间段   （using_time：优惠券使用时间）
4、是否满足参与的门店
核销失败的原因
1、不符合最低消费额 limit_price  Ok
2、此时段不能核销   表：coupon_user_defined_template  ok
3、此门店不参与活动 belong_store_id   ok
4、优惠卷已过期   (失效时间：expiry_date) ok
5、活动还未开始（还没到优惠卷的起始日期） 表：coupon_user_defined_template，字段：start_time  ok
6、标记优惠券是否使用  0表示未使用 1表示已使用：is_used ok
'''

import json
import requests
import unittest 
from common import tokenfile

class standardWriteoff (unittest.TestCase):
    '''优惠券核销接口'''

    def setUp(self):
        self.url = 'https://api.cecook.net/v1/scrm/standard/standardWriteoff'
        self.headers = {"authorization": tokenfile.token,'Content-Type': 'application/json'}

    def test_standardWriteoff_ok(self):
        payload ={
            "consumptionAmount": 1,
            "cid": 31,
            "belongStoreId": 0,
            "belongStoreName": "123",
            "couponCode": '0V01700578314',
            "useTimeType": "",
            "customerName": "",
            "actionUserId": 0
        }
        r = requests.post(url=self.url, headers = self.headers, data= json.dumps(payload))
        result = r.json()
        print(result)
        code = result['status']
        print(code)

        if code == '200':
            return self.assertEqual(result['message'], '核销成功')
        else:
            return self.assertEqual(result['message'], '优惠券已核销')

    def test_standardWriteoff_expired(self):
        payload ={
            "consumptionAmount": 1,
            "cid": 31,
            "belongStoreId": 0,
            "belongStoreName": "123",
            "couponCode": '0V01706663650',  #过期券
            "useTimeType": "",
            "customerName": "",
            "actionUserId": 0
        }
        r = requests.post(url=self.url, headers = self.headers, data= json.dumps(payload))
        result = r.json()
        print(result)
        self.assertEqual(result['status'],'507')
        self.assertEqual(result['message'], '优惠券已失效')

    def test_standardWriteoff_is_used_1(self):
        payload ={
            "consumptionAmount": 0,
            "cid": 31,
            "belongStoreId": 0,
            "belongStoreName": "123",
            "couponCode": '0V01701195561',  #已使用过
            "useTimeType": "",
            "customerName": "",
            "actionUserId": 0
        }
        r = requests.post(url=self.url, headers = self.headers, data= json.dumps(payload))
        result = r.json()
        print(result)
        self.assertEqual(result['status'],'507')
        self.assertEqual(result['message'], '优惠券已核销')



    def test_standardWriteoff_is_used_limit_price(self):
        payload = {
        "consumptionAmount": 1,
        "cid": 31,
        "belongStoreId": 0,
        "belongStoreName": "123",
        "couponCode": '0V01700609266',  # 最低消费100
        "useTimeType": "",
        "customerName": "",
        "actionUserId": 0
        }
        r = requests.post(url=self.url, headers=self.headers, data=json.dumps(payload))
        result = r.json()
        print(result)
        self.assertEqual(result['status'], '507')
        self.assertEqual(result['message'], '您的消费金额不符合优惠券使用条件')

    def test_standardWriteoff_storeId(self):
        payload = {
        "consumptionAmount": 1,
        "cid": 31,
        "belongStoreId": 1,
        "belongStoreName": "123",
        "couponCode": '0V01702736363',
        "useTimeType": "",
        "customerName": "",
        "actionUserId": 0
        }
        r = requests.post(url=self.url, headers=self.headers, data=json.dumps(payload))
        result = r.json()
        print(result)
        self.assertEqual(result['status'], '502')
        self.assertEqual(result['message'], '此门店不参与活动')

    def test_standardWriteoff_not_start(self):
        payload = {
                "consumptionAmount": 1,
                "cid": 31,
                "belongStoreId": 0,
                "belongStoreName": "123",
                "couponCode": '0V01708707354',  # 活动还没开始
                "useTimeType": "",
                "customerName": "",
                "actionUserId": 0
            }
        r = requests.post(url=self.url, headers=self.headers, data=json.dumps(payload))
        result = r.json()
        print(result)
        self.assertEqual(result['status'], '507')
        self.assertEqual(result['message'], '活动未开始')

    def test_standardWriteoff_error_time(self):
        payload = {
                "consumptionAmount": 1,
                "cid": 31,
                "belongStoreId": 0,
                "belongStoreName": "123",
                "couponCode": '0V01708707354',  # 活动还没开始
                "useTimeType": "",
                "customerName": "",
                "actionUserId": 0
            }
        r = requests.post(url=self.url, headers=self.headers, data=json.dumps(payload))
        result = r.json()
        print(result)
        self.assertEqual(result['status'], '507')
        self.assertEqual(result['message'], '当前时段不能核销')

if __name__ == '__main__':
    unittest.main