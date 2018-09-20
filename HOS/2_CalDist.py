import pandas as pd
import numpy as npy
import geopy

#Load
hos = pd.read_csv('/Users/jiangna/Desktop/hos_with_coor.csv')
work = pd.read_csv('/Users/jiangna/Desktop/work_with_coor.csv')

#get coord
workcors = work.loc[:,'Coord']
hoscors = hos.loc[:,'Coord']

#To LIST
hoscorlist = hoscors['Coord'].tolist()
workcorlist = workcors['Coord'].tolist() 

#caculate distance
from geopy import distance
output =[]
hoscorlist_len = len(hoscorlist)
workcorlist_len = len(workcorlist)

for i in range(0,hoscorlist_len):
    dist = [distance.distance(hoscorlist[i], workcorlist[j]).km for j in range(0, workcorlist_len)]
    output.append(dist)

hosdis = pd.DataFrame(output)
hosdist = hosdis.T
hosdist['wrkID'] = work['wrkID']
hosdist.to_csv('/Users/jiangna/Desktop/hosdist.csv')