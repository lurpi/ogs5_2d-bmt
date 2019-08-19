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
import numpy as np
#-------------------------------
#         define parameters
#
#-------------------------------
strike = 90
dip = 65
#-------------------------------
#         define functions to compute 
#        (project and rotate) stresses
#
#-------------------------------

def ogs_to_sn(syy,szz,syz, dr): # dr is dip  in radians
   nor=[]
   she=[]
   dr=np.pi/2.-dr
   for jj in range(0,len(szz),1):
        norm=0.5*(-syy[jj]-szz[jj])+0.5*(-syy[jj]+szz[jj])*np.cos(2*dr)+syz[jj]*np.sin(2*dr)
        #(((syy[jj])*np.sin(dr)*np.sin(dr))-2*syz[jj]*(np.sin(dr)*np.cos(dr))+(szz[jj])*(np.cos(dr)*np.cos(dr)))
        shear=(0.5*(-syy[jj]+szz[jj])*np.sin(2.*dr)-(syz[jj]*np.cos(2*dr)))
        #(0.5*(szz[jj]-syy[jj])*np.cos(-2.*dr)-(syz[jj]*np.sin(2*dr)))
        nor.append(norm)
        she.append(shear)        

   return nor,she

#-------------------------------
#         define files and columns header
#
#-------------------------------
r0="taskB-2d_time_INJ_POINT_OFFFAULT.tec"
r3="taskB-2d_time_INJ_POINT_OFFFAULT.tec"

column_hist1 = ("TIME","STRAIN_PLS","PRESSURE1","STRESS_XX","STRESS_YY","STRESS_ZZ","STRESS_XY","STRESS_XZ","STRESS_YZ","VELOCITY_X1","VELOCITY_Y1","VELOCITY_Z1","DISPLACEMENT_X1","DISPLACEMENT_Y1","DISPLACEMENT_Z1","p_(1st_Invariant)","q_(2nd_Invariant)","Effective_Strain")
column_hist3 = ("TIME","STRAIN_PLS","PRESSURE1","STRESS_XX","STRESS_YY","STRESS_ZZ","STRESS_XY","STRESS_XZ","STRESS_YZ","VELOCITY_X1","VELOCITY_Y1","VELOCITY_Z1","DISPLACEMENT_X1","DISPLACEMENT_Y1","DISPLACEMENT_Z1","p_(1st_Invariant)","q_(2nd_Invariant)","Effective_Strain")
chist0=("TIME","STRAIN_PLS","PRESSURE1","STRESS_XX","STRESS_YY","STRESS_ZZ","STRESS_XY","STRESS_XZ","STRESS_YZ","VELOCITY_X1","VELOCITY_Y1","VELOCITY_Z1","DISPLACEMENT_X1","DISPLACEMENT_Y1","DISPLACEMENT_Z1","p_(1st_Invariant)","q_(2nd_Invariant)","Effective_Strain")

p0 = pd.read_csv(r0, skiprows=2, header=0, names=column_hist1, delimiter=r"\s+")  

p3 = pd.read_csv(r3, skiprows=2, header=0, names=column_hist3, delimiter=r"\s+") 
 
#-------------------------------
#         assign data to arrays
#
#-------------------------------
T3=p3["TIME"].values
P_f2=p3["PRESSURE1"].values
#-------------------------------
#         compute Normal N3 and Shear S3 stress
#         (function reads values from OGS output files)
#-------------------------------
N3,S3= ogs_to_sn(-p3["STRESS_YY"].values,-p3["STRESS_ZZ"].values,p3["STRESS_YZ"].values, np.pi-np.deg2rad(dip))

#-------------------------------
#         calculate Mohr envelope
# will be used in
#        plt.plot(tx,np.tan(np.deg2rad(22))*ty+coh, 'b--')
#        plt.plot(tx,-1.0*np.tan(np.deg2rad(22))*ty-coh, 'b--')
#-------------------------------
tx = -1.*np.arange(0., 9e6, 1e5)
ty = np.arange(0., 9e6, 1e5)
coh=1.e6

