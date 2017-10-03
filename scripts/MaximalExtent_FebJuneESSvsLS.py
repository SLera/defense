# -*- coding: utf-8 -*-
"""
Created on Tue Oct 04 10:15:24 2016

@author: lselyuzh
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import datetime


INDIR = '/home/valeria/AWI/HPbckp/LaptevFastIceproject/Scripts/ESiberian/Output/Monthly_area_seasons/'
INDIR_LS = '/home/valeria/AWI/HPbckp/LaptevFastIceproject/Scripts/LaptevSea/Output/Monthly_area_seasons/'
years = np.arange(1999,2015,1)
years_LS = np.arange(1999,2014,1)

max_extent = []
max_extent_LS = []

for y in years:
    #print y
    #ESS
    area = np.loadtxt(INDIR+str(y)+'_area_s.txt')
    yr,m,d = np.loadtxt(INDIR+str(y)+'_dates_s.txt', unpack= True, dtype=int)
       
    dates = [datetime.date(yr[i],m[i],d[i]) for i in range(len(yr)) ]
    dates = np.array(dates)
    ind = np.where((dates< datetime.date(y+1,6,1)) & (dates > datetime.date(y+1,1,31)))
   
    max_extent_year = area[ind]
    print np.array(max_extent_year).mean(), len(max_extent_year)
    max_extent.append(np.array(max_extent_year).mean())
    
    #LS
    if y in years_LS:
        print y, 'LS'
        area = np.loadtxt(INDIR_LS+str(y)+'_area_s.txt')
        yr,m,d = np.loadtxt(INDIR_LS+str(y)+'_dates_s.txt', unpack= True, dtype=int)
           
        dates = [datetime.date(yr[i],m[i],d[i]) for i in range(len(yr)) ]
        dates = np.array(dates)
        ind = np.where((dates< datetime.date(y+1,6,1)) & (dates > datetime.date(y+1,1,31)))
       
        max_extent_year_LS = area[ind]
        #print np.array(max_extent_year_LS).mean(), len(max_extent_year_LS)
        max_extent_LS.append(np.array(max_extent_year_LS).mean())

max_extent=np.array(max_extent)
max_extent_nN=np.delete(max_extent,2)
std_max_extent= np.std(max_extent_nN)
slope1, intercept1, r_value1, p_value1, std_err1 = stats.linregress(np.delete(years,[2]),np.delete(max_extent, [2])) 
print slope1, r_value1, p_value1, std_err1   
line1 = slope1*years+intercept1

max_extent_LS=np.array(max_extent_LS)
max_extent_nN_LS=np.delete(max_extent_LS,[2,14])
std_max_extent_LS= np.std(max_extent_nN_LS)
slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(np.delete(years_LS,[2,14]),np.delete(max_extent_LS, [2,14])) 
print slope2, r_value2, p_value2, std_err2  
line2 = slope2*years+intercept2



#fig, ax = plt.subplots(figsize = (6,5))
#ax.set_xlim(1998,2016)
#
#ax.plot(years_LS, line1_LS, 'r--', lw=lw)
#p1, = plt.plot(years_LS, end_FI_LS, marker ='o', color ='r', markersize=markersize, markeredgewidth= 1., label = 'end of season')
#
#ax.plot(years_LS, line2_LS, 'k--', lw=lw)
#p2, = plt.plot(years_LS, melt_LS, marker ='o', color ='k', markersize=markersize, markeredgewidth= 1., label = 'melt')
#
#ax.text(2009, 290, 'r = 0.8',
#        verticalalignment='bottom', horizontalalignment='right',
#        color='r',  bbox=props, fontsize=16)
#
#
#plt.yticks (np.arange(250,340,10),fontsize = 14)
#plt.xticks(np.arange(2000,2017,3),fontsize =14)
#
#plt.ylabel('Day since 1 September', fontsize = 16)
#plt.grid()
#plt.legend(loc=0)
#plt.title('Laptev Sea', color = 'red', fontsize = 18)
#plt.savefig('End_melt_LS.pdf', pad_inches=0.1, bbox_inches='tight', fortmat = 'PDF', dpi = 300)

#plot figs
fs = 16
lw=1
markersize = 8
props = dict(boxstyle='round', facecolor='grey', alpha=0.5)

fig, ax = plt.subplots(figsize = (6,5))
ax.set_xlim(1998,2016)

#ax.plot(years, max_extent, lw=lw, label = 'ESS')
p1, = plt.plot(years, max_extent, marker ='o', color ='b', markersize=markersize, markeredgewidth= 1., label = 'ESS')

ax.set_xlim(1998,2016)
ax.set_xticks(np.arange(1999,2017,3))
ax.set_xticklabels(np.arange(2000,2017,3),fontsize = 14)
ax.set_ylim([70000,200000])
ax.set_yticks(np.arange(70000,210000,30000))
ax.plot(years,line1,'b--', lw=lw)

#ax.plot(years_LS, max_extent_LS, lw=lw, c = 'r', label = 'LS')
p2, = plt.plot(years_LS, max_extent_LS, marker ='o', color ='r', markersize=markersize, markeredgewidth= 1., label = 'LS')
ax.plot(years,line2,'r--', lw=lw)

#ax.text(0.95, 0.01, r"STD ="+str(np.round(std_max_extent_LS/10000,0))+r" X $10^3 km^2$",
#        verticalalignment='bottom', horizontalalignment='right',
#        transform=ax.transAxes,
#        color='r', fontsize=14)
std_LS_prc = std_max_extent_LS/max_extent_nN_LS.mean()
ax.text(0.95, 0.15, r"STD ="+str(np.round(std_LS_prc*100,0))+r"%",
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='r', fontsize=16)
        
#ax.text(0.05, 0.90, r"STD ="+str(np.round(std_max_extent/10000,0))+r" X $10^3 km^2$",
#        verticalalignment='bottom', horizontalalignment='right',
#        transform=ax.transAxes,
#        color='b', fontsize=14)
std_prc = std_max_extent/max_extent_nN.mean()
ax.text(0.40, 0.85, r"STD ="+str(np.round(std_prc*100,0))+r"%",
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='b', fontsize=16)
        
ax.set_ylabel(u"$10^3 km^2$", fontsize = 18)
ax.set_yticklabels(('70','100','130','160','190'),fontsize=14)


plt.title('Mean Feb-June Fast Ice Area', fontsize = 18)
#plt.legend(prop={'size':18})
#plt.grid(axis='x')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
plt.savefig('WinterArea_FebMay.pdf', pad_inches=0.1, bbox_inches='tight', fortmat = 'PDF', dpi = 300)    
#
#plt.yticks (np.arange(210,310,10),fontsize = 19)
#
#plt.ylabel('days', fontsize = 20)
#plt.grid(axis='x')
#name = 'Duration of fast ice season'
#plt.title(name,fontsize = 24)
#plt.legend(loc=4, prop={'size':18})
#
#plt.show()