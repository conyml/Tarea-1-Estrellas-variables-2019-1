#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 19:06:55 2019

@author: constanzamunoz
"""
import numpy as np
import pandas as pd
from collections import Counter
import pylab as pl

UV = "GCVS_UV.txt"
RR = "GCVS_RR.txt"
SXARI = "GCVS_SXARI.txt"
N = "GCVS_N.txt"
E = "GCVS_E.txt"

subclasses = [UV, RR, SXARI, N, E]
sub_classes = ["UV", "RR", "SXARI", "N", "E"]
constelaciones = []
N_obj = []
for elemento in subclasses:
    file = pd.read_csv(elemento)
    c = 0
    while c < len(file):
        row = file.iloc[c,0]
        const = (row[6] + row[7] + row[8] +
                row[9])
        const = constelaciones.append(const)
        c = c + 1
    N_obj.append(len(file))
    print("Number of objects in "+elemento +": ",len(file))
#print(Counter(constelaciones).most_common())

total = N_obj[0]+ N_obj[1]+ N_obj[2]+ N_obj[3]+ N_obj[4]
pl.figure(figsize=(5,4.5))
x = range(5)
pl.xticks(x, sub_classes, rotation=60)
pl.bar(x, N_obj, color='Blue', label="Total Object : "+str(total))
pl.title("Variable type object (GCVS 5.1)")
pl.legend()
pl.savefig("Var_type_GCVS.png")