#-------------------------------
#         prepare and draw plot
#
#-------------------------------

plt.figure(figsize=(8,5))
plt.scatter(N3, S3, c=T3, s=75, cmap=plt.cm.plasma, edgecolors='black', alpha=0.75)
plt.plot(tx,np.tan(np.deg2rad(22))*ty+coh, 'b--')
plt.plot(tx,-1.0*np.tan(np.deg2rad(22))*ty-coh, 'b--')
plt.axis([-6.75e6, -0., -2.e6, 2e6])
# plot annotations (arrow + text box)
plt.annotate('Time 0',
                   xy=(N3[0],S3[0]), xycoords='data',
                   xytext=(10, -35), textcoords='offset points',
                   arrowprops=dict(arrowstyle="->", edgecolor='green',shrinkB=0., 
                                   connectionstyle="angle3", lw=2.5), bbox=dict(boxstyle="square", fc="w"))
plt.annotate('Time :'+np.str(np.trunc(T3[-1])),
                   xy=(N3[-1],S3[-1]), xycoords='data',
                   xytext=(10, +35), textcoords='offset points',
                   arrowprops=dict(arrowstyle="->", edgecolor='green',shrinkB=0., 
                                   connectionstyle="angle3", lw=2.5), bbox=dict(boxstyle="square", fc="w"))
if len(T3)>43:                                   
   plt.annotate('Time :'+np.str(np.trunc(T3[43]))+' Pressure :'+np.str(np.trunc(P_f2[43]/1.e3)/1.e3)+' MPa',
                   xy=(N3[43],S3[43]), xycoords='data',
                   xytext=(-200, -35), textcoords='offset points',
                   arrowprops=dict(arrowstyle="->", edgecolor='green',shrinkB=0., 
                                   connectionstyle="angle3", lw=2.5), bbox=dict(boxstyle="square", fc="w"))
if len(T3)>95:                                   
    plt.annotate('Time :'+np.str(np.trunc(T3[95]))+' Pressure :'+np.str(np.trunc(P_f2[95]/1.e3)/1.e3)+' MPa',
                   xy=(N3[95],S3[95]), xycoords='data',
                   xytext=(-150, -47.5), textcoords='offset points',
                   arrowprops=dict(arrowstyle="->", edgecolor='green',shrinkB=0., 
                                   connectionstyle="angle3", lw=2.5), bbox=dict(boxstyle="square", fc="w"))
if len(T3)>174:                                   
    plt.annotate('Time :'+np.str(np.trunc(T3[174]))+' Pressure :'+np.str(np.trunc(P_f2[174]/1.e3)/1.e3)+' MPa',
                   xy=(N3[174],S3[174]), xycoords='data',
                   xytext=(-100, -60), textcoords='offset points',
                   arrowprops=dict(arrowstyle="->", edgecolor='green',shrinkB=0., 
                                   connectionstyle="angle3", lw=2.5), bbox=dict(boxstyle="square", fc="w"))

if len(T3)>188:                                   
    plt.annotate('Time :'+np.str(np.trunc(T3[188]))+' Pressure :'+np.str(np.trunc(P_f2[188]/1.e3)/1.e3)+' MPa',
                   xy=(N3[188],S3[188]), xycoords='data',
                   xytext=(-100, -60), textcoords='offset points',
                   arrowprops=dict(arrowstyle="->", edgecolor='green',shrinkB=0., 
                                   connectionstyle="angle3", lw=2.5), bbox=dict(boxstyle="square", fc="w"))
# define axis legends, title,  colorbar
plt.title('Stress evolution in the fault, point %s' %r3, fontsize=24)
plt.xlabel('Normal stress (MPa)', fontsize=20)
plt.ylabel('Shear stress (MPa)', fontsize=20)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
cb=plt.colorbar()
cb.set_label('Injection time', fontsize=14)
plt.grid()
plt.show()

