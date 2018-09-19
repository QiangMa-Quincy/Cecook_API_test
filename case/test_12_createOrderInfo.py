# -*- coding: utf-8 -*-

import json
import requests
import unittest
from common import tokenfile

class createOrderInfo (unittest.TestCase):
    '''订单写入接口'''

    def setUp(self):
        self.url = ' https://api.cecook.net/v1/scrm/standard/createOrderInfo'
        self.headers = {"authorization": tokenfile.token,'Content-Type': 'application/json'}

    def test_createOrderInfo_ok(self):
        payload ={
  "cid": 1,
  "orderNumber": 22221,
  "tradePrice":100,
  "tradeTime":"2018-09-05",
  "storeId": 11,
  "consumerPhone": 13641250842,
  "payType": 1,
  "status": 0,
  "payPrice": 10000,
  "pay_time": "2018-09-05",
  "orderDetail":{"goodsName":"mashao","purchaseQuantity":10}
}
        '''
                payload ={
	"cid": 31,
	"orderNumber": "", #订单编号
	"tradePrice": "", #订单金额（单位分）
	"tradeTime": "",    #交易时间
	"storeId": 0,       #门店ID
	"consumerPhone": "",        #消费者/会员电话
	"payType": "",      #支付方式
	"status": "",       #订单状态:0未处理交易1已处理交易2取消交易
	"payPrice": 0,      #支付金额（单位分）
	"payTime": "",         #支付时间
	"belongStoreId": 0,
	"orderDetail": {
		"goodsName": "",        #商品名称
		"unitPrice": "",        #单价
		"purchaseQuantity": 0       #购买数量
	    }
}
        '''
        r = requests.post(url=self.url, headers = self.headers, data= json.dumps(payload))
        result = r.json()
        print(result)
        code = result['status']
        print(code)

        if code == '200':
            return self.assertEqual(result['message'], '请求成功，订单已同步')
        else:
            return self.assertEqual(result['message'], '请求参数错误，改客户已存在此订单，订单异常')

