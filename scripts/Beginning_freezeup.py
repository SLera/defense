#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 14:22:47 2017

@author: valeria
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import datetime


INDIR_ESS = '/home/valeria/AWI/HPbckp/LaptevFastIceproject/Scripts/ESiberian/ESS/IdentificationKeyEvents/'
INDIR_LS = '/home/valeria/AWI/HPbckp/LaptevFastIceproject/Scripts/LaptevSea/SELS/Identification of key events/'

years_ESS = np.arange(1999,2016,1)
years_LS = np.arange(1999,2014,1)

#here days since September 1
def doy(fname):
    f = open(fname)
    table = [row.strip().split('\t') for row in f]
    f.close()
    date_of_event = np.array(table, int)
    
    doy_date = []
    dates = []
    for i in range(len(date_of_event)):
        year = date_of_event[i][0]
        month = date_of_event[i][1]
        day = date_of_event[i][2]
        date = datetime.date(year, month, day)
        dates.append(date)
        
        Sep1 = datetime.date(year,9,1)
        #Jan1 = datetime.date(year,1,1)
        ddays = date-Sep1
        if ddays.days<0.:
            Sep1 = datetime.date(year-1,9,1)
            ddays = date-Sep1
        doy_date.append(ddays.days)
        
    return np.array(doy_date)
    
    
def doytodas(year, doy):
    "convert day of year to day after September 1"
    Sep1 = datetime.date(year,9,1)
    Jan1 = datetime.date(year,1,1)
    ddif = Sep1 -Jan1
    das = doy-ddif.days
    if das <0.:
        Sep1 = datetime.date(year-1,9,1)
        ddif = Sep1 -Jan1
        das = doy-ddif.days
    return das

#plot figs
fs = 16
lw=1
markersize = 8
props = dict(boxstyle='round', facecolor='grey', alpha=0.5)
    
### LS  
#import dates of the key events

#import dates of beginning of FI season (1999-2014)
fname = INDIR_LS + 'BeginningofFIdevelopment/Beginning_season_new.txt'
begin_FI_LS = doy(fname) 

slope1_LS, intercept1_LS, r_value1_LS, p_value1_LS, std_err1_LS = stats.linregress(years_LS, begin_FI_LS) 
print slope1_LS, r_value1_LS, p_value1_LS, std_err1_LS   
line1_LS = slope1_LS*years_LS+intercept1_LS

fname_freezeup = '/home/valeria/AWI/HPbckp/LaptevFastIceproject/Scripts/LaptevSea/SELS/Freezup-Melt_onset/date_freeze_1999-2013.txt'
freezeup_LS = doy(fname_freezeup) 
slope2_LS, intercept2_LS, r_value2_LS, p_value2_LS, std_err2_LS = stats.linregress(years_LS, freezeup_LS) 
print slope2_LS, r_value2_LS, p_value2_LS, std_err2_LS   
line2_LS = slope2_LS*years_LS+intercept2_LS


fig, ax = plt.subplots(figsize = (6,5))
ax.set_xlim(1998,2016)

ax.plot(years_LS, line1_LS, 'r--', lw=lw)
p1, = plt.plot(years_LS, begin_FI_LS, marker ='o', color ='r', markersize=markersize, markeredgewidth= 1., label = 'beginning of season')

ax.plot(years_LS, line2_LS, 'k--', lw=lw)
p2, = plt.plot(years_LS, freezeup_LS, marker ='o', color ='k', markersize=markersize, markeredgewidth= 1., label = 'freezeup')

ax.text(2009, 10, 'r = 0.6',
        verticalalignment='bottom', horizontalalignment='right',
        color='r',  bbox=props, fontsize=16)


plt.yticks (np.arange(0,100,10),fontsize = 14)
plt.xticks(np.arange(2000,2017,3),fontsize =14)

plt.ylabel('Day since 1 September', fontsize = 16)
plt.grid()
plt.legend(loc=2)
plt.title('Laptev Sea', color = 'red', fontsize = 18)
plt.savefig('Beginning_frzp_LS.pdf', pad_inches=0.1, bbox_inches='tight', fortmat = 'PDF', dpi = 300)
#plt.close('all')

### ESS
#import dates of beginning of FI season (1999-2014)
fname = INDIR_ESS + 'Beginning_season.txt'
begin_FI_ESS = doy(fname) 

slope1_ESS, intercept1_ESS, r_value1_ESS, p_value1_ESS, std_err1_ESS = stats.linregress(np.delete(years_ESS,14), np.delete(begin_FI_ESS,14)) 
print slope1_ESS, r_value1_ESS, p_value1_ESS, std_err1_ESS   
line1_ESS = slope1_ESS*years_ESS+intercept1_ESS

fname_freezeup = '/home/valeria/AWI/HPbckp/LaptevFastIceproject/Scripts/ESiberian/ESS/Freezeup-Melt Onset/Date_freeze_ESS_1999-2014.txt'
freezeup_ESS = doy(fname_freezeup) 
slope2_ESS, intercept2_ESS, r_value2_ESS, p_value2_ESS, std_err2_ESS = stats.linregress(np.delete(years_ESS,-1), freezeup_ESS) 
print slope2_ESS, r_value2_ESS, p_value2_ESS, std_err2_ESS
line2_ESS = slope2_ESS*years_ESS+intercept2_ESS


fig, ax = plt.subplots(figsize = (6,5))
ax.set_xlim(1998,2016)

ax.plot(years_ESS, line1_ESS, 'b--', lw=lw)
p1, = plt.plot(np.delete(years_ESS,14), np.delete(begin_FI_ESS,14), marker ='o', color ='b', markersize=markersize, markeredgewidth= 1., label = 'beginning of season')

ax.plot(years_ESS, line2_ESS, 'k--', lw=lw)
p2, = plt.plot(np.delete(years_ESS,-1), freezeup_ESS, marker ='o', color ='k', markersize=markersize, markeredgewidth= 1., label = 'freezeup')

props = dict(boxstyle='round', facecolor='grey', alpha=0.5)

ax.text(2009, 10, 'r = 0.8',
        verticalalignment='bottom', horizontalalignment='right',
        color='b',  bbox=props, fontsize=16)

plt.yticks (np.arange(0,100,10),fontsize = 14)
plt.xticks(np.arange(2000,2017,3),fontsize =14)

plt.ylabel('Day since 1 September', fontsize = 16)
plt.grid()
plt.legend(loc=2)
plt.show()
plt.title('East Siberian Sea', color = 'b', fontsize = 18)
plt.savefig('Beginning_frzp_ESS.pdf', pad_inches=0.1, bbox_inches='tight', fortmat = 'PDF', dpi = 300)