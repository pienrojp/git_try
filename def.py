#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 21:25:42 2017

@author: panin
"""

def find_max(a,b,c):
    if a>=b:
        if b>=c:
            return "The max number is ", a
        else:
            if a>=c:
                return "The max number is ", a
            else:
                return "The max number is ", c

    else:
        d=b
        b=a
        a=d
        return find_max(a,b,c)
        
      