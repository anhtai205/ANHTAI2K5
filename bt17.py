# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:32:58 2024

@author: AT
"""
def find_min_max(a, b, c):
    return min(a, b, c), max(a, b, c)
a = float(input("nhập a:"))
b = float(input("nhập b:"))
c = float(input("nhập c:"))
min_val, max_val = find_min_max(a, b, c)
print(f"Số nhỏ nhất: {min_val}, Số lớn nhất: {max_val}")