# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:07:21 2024

@author: AT
"""
print("============= MENU ============")
print("1. HU TIEU")
print("2. CHAO LONG")
print("3. BANH CANH")
print("4. BUN RIEU")
print("5. PHO BO ")
print("===============================")
lua_chon = int(input("moi lua chon:"))
print("=============================")
print(f"ban da chon: {lua_chon} ")
if lua_chon == 1:
    print("ban chon :hu tieu")
elif lua_chon == 2:
    print("ban chon :chao long")
elif lua_chon == 3:
    print("ban chon :banh canh")
elif lua_chon == 4:
    print(" ban chon :bun rieu")
elif lua_chon == 5:
    print("ban chon :pho bo")
else:
    print("lua chon khong hop le")    
