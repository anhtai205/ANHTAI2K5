# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:43:01 2024

@author: AT
"""
a = float(input("nhập a:"))
b = float(input("nhập b:"))
c = float(input("nhập c:"))
d = float(input("nhập d:"))
min_val = a
if b < a:
    min_val = b
if c < a:
    min_val = c
if d < a:
    min_val = d
print(f"Số nhỏ nhất: {min_val}")
