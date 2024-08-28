# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 21:57:54 2024

@author: AT
"""
def time_to_seconds(time_str):
    h, m, s = map(int, time_str.split(':'))
    total_seconds = h * 3600 + m * 60 + s
    return total_seconds
time_input = input("nhập thời gian theo định dạng hh:mm:ss:")
seconds = time_to_seconds(time_input)
print(f"tổng số giây là: {seconds}")
    
