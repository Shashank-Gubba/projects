import pandas as pd
import matplotlib.pyplot as plt

# reading the data set as a data frame
df= pd.read_csv('cancer.csv')
# naming the columns 
df.columns=["diameter","pigment","cancerous"]
# assigning columns
col1=df["diameter"]
col2=df["pigment"]
# calculating standard deviation 
std1=col1.std()
std2=col2.std()
coeff=col1.corr(col2)
# calculating slope
m=coeff*(std1/std2)
x=[]
y=[]

#plotting the graph    
plt.title('Skin Cancer by Lesion Diameter and Pigment Density')
plt.xlabel('Diameter of lesion (mm)')
plt.ylabel('Pigment density of lesion')

# calculating averages
xbar=col1.sum()/len(df)
ybar=col2.sum()/len(df)

#calculating y-intercept
b=xbar-m*ybar
for i in col1:
    y.append(m*i+b)
    x.append(i)
plt.plot(x,y)
print(b)