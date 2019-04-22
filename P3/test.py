#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 01:38:55 2019

@author: constanzamunoz
"""

import numpy as np
import matplotlib.pyplot as plt

espectro = np.loadtxt("times-of-maxima.dat")
t = espectro[:, 0] #[HJD]
d = espectro[:, 1]   #[uncertainty]

plt.figure(figsize=(7,5))
#plt.plot(t, d,'.', color='blue')
plt.xlabel('Time [HJD]')
plt.ylabel('Uncertainty')
#plt.title("Star 1 Photometry ")

t0 = 2442582.4060 #[HJD] initial time
p0 = 0.41986 #[days] period

o_c = np.array([]) 

"""
for i in t:
     a0 = i - t0
     a1 = (i - p0)
     oc = (a1* E) + a0
     o_c= np.append(o_c, oc)
     E= E+1
     
plt.plot(t, o_c,'.', color='blue')
"""

def epoch(k):
    n_ek = int((t[k] - t0)/p0) #number of cycle since t0
    return n_ek
    

def mean_period (t):
    periodo = np.array([])
    tiempos = np.array([])
    p_mean = 0
    i = 0
    n = 0
    while i != (len(t) -2):
        n_e = epoch(i+1) - epoch(i) #number of cycle between epoch i+1 and i
        if n_e == 0:
            pass
        else:
            n = n + 1 
            period = ((t[i+1] - t[i])/n_e)
            periodos = ((t[i+1] - t[i])/n_e)
            periodo = np.append(periodo, period)
            tiempos = np.append(tiempos,t[i+1]- t[i])
            p_mean = period + p_mean
        i = i + 1
    Pm = p_mean / n #mean period
    return Pm, periodo, tiempos
z=0
dp_dt=0
while z< len(mean_period(t)[2]):
    dp = mean_period(t)[1][z+1] -mean_period(t)[1][z]
    dt = ((mean_period(t)[2][z+1] -mean_period(t)[2][z])/365)/1e6
    dp_dt = dp_dt + abs(dp/dt)
    z=z+1
    print(dp/dt)

def period(i, j,t):
    n_e = epoch(j) - epoch(i)
    if n_e != 0:
        period = (t[j] - t[i])/n_e
        return period, n_e
    else:
        return False 
    
"""
j = 0
while j != (len(t) -2):
    if period(j,j+1,t) != False and period(j+1,j+2,t) != False:
        dp  = (period(j,j+1,t)[0] - period(j+1,j+2,t)[0])
        dt = (period(j,j+1,t)[1] + period(j+1,j+2,t)[1])
        pend = dp/dt
        oc = 0.5 *pend*mean_period(t)*(epoch(j)**2)
        o_c = np.append(o_c, oc)
        #print(oc)
    else:
        o_c = np.append(o_c, 0)    
    j = j + 1
 """
j = 1
while j != (len(t) -3):
    if period(j,j+1,t) != False and period(j+1,j+2,t) != False:
        a0 = (-period(j,j+1,t)[1] + period(j+1,j+2,t)[1])
        a1 = (-period(j,j+1,t)[0] + period(j+1,j+2,t)[0])
        oc = a0*epoch(j) + a1
        o_c = np.append(o_c, oc)
        #print(oc)
    else:
        o_c = np.append(o_c, 0)    
    j = j + 1   

   
epoch_array = np.array([])
k = 1
while k != (len(t) -3):
    epoch_array = np.append(epoch_array, epoch(k))
    k = k+1
plt.plot(epoch_array, o_c)
    