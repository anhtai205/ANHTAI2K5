# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 14:18:53 2024

@author: AT
"""
def kttg(gio, phut, giay):
    if 0 <= gio < 24 and 0 <= phut < 60 and 0 <= giay < 60:
        return "Thoi gian hop le."
    else:
        return "Thoi gian khong hop le."
gio = int(input("Nhap gio (0-23): "))
phut = int(input("Nhap phut (0-59): "))
giay = int(input("Nhap giay (0-59): "))
kq = kttg(gio, phut, giay)
print(kq)
