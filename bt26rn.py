# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 14:26:19 2024

@author: AT
"""

a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))
c = int(input("Nhap so c: "))
nums = [a, b, c]
nums.sort()
print("Cac so theo thu tu tang dan:", nums)
N = input("Nhap mot so nguyen: ")
sorted_digits = ''.join(sorted(N))
print("So sau khi sap xep:", sorted_digits)
