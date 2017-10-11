#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 17:10:12 2017

@author: valeria
"""

import matplotlib
matplotlib.use('qt5agg')

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import glob, os
import matplotlib as mpl

#INDIR = 'X:\\LaptevFastIceproject\\Scripts\\LaptevSea\\Output\\Monthly_frequency_new\\temp\\'
#OUTDIR = 'X:\\LaptevFastIceproject\\Scripts\\LaptevSea\Output\\Monthly_frequency_new\\temp\\Figures\\'

INDIR = '/home/valeria/AWI/HPbckp/LaptevFastIceproject/Scripts/LaptevSea/Output/LS_SE_1km_new_lm_Oct_Jul_Seasons/2000'
OUTDIR = '/home/valeria/Jacobs/Defense/defense/laptev/'


def create_map(res_file,FILENAME):
    fig = plt.figure(1,frameon=False, dpi=600)
    fig.add_axes([0, 0, 1, 1])

    m = Basemap(resolution="h",projection='laea', lat_ts=90, lat_0=90., lon_0=0.,
                llcrnrlon= 131.7520359690613, llcrnrlat= 79.649075580926876 ,
                urcrnrlon= 133.09583606755186, urcrnrlat= 68.671528061194962)

    fast = np.load(FILENAME)
    m.imshow(fast)
    
    #m.drawcoastlines()
    m.fillcontinents( color='0.8', lake_color='0.8' ) #color='#FFEC8B')
    #m.drawmeridians(np.arange(110.,150.,10.),labels=[1, 0, 0, 0])
    #m.drawparallels(np.arange(70.,80.,5.),labels=[1, 0, 0, 0])
    #m.drawmapboundary(fill_color='#6587ad', linewidth=0.0)
    
    #colorbar settings
    colors = ['white', '#cc0000']
    cmap = mpl.colors.ListedColormap(colors)
    bounds = [-5.,50.,105.]
    bounds = map(lambda x : x / 100., bounds)
    #print bounds
    norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
    
    img = m.imshow(fast,cmap=cmap, norm=norm)
    
    #cbar = plt.colorbar(img, cmap=cmap, norm=norm, boundaries=bounds,ticks=np.linspace(0,100,11))
    plt.title( FILENAME[-11:-7] + "." + FILENAME[-7:-5] + "." + FILENAME[-5:-3], fontsize = 20)
    #cbar.set_ticklabels(range(0,110,10))
    #plt.show()    
    plt.savefig(res_file+'.pdf', pad_inches=0.0, bbox_inches='tight')
    fig.clear()

    
#years = np.arange(2011,2013,1)
def some_old_func():
    months = np.arange(1,13,1)
    for month in months:
        print month
        flist = np.array(glob.glob(os.path.join(INDIR+str(month)+'\\', '*')))
        
        for j in range(len(flist)):
            
            create_map(OUTDIR+str(month)+'\\',flist[j])
    #        plt.colorbar()
            #plt.savefig(OUTDIR+flist[j][-10:]+'.pdf', pad_inches=0.0, bbox_inches='tight')
            #plt.savefig(OUTDIR+flist[j][-10:]+'.pdf')
def some_new_func():
    files = glob.glob(os.path.join(INDIR, '*'))
    files.sort()
    res_files = map( lambda x : str.format( OUTDIR + "m-{}", x), range(0, len(files), 1))
    for fi, fo in zip( files, res_files ):
        create_map(fo, fi)

#20011003_lm  20011024_lm  20011121_lm  20011212_lm  20020710_lm  20020731_lm
#20011010_lm  20011031_lm  20011128_lm  20011219_lm  20020716_lm
#20011017_lm  20011114_lm  20011205_lm  20020703_lm  20020724_lm

some_new_func()