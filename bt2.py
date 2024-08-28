# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 21:23:38 2024

@author: PC
"""
a = int(input("nhập số a:"))
b = int(input("nhập số b:"))
tong = a + b
hieu = a - b
tich = a * b
thuong_2 = round(a / b, 2)
thuong_3 = round(a / b, 3)
print(f" tổng của {a} và {b} là: {tong}")
print(f" hiệu của {a} và {b} là: {hieu}")
print(f" tich của {a} và {b} là: {tich}")
print(f" thương của {a} và {b} làm tròn 2 chữ số sau dấu chấm là: {thuong_2} ")
print(f" thương của {a} và {b} làm tròn  chữ số sau dấu chấm là: {thuong_3} ")