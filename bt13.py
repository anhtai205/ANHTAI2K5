# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:48:59 2024

@author: AT
"""
ngay, thang, nam = map(int, input().split())
print(f"a1) {ngay}/{thang}/{nam}")
print(f"b1) {ngay}/{thang}/{nam % 100:02d}")
print(f"c1) {nam}/{thang}/{ngay}")
ngay, thang, nam = map(int, input("nhập ngày/tháng/năm:").split('/'))
print(f" {ngay} {thang} {nam}")
ngay, thang, nam = map(int, input("nhập ngày/tháng/năm (2 số cuối):").split('/'))
print(f" {ngay} {thang} {nam}")
ngay, thang, nam = map(int, input("nhập năm/tháng/:").split('/'))
print(f" {ngay} {thang} {nam}")
