# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 09:52:34 2015

@author: Luca Urpi
"""
#-------------------------------
#         import useful modules
#
#-------------------------------
import matplotlib.pyplot as plt
import pandas as pd

#-------------------------------
#         define files and columns header
#
#-------------------------------
r0="taskB-2d_time_INJ_POINT.tec"
r1="taskB-2d_time_MONITORING2.tec"
r2="taskB-2d_time_AW2.tec"
column_hist1 = ("TIME","STRAIN_PLS","PRESSURE1","STRESS_XX","STRESS_YY","STRESS_ZZ","STRESS_XY","STRESS_XZ","STRESS_YZ","VELOCITY_X1","VELOCITY_Y1","VELOCITY_Z1","DISPLACEMENT_X1","DISPLACEMENT_Y1","DISPLACEMENT_Z1","p_(1st_Invariant)","q_(2nd_Invariant)"," Effective_Strain")
column_hist0 = ("TIME","STRAIN_PLS","VELOCITY_X1","VELOCITY_Y1","VELOCITY_Z1","DISPLACEMENT_X1","DISPLACEMENT_Y1","DISPLACEMENT_Z1","PRESSURE1","STRESS_XX","STRESS_YY","STRESS_ZZ","p_(1st_Invariant)","q_(2nd_Invariant)","Effective_Strain")
column_hist3 = ("TIME","STRAIN_PLS","VELOCITY_X1","VELOCITY_Y1","VELOCITY_Z1","DISPLACEMENT_X1","DISPLACEMENT_Y1","DISPLACEMENT_Z1","PRESSURE1","STRESS_XX","STRESS_YY","STRESS_ZZ","STRESS_XY","STRESS_XZ","STRESS_YZ","p_(1st_Invariant)","q_(2nd_Invariant)"," Effective_Strain")


p0 = pd.read_csv(r0, skiprows=2, header=0, names=column_hist0, delimiter=r"\s+")  
p1 = pd.read_csv(r1, skiprows=2, header=0, names=column_hist1, delimiter=r"\s+")  
p2 = pd.read_csv(r2, skiprows=2 ,header=0, names=column_hist3, delimiter=r"\s+")  

#-------------------------------
#         assign data to arrays
#
#-------------------------------
X= p0["TIME"].values
X1= p1["TIME"].values
X2= p2["TIME"].values
P_inj = p0["PRESSURE1"].values
P1 = p1["PRESSURE1"].values
P2 = p2["PRESSURE1"].values

#-------------------------------
#         prepare and draw plot
#
#-------------------------------
fig3 = plt.figure(figsize=(9,6))
ax1 = fig3.add_subplot(111)
ax1.plot(X, P_inj/1.e6, 'k--', lw=1.5,label='Injection pressure')
ax1.plot(X1, P1/1.e6, 'bo', lw=2.5,label='Pressure at monitoring2')
ax1.set_xlabel('Time (s)', fontsize=28)
ax1.set_ylabel('Pressure (MPa)', fontsize=28)
ax1.tick_params(axis='y', labelsize=24)
ax1.tick_params(axis='x', labelsize=24)
ax1.set_xlim(0,850)
ax1.set_ylim(0,1.1)
plt.legend(loc=2)
plt.tight_layout()
plt.grid()
#plt.savefig("FM1_upd.png",dpi=600)
plt.show()


