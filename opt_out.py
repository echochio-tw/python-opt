#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox  # 弹窗
import sys
import os
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
TOTP = str(0) + str(DynamicPasswd) if len(DynamicPasswd) < 6 else DynamicPasswd

window = tk.Tk()
window.title("OTP")
dout = "OTP code : "+TOTP
lb = tk.Label(window, text=dout)
lb.grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
number = tk.StringVar()
tk.Button(window, text='退出', width=10, command=window.quit).grid(row=3, column=1, sticky=tk.E, padx=10, pady=5)
tk.mainloop()
