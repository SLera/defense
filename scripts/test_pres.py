# -*- coding: utf-8 -*-
"""
Created on Thu Jan 09 11:06:10 2014

@author: lselyuzh
"""
import numpy as np
import os, glob
import datetime
import matplotlib.pyplot as plt
from pylab import *
rcParams['legend.numpoints'] = 1
from scipy import stats

#Plots key events dates and trends

INDIR = '/home/valeria/AWI/HPbckp/LaptevFastIceproject/Scripts/LaptevSea/SELS/Identification of key events/'

years = np.arange(1999,2014,1)

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
    
    
#import dates of the key events

#import dates of beginning of FI season (1999-2014)
fname = INDIR + 'BeginningofFIdevelopment/Beginning_season_new.txt'
begin_FI = doy(fname) 

slope1, intercept1, r_value1, p_value1, std_err1 = stats.linregress(years, begin_FI) 
print slope1, r_value1, p_value1, std_err1   
line1 = slope1*years+intercept1

#import dates of beginning and end of rapid growth (1999-2014) (-2002 for the end of rgrth)
fname = INDIR + 'Rapid growth/Beginning_of_rapid_growth1_new.txt'
begin_rgrth = doy(fname) 

slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(years,begin_rgrth) 
print slope2, r_value2, p_value2, std_err2   
line2 = slope2*years+intercept2


fname = INDIR + 'Rapid growth/End_of_rapid_growth1_new.txt'
end_rgrth = doy(fname)
#remove dates for 2002 and 2013 when the complete data was not avaliable
end_rgrth = np.delete(end_rgrth,[3,14])
#end_rgrth[2]=end_rgrth[2]+2

slope3, intercept3, r_value3, p_value3, std_err3 = stats.linregress(np.delete(years,[2,14]),end_rgrth) 
print slope3, r_value3, p_value3, std_err3  
line3 = slope3*(np.delete(years,[3,14]))+intercept3

#import dates of beginning and end of rapid decrease (1999-2013) -1999,2002
fname = INDIR + 'Rapid decrease/Beginning_of_rapid_decrease1_new.txt'
begin_rdcrs = doy(fname) 
# remove 1999, 2002 
begin_rdcrs = np.delete(begin_rdcrs,[0,3])

slope4, intercept4, r_value4, p_value4, std_err4 = stats.linregress(np.delete(years,[0,3]),begin_rdcrs) 
print slope4, r_value4, p_value4, std_err4   
line4 = slope4*np.delete(years,[0,3])+intercept4

fname = INDIR + 'Rapid decrease/End_of_rapid_decrease1_new.txt'
end_rdcrs = doy(fname) 

slope5, intercept5, r_value5, p_value5, std_err5 = stats.linregress(years,end_rdcrs) 
print slope5, r_value5, p_value5, std_err5   
line5 = slope5*years+intercept5

#import dates of end of FI season (1999-2013), 
fname = INDIR + 'End of FI season/End_season_new.txt'
end_FI = doy(fname) 
end_FI = np.delete(end_FI,0)

slope6, intercept6, r_value6, p_value6, std_err6 = stats.linregress(np.delete(years,-1),end_FI) 
print slope6, r_value6, p_value6, std_err6   
line6 = slope6*np.delete(years,-1)+intercept6


#calculate lenght of the season
season_length = end_FI-np.delete(begin_FI,-1)


slope7, intercept7, r_value7, p_value7, std_err7 = stats.linregress(np.delete(years,0),season_length) 
print slope7, r_value7, p_value7, std_err7   
line7 = slope7*np.delete(years,0)+intercept7


#calculate length of th events periods
rgrth_length = end_rgrth - np.delete(begin_rgrth,[3,14])

slope8, intercept8, r_value8, p_value8, std_err8 = stats.linregress(np.delete(years,[3,14]),rgrth_length) 
print slope8, r_value8, p_value8, std_err8   
line8 = slope8*np.delete(years,[3,14])+intercept8

rdcrs_length = np.delete(end_rdcrs,[0,3]) - begin_rdcrs

slope9, intercept9, r_value9, p_value9, std_err9 = stats.linregress(np.delete(years,[0,3]),rdcrs_length) 
print slope9, r_value9, p_value9, std_err9   
line9 = slope9*np.delete(years,[0,3])+intercept9


#plot figs
fs = 16
lw=2
markersize = 10


fig, ax = plt.subplots(figsize = (6,5))

#ax.plot(years, line2, lw=lw, ls ='-')#b
ax.plot(years, line2, 'k--', lw=2)
p1, = plt.plot(years, begin_rgrth, marker ='o', color ='#FF1F00', markersize=10, markeredgewidth= 1., label = 'Key event 2')
ax.plot(np.delete(years,[2,14]), line3,lw=lw, ls ='--')#k
ax.plot(np.delete(years,[2,14]), line3,ls ='--', lw=2)#k
p2, = plt.plot(np.delete(years,[2,14]), end_rgrth, marker ='o', color = '#05148F', markersize=10, markeredgewidth= 1.,  label = 'Key event 3')


ax.text(0.90, 0.15, 'beginning',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='#FF1F00', fontsize=15)
        
ax.text(0.90, 0.85, 'end',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='#05148F', fontsize=15)

plt.yticks (np.arange(30,220,20),fontsize = 14)
plt.xticks(np.arange(2000,2014,3),fontsize =14)

plt.ylabel('Day since 1 September', fontsize = 18)


name = ''
plt.title(name,fontsize = 16)

l1 = plt.legend([p1],['Key event 2'], loc=4,prop={'size':14})
l2 = plt.legend([p2],['Key event 3'], loc=1, prop={'size':14}) # this removes l1 from the axes.
plt.gca().add_artist(l1) # add l1 as a separate artist to the axes

#plt.text()
plt.grid()
plt.show()

plt.savefig('Trend_RDP_pres', pad_inches=0.1, bbox_inches='tight', dpi = 200)



