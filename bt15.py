# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:25:18 2024

@author: AT
"""

a = float(input("nhập a:"))
b = float(input("nhập b:"))
A = ((a + b) / (a ** 1/3 + b ** 1/3)) - (a*b) ** 1/3
B = (a ** 1/3 - b ** 1/3) ** 2
ketqua = A - B
print(f" kết quả là: {ketqua}")
