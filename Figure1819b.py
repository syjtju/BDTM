# -*- coding: utf-8 -*-
"""
Created on Fri May 17 12:16:12 2024

@author: Jay Sun
"""

import csv
with open('piir_sentiment_sr_case2.csv',encoding='gbk',errors='ignore') as total:
    reader = csv.reader(total)
    t1 = [row[1] for row in reader]
with open('piir_sentiment_sr_case2.csv',encoding='gbk',errors='ignore') as total:
    reader = csv.reader(total)    
    t2 = [row[2] for row in reader]
#%%
thetasr = []
for i in range(1, 51):
    t = [float(t1[i]), float(t2[i])]
    thetasr.append(t)

#%%
from class_SRJST import SRJST

sr = SRJST(3, 50, 2)
nmk = sr._initialize_()
#%%
NMK = []
for i in nmk:
    NMK.append(len(i))
#%%
from scipy.stats import entropy  
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
IC = [0.3306, 0.6694]
SKall = np.zeros(len(thetasr))
for t in range(len(thetasr)):
    SKall[t] = NMK[t] * entropy(IC, np.array(thetasr[t]))
SKi = pd.DataFrame(SKall) 
SKie = SKi[0].ewm(alpha = 0.3).mean()
    
CL_k = np.percentile(SKie, 90)
cl_listk = np.zeros(len(SKie))
for i in range(len(cl_listk)):
    cl_listk[i] = CL_k
plt.xlabel('time')
plt.ylabel('Charting Statistics')
plt.plot(range(len(SKie)), SKie,'-o',color = 'k', \
         markersize=2, linewidth = 0.8)
    
plt.plot(range(len(cl_listk)), cl_listk, color = 'k',\
         dashes=(5, 3), linewidth = 0.8, linestyle = '--',\
             label = 'Control Limit = 8.0530')
plt.legend()  
#%%
with open('piar_sentiment_sr_case2.csv',encoding='gbk',errors='ignore') as total:
    reader = csv.reader(total)
    t1a = [row[1] for row in reader]
with open('piar_sentiment_sr_case2.csv',encoding='gbk',errors='ignore') as total:
    reader = csv.reader(total)    
    t2a = [row[2] for row in reader]
#%%
thetasra = []
for i in range(1, 51):
    t = [float(t1a[i]), float(t2a[i])]
    thetasra.append(t)
from class_SRJST_ar import SRJSTar
sra = SRJSTar(3, 50, 2)
nmka = sra._initialize_()
#%%
from scipy.stats import entropy  
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

NMKA = []
for i in nmka:
    NMKA.append(len(i))

IC = [0.3306, 0.6694]
SKalla = np.zeros(len(thetasra))
for t in range(len(thetasra)):
    SKalla[t] = NMK[t] * entropy(IC, np.array(thetasra[t]))
SKia = pd.DataFrame(SKalla) 
SKiea = SKia[0].ewm(alpha = 0.3).mean()
    
CL_ka = np.percentile(SKiea, 90)
cl_listka = np.zeros(len(SKiea))
for i in range(len(cl_listka)):
    cl_listka[i] = CL_k
plt.xlabel('time')
plt.ylabel('Charting Statistics')
plt.plot(range(len(SKiea)), SKiea,'-o',color = 'k', \
         markersize=2, linewidth = 0.8)
    
plt.plot(range(len(cl_listka)), cl_listka, color = 'k',\
         dashes=(5, 3), linewidth = 0.8, linestyle = '--',\
             label = 'Control Limit = 7.7703')
plt.legend() 