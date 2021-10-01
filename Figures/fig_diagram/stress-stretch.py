#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 15:28:46 2021

@author: vahidullahtac
"""

import matplotlib.pyplot as plt
import numpy as np

dataset_name = 'stress_strain'
with open('training_data/' + dataset_name + '.npy', 'rb') as f:
    X, Y = np.load(f,allow_pickle=True) 

fsize=20
pltparams = {'legend.fontsize': 'large',
          'figure.figsize': (3,3),
          'axes.labelsize': fsize*1.5,
          'axes.titlesize': fsize*1.5,
          'xtick.labelsize': fsize*1.25,
          'ytick.labelsize': fsize*1.25,
          'axes.titlepad': 25,
          "mathtext.fontset": 'dejavuserif'}
plt.rcParams.update(pltparams)
plt.rcParams["mathtext.fontset"] = 'dejavuserif'

fig,ax = plt.subplots(1)
ax.set_yticklabels([])
ax.set_xticklabels([])
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlabel('$\lambda_1, \lambda_2$')
ax.set_ylabel('$\sigma_1, \sigma_2$')
# ax.set_title('Synthetic/Experimental \nStretch-Stress Data')
# ax.set_title('Training Data')

for i in range(3,11):
    ax.plot(X[i*15:(i+1)*15,1],Y[i*15:(i+1)*15,1],'k-')
fig.savefig('stress-stretch2.jpg', bbox_inches='tight')