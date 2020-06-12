#!/usr/bin/python
# -*- coding: utf-8 -*-
import base64
import json
import requests
import time as t
from Crypto.Cipher import AES

key = 'ybbbby2018ybbbby'
iv = 'cisdom2018cisdom'

def add_to_16(s):
    while len(s) % 16 != 0:
        s += '\0'
    return str.encode(s)

def encrypt(params):
    aes = AES.new(str.encode(key), AES.MODE_CBC,str.encode(iv))
    return str(base64.encodebytes(aes.encrypt(add_to_16(params))), encoding='utf8').replace('\n', '')

def decrypt(result):
    aes = AES.new(str.encode(key), AES.MODE_CBC,str.encode(iv))
    return str(aes.decrypt(base64.decodebytes(bytes(result, encoding='utf8'))).rstrip(b'\0').decode("utf8"))

def getWySign():
    time=int(t.time())
    return key + '@' + str(time) + '@qqqqqq@1@1.0.0'
params = {
    'id' : 16,
    'device':3,
    'token':'d75ad0cf991925c0396c91d77fbc45d7',
    'sign':encrypt(getWySign())
}
postData={
    'data':encrypt(json.dumps(params))
}
baseUrl='http://192.168.50.4:8989/public/index.php/wyapi/v1_0_0/'
result=requests.post(baseUrl+'money',data=postData)
print(result.json())