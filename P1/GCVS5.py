#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 20:49:10 2019

@author: constanzamunoz
"""

import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
from collections import Counter


constelaciones = []
Sgr_type = []
Cae_type = []

file = open("GCVS5.txt","r")

for object in file:
    const = object[0] + object[1]
    constelaciones.append(const)
    if const == str(72):
        type = (object[41]+ object[42]+ object[43]+ object[44]+ object[45])
        Sgr_type.append(type)
    if const == str(10):
        type = (object[41]+ object[42]+ object[43]+ object[44]+ object[45])
        Cae_type.append(type)
    
        
#print(Counter(constelaciones).most_common())
#print(Counter(Sgr_type).most_common())
Sgr_sorted = Counter(Sgr_type).most_common()
Cae_sorted = Counter(Cae_type).most_common()

types = ["Eruptive", "Pulsating", "Rotating", "Cataclysmic", "Eclipsing", "X-Ray", "Other"]
eruptive  = ["BE   ", "FU   ", "GCAS ", "I    ", "IA   ",
             "IB   ", "IN   ", "INA  ", "INB  ", "INT  ",
             "IT   ", "IN(YY", "IS   ", "ISA  ", "ISB  ",
             "RCB  ", "RS   ", "SDOR ", "UV   ", "UVN  ", "WR   "]
pulsating = ["ACYG ", "BCEP ", "BCEPS", "BLBOO", "CEP  ", "CEP(B",
             "CW   ", "CWA  ", "CWB  ", "DCEP ", "DCEPS", "DSCT ", 
             "DSCTC", "GDOR ", "L    ", "LB   ", "LC   ", "LPB  ", 
             "M    ", "PVTEL", "RPHS ", "RR   ", "RR(B)", "RRAB ",
             "RRC  ", "RV   ", "RVA  ", "RVB  ", "SR   ", "SRA  ",
             "SRB  ", "SRC  ", "SRD  ", "SRS  ", "SXPHE", "ZZ   ",
             "ZZA  ", "ZZB  ", "ZZO  "]
rotating = [ "ACV  ", "ACVO ", "BY   ", "ELL  ", "FKCOM", "PSR  ", 
             "R    ", "SXARI"]
cataclys = [ "N    ", "NA   ", "NB   ", "NC   ", "NL   ", "NR   ",
             "SN   ", "SNI  ", "SNII ", "UG   ", "UGSS ", "UGSU ", 
             "UGZ  ", "ZAND "]
eclipsing =[ "E    ", "EA   ", "EB   ", "EP   ", "EW   ", "GS   ",
             "PN   ", "RS   ", "WD   ", "WR   ", "AR   ", "D    ",
             "DM   ", "DS   ", "DW   ", "K    ", "KE   ", "KW   ", 
             "SD   "]
X_rays =   [ "AM   ", "X    ", "XB   ", "XF   ", "XI   ", "XJ   ",
            "XND  ", "XNG  ", "XP   ", "XPR  ", "XPRM ", "XM   "] 
other  =   [ "BLLAC", "CST  ", "GAL  ", "L:   ", "QSO  ", "S    ",
             "*    ", "+    ", ":    "]
Sgr_e = 0
Sgr_p = 0
Sgr_r = 0
Sgr_c = 0
Sgr_ec = 0
Sgr_x = 0
Sgr_o = 0


Cae_e = 0
Cae_p = 0
Cae_r = 0
Cae_c = 0
Cae_ec = 0
Cae_x = 0
Cae_o = 0


for i in Sgr_sorted:
    j = i[0] in eruptive
    if j == True:
        Sgr_e = Sgr_e +  i[1]
    j = i[0] in pulsating
    if j  == True:
        Sgr_p = Sgr_p + i[1]
    j = i[0] in rotating
    if j == True:
        Sgr_r = Sgr_r + i[1]
    j = i[0] in cataclys 
    if j == True:
        Sgr_c = Sgr_c + i[1]
    j = i[0] in eclipsing   
    if j == True:
        Sgr_o = Sgr_ec + i[1]
    j = i[0] in X_rays
    if j == True:
        Sgr_x = Sgr_x + i[1]
    j = i[0] in other
    if j == True or j == False:
        Sgr_o = Sgr_o + i[1]
Sgr = Sgr_e+ Sgr_p+ Sgr_r+ Sgr_c+ Sgr_e+ Sgr_x+ Sgr_o
Sgr_array = np.array([Sgr_e, Sgr_p, Sgr_r, Sgr_c, Sgr_e, Sgr_x, Sgr_o+ len(Sgr_type)-Sgr ])
Sgr_list = [Sgr_e, Sgr_p, Sgr_r, Sgr_c, Sgr_e, Sgr_x, Sgr_o+ len(Sgr_type)-Sgr ]
print("Sgr_p: ", Sgr_array[1])    
print("Sgr_r: ", Sgr_array[2]) 
print("Sgr_c: ", Sgr_array[3]) 
print("Sgr_e: ", Sgr_array[4]) 
print("Sgr_x: ", Sgr_array[5]) 
print("Sgr_o: ", Sgr_array[6])

pl.figure(figsize=(7,7))
x = range(7)
pl.xticks(x, types, rotation=60)
pl.bar(x, Sgr_list, color='Orange', label="Total Object : 5889")
pl.title("Distribution of Variable Stars in Sgr Constellation (GCVS 5.1)")
pl.legend()
pl.savefig("Sgr_GCVS.png")

for i in Cae_sorted:
   j = i[0] in eruptive
   if j == True:
       Cae_e = Cae_e +  i[1]
   j = i[0] in pulsating
   if j  == True:
       Cae_p = Cae_p + i[1]
   j = i[0] in rotating
   if j == True:
       Cae_r = Cae_r + i[1]
   j = i[0] in cataclys 
   if j == True:
       Cae_c = Cae_c + i[1]
   j = i[0] in eclipsing   
   if j == True:
       Cae_o = Cae_ec + i[1]
   j = i[0] in X_rays
   if j == True:
       Cae_x = Cae_x + i[1]
   j = i[0] in other
   if j == True or j == False:
       Cae_o = Cae_o + i[1]

Cae = Cae_e+ Cae_p+ Cae_r+ Cae_c+ Cae_e+ Cae_x+ Cae_o
Cae_array = np.array([Cae_e, Cae_p , Cae_r, Cae_c, Cae_e, Cae_x, Cae_o+ len(Cae_type)-Cae ])
Cae_list = [Cae_e, Cae_p , Cae_r, Cae_c, Cae_e, Cae_x, Cae_o+ len(Cae_type)-Cae ]
print("Cae_e: ", Cae_array[0]) 
print("Cae_p: ", Cae_array[1])    
print("Cae_r: ", Cae_array[2]) 
print("Cae_c: ", Cae_array[3]) 
print("Cae_e: ", Cae_array[4]) 
print("Cae_x: ", Cae_array[5]) 
print("Cae_o: ", Cae_array[6])

pl.figure(figsize=(7,7))
x = range(7)
pl.xticks(x, types, rotation=60)
pl.bar(x, Cae_list, color='Green', label="Total Object : 32")
pl.title("Distribution of Variable Stars in Cae Constellation (GCVS 5.1)")
pl.legend()
pl.savefig("Cae_GCVS.png")
