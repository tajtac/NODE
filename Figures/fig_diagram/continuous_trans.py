#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 04:23:23 2021

@author: vahidullahtac
Description: Generate vector field image
"""

import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.size'] = 15

t,y = np.meshgrid(np.linspace(0,1,10),np.linspace(-1,1,10))

fig, ax = plt.subplots()
fig.set_size_inches((5,3))
u = np.sin(t)
v = np.sin(y)
ax.quiver(t,y,u,v, color='#DCDCDC')
ax.yaxis.set_visible(False)
ax.set_xlim([0,1])

t = np.linspace(0,1,50)
y = np.cos(t) - 1.2
ax.plot(t,y,'k-')

t = np.random.choice(t, 10)
t = np.append(t,0)
t = np.append(t,1)
y = np.cos(t) - 1.2
ax.plot(t,y,'ko')

fig.savefig('continuous_trans.jpg', dpi = 200)