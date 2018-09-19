# -*- coding: utf-8 -*-

import json
import requests
import unittest
from common import tokenfile

class orderRead (unittest.TestCase):
    '''交易读取接口'''

    def setUp(self):
        self.url = ' https://api.cecook.net/v1/scrm/standard/orderReadInfo'
        self.headers = {"authorization": tokenfile.token,'Content-Type': 'application/json'}

    def test_orderRead_ok(self):
        payload ={
                "cid": 4,
                "createTime": "2018-08-16",
                "pageNum": "2"
            }

        r = requests.post(url=self.url, headers = self.headers, data= json.dumps(payload))
        result = r.json()
        print(result)
        code = result['status']
        print(code)
        self.assertEqual(code,'200')

        if code == '200':
            return self.assertEqual(result['message'], '请求成功')
        else:
            return self.assertEqual(result['message'], '请求成功，无记录')

if __name__ == '__main__':
    unittest.main