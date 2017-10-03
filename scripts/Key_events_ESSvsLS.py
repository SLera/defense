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
    
    
#import dates of the key events

#import dates of beginning of FI season (1999-2014)
fname = INDIR_LS + 'BeginningofFIdevelopment/Beginning_season_new.txt'
begin_FI_LS = doy(fname) 

slope1_LS, intercept1_LS, r_value1_LS, p_value1_LS, std_err1_LS = stats.linregress(years_LS, begin_FI_LS) 
print slope1_LS, r_value1_LS, p_value1_LS, std_err1_LS   
line1_LS = slope1_LS*years_LS+intercept1_LS

fname = INDIR_ESS + 'Beginning_season.txt'
begin_FI_ESS = doy(fname) 

slope1_ESS, intercept1_ESS, r_value1_ESS, p_value1_ESS, std_err1_ESS = stats.linregress(np.delete(years_ESS,14), np.delete(begin_FI_ESS,14)) 
print slope1_ESS, r_value1_ESS, p_value1_ESS, std_err1_ESS   
line1_ESS = slope1_ESS*years_ESS+intercept1_ESS

#plot figs
fs = 16
lw=2
markersize = 10

fig, ax = plt.subplots(figsize = (6,5))

ax.plot(years_LS, line1_LS, 'k--', lw=lw)
p1, = plt.plot(years_LS, begin_FI_LS, marker ='o', color ='r', markersize=markersize, markeredgewidth= 1., label = 'LS')

ax.plot(np.delete(years_ESS,14), np.delete(line1_ESS,14), 'k--', lw=lw)
p1, = plt.plot(np.delete(years_ESS,14), np.delete(begin_FI_ESS,14), marker ='o', color ='b', markersize=markersize, markeredgewidth= 1., label = 'ESS')

ax.text(0.90, 0.15, 'LS',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='r', fontsize=15)
        
ax.text(0.90, 0.85, 'ESS',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='b', fontsize=15)

plt.yticks (np.arange(30,100,10),fontsize = 14)
plt.xticks(np.arange(2000,2014,3),fontsize =14)

plt.ylabel('Day since 1 September', fontsize = 18)


name = 'Beginning of season'
plt.title(name,fontsize = 16)

#l1 = plt.legend([p1],['Key event 2'], loc=4,prop={'size':14})
#l2 = plt.legend([p2],['Key event 3'], loc=1, prop={'size':14}) # this removes l1 from the axes.
#plt.gca().add_artist(l1) # add l1 as a separate artist to the axes

#plt.text()

plt.grid()
plt.show()

plt.savefig('BEginning_LSvsESS', pad_inches=0.1, bbox_inches='tight', dpi = 300)


#ax.plot(years_LS, max_extent, lw=1.5, label = 'LS')
#ax.plot(years, max_extent, 'o', markeredgecolor='r',markeredgewidth=1.5, markerfacecolor='r')
#ax.set_xlim([1998,2016])
#ax.set_xticks(np.arange(1999,2017,2))
#ax.set_xticklabels(np.arange(1999,2017,2),fontsize = 14)
#ax.set_ylim([70000,200000])
#ax.set_yticks(np.arange(70000,210000,30000))
#ax.plot(years,line1,'b--', lw=1)
#
#ax.plot(years_LS, max_extent_LS, lw=1.5, c = 'r', label = 'LS')
#ax.plot(years_LS, max_extent_LS, 'o', markeredgecolor='r',markeredgewidth=1.5, markerfacecolor='None')
#ax.plot(years,line2,'r--', lw=1)