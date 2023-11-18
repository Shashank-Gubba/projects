
#importing libraries and models
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import numpy as np

#reading the data
df= pd.read_csv("C:\\Users\\shash\\OneDrive\\Desktop\\Computing for Business Analytics\\Assignment 6\\NBA201516.csv")
#assigning the variables
y=df["PS/G"]
x=df[["AST","STL","MP"]]
#splitting the data for testing and training
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)
LR = LinearRegression()
LR.fit(x_train,y_train)
y_prediction =  LR.predict(x_test)
# predicting the accuracy score
score=r2_score(y_test,y_prediction)
print("r2 score is=",score)
print("mean_sqrd_error is=",mean_squared_error(y_test,y_prediction))
print("root_mean_squared error of is=",np.sqrt(mean_squared_error(y_test,y_prediction)))
print(LR.coef_)
print("Intercept:",LR.intercept_)
#adjusted r2 score
ad_r2 = 1 - (1-r2_score(y_test,y_prediction)) * (len(y)-1)/(len(y)-x.shape[1]-1)
print('adjusted r2 score is:',ad_r2)