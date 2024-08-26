# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 17:59:00 2024

@author: AT
"""
w = float(input("nhập cân nặng(kg):"))
h = float(input("nhập chiều cao(m):"))
bmi = w / h ** 2
bmi = round(bmi , 2)
print(f"chỉ số bmi là: {bmi}")
