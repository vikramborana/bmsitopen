# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 09:58:44 2019

@author: prakh
"""

print("start")
data=open("str.txt","w+")
x=""
while True:
    y=input()
    x=x+y
    data.write(x)
    
data.close()

