# -*- coding: utf-8 -*-
"""
Created on Fri Dec 3 14:10:08 2021

@author: shash
"""


import gurobipy as gp
from gurobipy import GRB
#create a model
m = gp.Model("Project on Management Accounting")

#create decision variables
x1 = m.addVar(vtype = GRB.CONTINUOUS, name ='x1')
x2 = m.addVar(vtype = GRB.CONTINUOUS, name ='x2')


#set objective
m.setObjective(350*x1+300*x2, GRB.MAXIMIZE)

#add constraints
m.addConstr(x1 + x2<=200,"c0")
m.addConstr(18*x1 + 12*x2 <= 3132,"c1")
m.addConstr(6*x1 + 8*x2 <= 1440, "c2")

m.optimize()

obj = m.getObjective()

for v in m.getVars():
    print(v.varName, v.x)

print('Obj:', obj.getValue())
