import tkinter as tk  
from functools import partial
import sys
import os
import hmac
import hashlib
import base64
import struct
import time

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def get_opt():
    Secret = 'userechochio' # Secret的不要太長不要超過32
    Secret = base64.b32encode(s=Secret.encode('utf-8'))
    K = base64.b32decode(Secret,True)
    C = struct.pack(">Q", int(time.time()) // 30)   # 30 秒後失效
    H = hmac.new(K,C,hashlib.sha1).digest() # 使用hmac sha1加密
    O = H[19] & 15  # bin(15)=00001111=0b1111
    DynamicPasswd = str((struct.unpack(">I", H[O:O+4])[0] & 0x7fffffff) % 1000000)
    TOTP = str(0) + str(DynamicPasswd) if len(DynamicPasswd) < 6 else DynamicPasswd
    return TOTP
   
def call_result(label_result, n1):  
    result = (n1.get())
    code = result
    TOTP = get_opt()
    if (code==TOTP):
        os.system(resource_path('hello.exe')) #這裡的 hello.exe 可換掉成要包裝的 exe
    return
   
root = tk.Tk()  
root.title('OTP')  
input1 = tk.StringVar()  
  
labelNum1 = tk.Label(root, text="輸入認證碼 : ").grid(row=1, column=0)  
labelResult = tk.Label(root)  
labelResult.grid(row=7, column=2) 
entryNum1 = tk.Entry(root, textvariable=input1).grid(row=1, column=2)
call_result = partial(call_result, labelResult, input1)   
tk.Button(root,width=10, text="確認與退出", command=lambda: [f() for f in [call_result, root.quit]]).grid(row=3, column=0)
root.mainloop()
