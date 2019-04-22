#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 12:54:56 2019

@author: constanzamunoz
"""

import numpy as np
import matplotlib.pyplot as plt

espectro = np.loadtxt("times-of-maxima.dat")
t = espectro[:, 0] #[HJD]
inc = espectro[:, 1]   #[uncertainty]

plt.figure(figsize=(7,5))
#plt.plot(t, d,'.', color='blue')
plt.xlabel('Time [HJD]')
#plt.title("Star 1 Photometry ")

t0 = 2442582.4060 #[HJD] initial time
p0 = 0.41986 #[days] period

def epoch(k):
    n_ek = int((t[k] - t0)/p0) #number of cycle since t0
    return n_ek
    
o_c = np.array([]) 
unc= np.array([])
j = 0
while j < len(t):
    o = t[j]
    c = t0 + p0*epoch(j)
    oc = o-c
    o_c = np.append(o_c, oc)
    unc = np.append(unc, inc[j])
    #print(o, c, oc)
    j = j + 1   

   
epoch_array = np.array([])
k = 0
while k < (len(t) ):
    epoch_array = np.append(epoch_array, epoch(k))
    k = k+1

plt.errorbar(epoch_array, o_c, yerr=unc, fmt=',')
pol = np.polyfit(epoch_array, o_c, 1)
plt.plot(epoch_array, (pol[0]* epoch_array) +pol[1], '--', color ="black",
         label= "Liner fit")
plt.ylabel("(O- C) [days]")
plt.xlabel('E ')
plt.title( "(O-C) diagram times-of-maxima.txt")
plt.text(-67300, 0.33,'To = 2442582.4060 HJD')
plt.text(-67300, 0.28,'Po = 0.41986 days')
plt.legend(loc='upper left')
plt.savefig("oc_diagram.png")
plt.show()

HJD_time =  (epoch_array * p0 )  + t0
HJd_max = np.max(HJD_time) #2458446.8161 Saturday, A.D. 2018 Nov 24	07:35:11.0 (UT1)
HJd_min = np.min(HJD_time) #2415290.66628 Friday, A.D. 1900 Sep 28	03:59:26.6	

dt =  HJd_max - HJd_min #with data (observed)
dp = (HJd_max - t0)/epoch(len(t)-1)  - (HJd_min - t0)/epoch(0) #with data
delta = ((inc[0]+ inc[len(t)-1]) /365)/1e6
delta_final  = (dp / dt)* ((delta/abs(dp)) + (delta/abs(dt)) ) 
cpr = dp / dt #change period rate [days/days] 
final_cpr = dp /((dt/365)/1e6)  #change period rate [days/Myr]  +- delta_final
