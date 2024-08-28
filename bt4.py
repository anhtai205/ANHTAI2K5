# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 21:43:58 2024

@author: AT
"""
N = int(input(" nhập các số nguyên dương N có 2 chữ số:"))
hang_chuc = N // 10
hang_don_vi = N % 10
tong = hang_chuc + hang_don_vi
print(f"tổng các chữ số N là: {hang_chuc} + {hang_don_vi} = {tong}")
