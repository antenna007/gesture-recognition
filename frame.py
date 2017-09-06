#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 17:34:41 2017

@author: marr3
"""

import numpy as np
import cv2
import pyttsx
from scipy import misc

cap = cv2.VideoCapture(0)

count=0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frameRGB = frame #cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv2.imshow('frame',gray)
    misc.imsave('results/outfile'+str(count)+'.png', gray)
    count+=1
    if cv2.waitKey(1) & 0xFF == ord('c'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
