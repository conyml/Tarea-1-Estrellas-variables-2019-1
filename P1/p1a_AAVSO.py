#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 00:52:25 2019

@author: constanzamunoz
"""

import numpy as np
import pandas as pd
from collections import Counter
import pylab as pl

UV = "AAVSO_UV.csv"
RR = "AAVSO_RR.csv"
SXARI = "AAVSO_SXARI.csv"
N = "AAVSO_N.csv"
E = "AAVSO_E.csv"

subclasses = [UV, RR, SXARI, N, E]
sub_classes = ["UV", "RR", "SXARI", "N", "E"]
constelaciones = []
N_obj = []
for elemento in subclasses:
    file = pd.read_csv(elemento)
    N_obj.append(len(file))
    print("Number of objects in "+elemento +": ",len(file))
#print(Counter(constelaciones).most_common())

total = N_obj[0]+ N_obj[1]+ N_obj[2]+ N_obj[3]+ N_obj[4]
pl.figure(figsize=(5,4.5))
x = range(5)
pl.xticks(x, sub_classes, rotation=60)
pl.bar(x, N_obj, color='c', label="Total Object : "+str(total))
pl.title("Variable type object (VSX)")
pl.legend()
pl.savefig("Var_type_AAVSO.png")

