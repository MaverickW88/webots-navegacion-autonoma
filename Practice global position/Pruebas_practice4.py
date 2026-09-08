# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 21:33:48 2020

@author: Humberto Guzman G
"""

from random import randint, uniform,random
import numpy as np


import random
map=[[0, 1, 0, 1, 0],
     [0, 1, 0, 0, 0],
     [0, 0, 0, 1, 0],
     [1, 0, 0, 0, 0],
     [0, 1, 1, 0, 0]]

print (map)
# print(map[2][1]) #fila, columna


zaf1 = random.randint(0,4)
zaf2 = random.randint(0,4)
print (zaf1,zaf2)
poszaf=(zaf1,zaf2)
zafmap=(map[zaf1][zaf2])
print (zafmap)

if zafmap==0:
  print("ok")
elif zafmap == 1:
  zaf1 = random.randint(0,4)
  zaf2 = random.randint(0,4)
  print (zaf1,zaf2)
  poszaf=(zaf1,zaf2)
  zafmap=(map[zaf1][zaf2])
  print (zafmap)

esm1 = random.randint(0,4)
esm2 = random.randint(0,4)
print(esm1, esm2)
posesm=(esm1,esm2)
esmmap=(map[esm1][esm2])
print (esmmap)

if esmmap==0:
  print("ok")
elif esmmap == 1:
  esm1 = random.randint(0,4)
  esm2 = random.randint(0,4)
  print(esm1, esm2)
  posesm=(esm1,esm2)
  esmmap=(map[esm1][esm2])
  print (esmmap)

rub1 = random.randint(0,4)
rub2 = random.randint(0,4)
print(rub1, rub2)
posrub=(rub1,rub2)
rubmap=(map[rub1][rub2])
print (rubmap)

if rubmap==0:
  print("ok")
elif rubmap == 1:
  rub1 = random.randint(0,4)
  rub2 = random.randint(0,4)
  print(rub1, rub2)
  posrub=(rub1,rub2)
  rubmap=(map[rub1][rub2])
  print (rubmap)  

