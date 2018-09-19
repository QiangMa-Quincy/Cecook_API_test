# -*- coding: utf-8 -*-

import requests


url = 'http://api.cecook.net/v1/oauth2/token'
payload =  {
"grant_type":"client_credentials",
 "provision_key":"v1",
"client_id":"T7GGglwMuBJRLseWmMm2P7oBQRe6r96R",
"client_secret":"yo43rsaAhHkdwIhE4rVHWt17Bi7Dmgja",
"authenticated_userid":"scrm_test"
}
r = requests.post(url,data= payload)
result = r.json()
#print(result)
token_typy = result['token_type']
access_token = result ['access_token']    #获取'access_token'的值
token = token_typy+' '+access_token


#token = str('bearer n6XAaXZ7gXGRXhFrL2BmTIyZa8KUcDGq')
print('token:' +token)