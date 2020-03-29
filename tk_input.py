import tkinter as tk  
from functools import partial  
   
   
def call_result(label_result, n1):  
    result = (n1.get())
    print (result)
    # here can call auth .....
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
