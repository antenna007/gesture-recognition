#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 18:22:18 2017

@author: marr3
"""

import pyttsx

#import random as r
def saySomething(j):
    engine = pyttsx.init()
    string=[["A"]]
    for index in range(0,len(string[j])):
        engine.say(string[j][index])
    engine.runAndWait()
    del engine

