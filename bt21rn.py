# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 13:55:11 2024

@author: AT
"""
def doc_so(number):
    chu = ["Khong", "Mot", "Hai", "Ba", "Bon", "Nam", "Sau", "Bay", "Tam", "Chin"]
    return chu[number] if 0 <= number <= 9 else "Khong doc duoc"

so = int(input("Nhap mot so bat ky: "))
print(doc_so(so))
