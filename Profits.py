
"""
Created on Tue Nov  2 18:55:33 2021

@author: shash
"""
#importing required libraries and models
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#reading the csv file
custLoc=pd.read_csv("C:\\Users\\shash\\OneDrive\\Desktop\\Computing for Business Analytics\\Assignment 6\\customerLocations.csv",header=None,names=['x','y'])
#declaring empty lists
shop=[]
profit=[]
#here we are looping in range of 1,21 and assuming the costs and profits of 20 shops
for k in range(1,21):
#giving the customerLocations as input variable
    kmeans = KMeans(k).fit(custLoc)
#here clusterCenters gives us the average of all the points belonging to the cluster
    clusterCenters=kmeans.cluster_centers_
#now calling the labels_ function of kmean which provide the labels of each point     
    clusterMembership=kmeans.labels_

#declaring the empty dictionary    
    distanceCustomerToNearestStore={}
#intialising the variable to zero
    sumOfCustomerMarginProfits=0
#looping the customer number upto 10000
    for customerNumber in range(0,10000):
#declaring new variables for customer locations
        customerXLocation=custLoc['x'][customerNumber]
        customerYLocation=custLoc['y'][customerNumber]
#finding the nearest shops locations to customer 
        nearestStorenumber=clusterMembership[customerNumber]
        nearestStoreXLocation=clusterCenters[nearestStorenumber][0]
        nearestStoreYLocation=clusterCenters[nearestStorenumber][1]
        distanceCustomerToNearestStore[customerNumber]=((customerXLocation-nearestStoreXLocation)**2+(customerYLocation-nearestStoreYLocation)**2)**0.5
#finding the profit from current customer and saving it variable        
        profitFromThisCustomer=1000/(1+distanceCustomerToNearestStore[customerNumber])
#adding up the profit from current customer to final/total profit
        sumOfCustomerMarginProfits+=profitFromThisCustomer
        
#finding the cost of opening the shops based on number of shops
costsOfOpeningStores=500000*k

#printing the number of shops and profit obtained
print('Profit from 20 stores is:'+str(k))
#finding the total profits
totalProfit=sumOfCustomerMarginProfits-costsOfOpeningStores
shop.append(k)
profit.append(totalProfit)
print(totalProfit)
print('Total customer profits:')
print(sumOfCustomerMarginProfits)
print('Store opening cost:')
print(costsOfOpeningStores)

#plotting the number of shops vs total profit graph
plt.title('No. of shops vs. Profit')
plt.scatter(shop,profit)
plt.xlabel('Number of shops')
plt.ylabel('Total profit')
plt.show()

#plotting the clusters
plt.scatter(clusterCenters[:,0],clusterCenters[:,1],c='blue')