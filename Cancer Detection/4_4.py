# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 20:21:47 2021

@author: shash
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#reading csv file as data frame
df=pd.read_csv('cancer.csv')
#naming the columns
df.columns=['Diameter','Pigment','Cancerous']
#sorting the data and adding no.of observations
sorted_data=df.sort_values(by=['Cancerous','Diameter'])
number_cancerous=np.sum(df['Cancerous'])
number_noncancerous=50-number_cancerous

noncancerousData=sorted_data[0:number_noncancerous]
cancerousData=sorted_data[number_noncancerous:]

from scipy.stats import ttest_ind
ttest_ind(cancerousData['Diameter'],noncancerousData['Diameter'])
