#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 17:08:21 2017

@author: marr3
"""

import cv2
import numpy as np
 
cap = cv2.VideoCapture(0)

while True:
    
    ret, frame = cap.read()
    
    cv2.imshow('frame',frame)
   
    
    if cv2.waitKey(0) & 0xFF == ord('q'):
    
        break
    
    cap.release()
    
    cv2.destroyAllWindows()
    
    