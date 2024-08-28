# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 14:05:55 2024

@author: AT
"""
a = float(input("Nhap he so a: "))
b = float(input("Nhap he so b: "))

if a != 0:
    x = -b / a
    print(f"Phuong trinh co nghiem duy nhat: x = {x}")
elif b == 0:
    print("Phuong trinh co vo so nghiem.")
else:
    print("Phuong trinh vo nghiem.")
