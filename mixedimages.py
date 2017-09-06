#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 13:07:12 2017

@author: marr3
"""

import cv2
import numpy as np

img1 = cv2.imread('ball.png')
img2 = cv2.imread('sunflower.png')

add = img1 + img2



cv2.imshow('add',add)
cv2.waitKey(0)
cv2.destroyAllWindows()