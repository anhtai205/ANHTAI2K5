# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:47:53 2024

@author: AT
"""
a = float(input("nhập a:"))
b = float(input("nhập b:"))
c = float(input("nhập c:"))
max_val = a
if b > a:
    max_val = b
if c > a:
    max_val = c
print(f"Số lớn nhất: {max_val}")

