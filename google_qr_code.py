#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Google Authenticator TOTP(Time-Based One-Time Password)

import hmac
import hashlib
import base64
import struct
import time

Secret = 'userechochio' # Secret的不要太長不要超過32

Secret = base64.b32encode(s=Secret.encode('utf-8'))
K = base64.b32decode(Secret,True)

C = struct.pack(">Q", int(time.time()) // 30)   # 30 秒後失效

H = hmac.new(K,C,hashlib.sha1).digest() # 使用hmac sha1加密
O = H[19] & 15  # bin(15)=00001111=0b1111

DynamicPasswd = str((struct.unpack(">I", H[O:O+4])[0] & 0x7fffffff) % 1000000)

TOTP = str(0) + str(DynamicPasswd) if len(DynamicPasswd) < 6 else DynamicPasswd # 得到6位数字 如果是5位则加上首位的0

print(TOTP)

#生成二维码
import pyotp
from qrcode import QRCode
from qrcode import constants

Secret = 'userechochio'
Secret = base64.b32encode(s=Secret.encode('utf-8'))
Content = pyotp.totp.TOTP(Secret).provisioning_uri(name='echochio', issuer_name="Verfiy Code")

qr = QRCode(version=1,error_correction=constants.ERROR_CORRECT_L,box_size=6,border=4,)

qr.add_data(Content)
qr.make(fit=True)
img = qr.make_image()
img.save('./GoogleQR.png')
