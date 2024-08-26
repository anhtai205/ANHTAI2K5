# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:10:49 2024

@author: AT
"""
a = input("nhập số xe:")
b = sum(int(c) for c in a)
if b >= 10:
    b = (b // 10) + (b % 10)
print(f"Tổng số nút là: {b}")
