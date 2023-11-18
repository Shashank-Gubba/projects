# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 21:48:19 2021

@author: shash
"""

import pandas as pd
#reading csvfile
stockData=pd.read_csv('stockGrowth.csv')
#assigning maximum and minimum of growth, market cap, risk values to variables
maxGrowth=stockData['Growth'].max()
minGrowth=stockData['Growth'].min()
maxMcap=stockData['Market Cap'].max()
minMcap=stockData['Market Cap'].min()
maximumRisk=stockData['Risk'].max()
minimumRisk=stockData['Risk'].min()

growth=4.5
MarketCap=4000000000
risk=0.5
length=len(stockData)
dist=[]
#calculating differences
for i in range(length):
    Growth_diff=abs(growth-stockData['Growth'][i])/(maxGrowth-minGrowth)
    MarketCap_diff=abs(MarketCap-stockData['Market Cap'][i])/(maxMcap-minMcap)
    Risk_diff=abs(risk-stockData['Risk'][i])/(maximumRisk-minimumRisk)
    dist.append([(Growth_diff**2+MarketCap_diff**2+Risk_diff**2)**0.5,i])
print('Growth difference:'+str(Growth_diff))
print('Market cap difference:'+str(MarketCap_diff))
print('Risk difference:'+str(Risk_diff))

dist.sort()
print(dist[0:5])