# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 19:45:38 2021

@author: shash
"""

import pandas as pd
# reading csv file as data frame
df=pd.read_csv('cancer.csv')
#naming the columns
df.columns=["diameter","pigment","cancerous"]
#assigning columns
col1=df["diameter"]
col2=df["pigment"]
col3=df["cancerous"]

can=0
ncan=0
c=0
nc=0
# adding up cancerous and non-cancerous values seperately
for i,j in zip(col1,col3):
    if(j==0):
        ncan+=i
        nc+=1
    else:
        can+=i
        c+=1
#printing added values
print('Sum of non-cancerous observations:'+str(ncan)+"\n"+'No.of non-cancerous observations:'
      +str(nc)+"\n"+'Sum of cancerous observations:'+str(can)+"\n"+'No.of cancerous observations:'+str(c))
# calculating the averages
Cancerous_avg=can/c 
nonCancerous_avg=ncan/nc 
#printing averages
print('Average diameter of non-cancerous observations:'+str(nonCancerous_avg)+"\n"
      +'Average diameter of cancerous observations:'+str(Cancerous_avg)) 
     
        