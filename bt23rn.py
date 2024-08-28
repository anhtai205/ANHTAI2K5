# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 14:09:58 2024

@author: AT
"""
import math

def giai_phuong_trinh_bac_hai(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "Phuong trinh co vo so nghiem."
            else:
                return "Phuong trinh vo nghiem."
        else:
            x = -c / b
            return f"Phuong trinh co nghiem duy nhat: x = {x}"
    else:
        delta = b**2 - 4*a*c
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            return f"Phuong trinh co  nghiem phan biet: x1 = {x1}, x2 = {x2}"
        elif delta == 0:
            x = -b / (2*a)
            return f"Phuong trinh co nghiem kep: x = {x}"
        else:
            return "Phuong trinh vo nghiem."
a = float(input("Nhap he so a: "))
b = float(input("Nhap he so b: "))
c = float(input("Nhap he so c: "))
ket_qua = giai_phuong_trinh_bac_hai(a, b, c)
print(ket_qua)
