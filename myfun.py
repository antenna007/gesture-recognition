#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 23:58:10 2017

@author: marr3
"""
x = 1
y = 2 
z = 3

def f(x=0,y=0,z=0):
    out = x**2 + y**2 + z**2
    return out

print "f=", f(x,y,z)

print "f=",f(x,y)

print "f=", f(y=y,z=z)

print "f=", f(y=x,z=y), f(0,1,2),f(y=1,z=2)


