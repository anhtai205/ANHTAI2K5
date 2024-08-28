# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 14:47:34 2024

@author: AT
"""
import math
hinh = input("Nhap hinh (v: vuong, n: chu nhat, t: tron): ")

if hinh == 'v':
    # diện tích và chu vi hình vuông
    canh = float(input("Nhap do dai canh: "))
    chu_vi = 4 * canh
    dien_tich = canh ** 2
    print(f"Ket qua P = {chu_vi} S = {dien_tich}")

elif hinh == 'n':
    # diện tích và chu vi hình chữ nhật
    chieu_rong = float(input("Nhap chieu rong: "))
    chieu_dai = float(input("Nhap chieu dai: "))
    chu_vi = 2 * (chieu_rong + chieu_dai)
    dien_tich = chieu_rong * chieu_dai
    print(f"Ket qua P = {chu_vi} S = {dien_tich}")

elif hinh == 't':
    # diện tích và chu vi hình tròn
    ban_kinh = float(input("Nhap ban kinh: "))
    chu_vi = 2 * math.pi * ban_kinh
    dien_tich = math.pi * ban_kinh ** 2
    print(f"Ket qua P = {chu_vi:.2f} S = {dien_tich:.2f}")

else:
    print("Loai hinh khong hop le.")
