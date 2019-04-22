#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 00:37:15 2019

@author: constanzamunoz
"""

import numpy as np
import matplotlib.pyplot as plt
from astropy.stats import LombScargle



espectro = np.loadtxt("star2.dat")
x = espectro[:, 0] #[Julian date]
y = espectro[:, 1]   #[V Magnitude]

plt.figure(figsize=(7,5))
plt.plot(x -2400000.5, y,'.', color='blue')
plt.xlabel('Time [MJD]')
plt.ylabel('V [Mag]')
plt.title("Star 2 Photometry ")
#plt.savefig("star2_photometry.png")
plt.show()
"""
plt.figure(figsize=(7,5))
frequency, power = LombScargle(x, y).autopower()
plt.plot(frequency, power, color="blue", label="Max: "+str(max(power)))  
plt.xlabel('Frequency')
plt.ylabel('Lomb-Scargle Power')
plt.legend()
plt.title("Star 1 Periodgram")

plt.show()
best_frequency = frequency[np.argmax(power)]
x_fit = np.linspace(0, 1)
y_fit = LombScargle(x, y).model(x_fit, best_frequency)
plt.plot(x_fit, y_fit)


"""

