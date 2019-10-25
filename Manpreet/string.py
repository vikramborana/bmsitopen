#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 11:27:21 2019

@author: root
"""

string=""
x=open("text.txt","w+")
while True:
    y=input()
    if y == "-1":
        break
    string=string+y
x.write(string)
x.close()    