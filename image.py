#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 01:23:10 2017

@author: marr3
"""

import numpy as np
import cv2

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

img[45,50] = [255,255,255]
px = img[55,55]

img[100:150, 100:150] = [0,0,255]

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()