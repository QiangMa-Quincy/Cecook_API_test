# -*- coding: utf-8 -*-

#商品同步到scrm-sps> good_base_info表

import json
import requests
import unittest
from common import tokenfile

class commoditySynchronization (unittest.TestCase):
    '''商品同步接口'''

    def setUp(self):
        self.url = ' https://api.cecook.net/v1/scrm/standard/commoditySynchronization'
        self.headers = {"authorization": tokenfile.token,'Content-Type': 'application/json'}

    def test_commoditySynchronization_ok(self):
        payload ={"cid": "31","brandName": "品牌名词-test药","categoryName": "所属品类-药品",
        "goodsName": "商品名称",
	    "goodsDesc": "感冒药",
	    "specifications": "规格",
        "weight": "50g",
	    "price": "100",
	    "goodsNumber": "123456",
	    "company": "66666",
	    "barCode": "34557868956",
        "packingSpecifications":"包装规格",
        "productionCompany":"test"}

        r = requests.post(url=self.url, headers = self.headers, data= json.dumps(payload))
        result = r.json()
        print(result)
        self.assertEqual(result['message'], '请求成功')

if __name__ == '__main__':
    unittest.main