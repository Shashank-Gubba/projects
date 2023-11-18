# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 00:31:01 2021

@author: shash
"""
##1
import pandas as pd
import matplotlib.pyplot as plt

# reading the data set as a data frame
df= pd.read_csv('cancer.csv')
# naming the columns 
df.columns=["diameter","pigment","cancerous"]
col1=df["diameter"]
col2=df["pigment"]
#calculating the correlation coeff 
coeff=col1.corr(col2)
print("Coefficient: ",coeff)





