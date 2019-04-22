#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 00:30:55 2019

@author: constanzamunoz
"""

import numpy as np
import matplotlib.pyplot as plt

espectro = np.loadtxt("star1.dat")
x = espectro[:, 0] #[Julian date]
y = espectro[:, 1]   #[V Magnitude]

plt.figure(figsize=(7,5))
plt.plot(x, y,',', color='blue')
plt.xlabel('Time [HJD-2400000]')
plt.ylabel('V [Mag]')
plt.title("Star 1 Photometry ")
plt.savefig("star1_photometry.png")