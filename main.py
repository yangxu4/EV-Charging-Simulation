# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 16:08:04 2022
535 simulation project
@author: XU Yang
"""

import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import Polygon, Point
from data import *

rng1 = np.random.RandomState(42)
rng2 = np.random.RandomState(44)

#Defining the randomization generator
def polygon_random_points(poly, num_points):
    min_x, min_y, max_x, max_y = poly.bounds
    points = []
    while len(points) < num_points:
        random_point = Point([rng1.uniform(min_x, max_x), rng1.uniform(min_y, max_y)])
        if (random_point.within(poly)):
            points.append(random_point)
    return points


ev_set = []
for i in range(len(poly_set)):
    points =  polygon_random_points(poly_set[i], ev_num[i])
    ev_regional = []
    # save the EV coordinates in the 1st region
    for p in points:
        ev_regional.append([p.x, p.y])
    ev_regional = np.array(ev_regional)
    # Then save all the EV coordinates
    ev_set.append(ev_regional)

# np.savetxt("ev_locations.csv", ev_set, delimiter=",", fmt='%s')

# calculate distance
dist = []

for ev in ev_set:
    num_ev = ev.shape[0]
    for i in range(num_ev):
        for j in range(len(cs_num)):
            dist.append(np.sqrt((ev[i,0] - cs_locations[j][0])**2 + (ev[i,1] - cs_locations[j][1])**2))
dist = np.array(dist)

# rank the distances to CS for each EV
ranks = []
idx = []
for i in range(total_ev):
    sort = np.sort(dist[i * len(cs_num) : (i+1) * len(cs_num)])
    sort_idx = np.argsort(dist[i * len(cs_num) : (i+1) * len(cs_num)])
    ranks.append(sort) # each row contains the distance information for each EV
    idx.append(sort_idx) # each row contains the index of shortest CS for each EV 
    
# determine the likelihood using the sorted distances
p_dist = np.zeros((total_ev, len(cs_num)))
for j in range(total_ev):
    for i in range(0, 4):
        p_dist[j, idx[j][i]] = rng2.uniform(0.75, 0.95)
    for i in range(4, 8):
        p_dist[j, idx[j][i]] = rng2.uniform(0.65, 0.85)
    for i in range(8, 12):
        p_dist[j, idx[j][i]] = rng2.uniform(0.55, 0.75)
    for i in range(12, 16):
        p_dist[j, idx[j][i]] = rng2.uniform(0.45, 0.65)
    for i in range(16, 30):
        p_dist[j, idx[j][i]] = 0 # If the CS is too far, EV won't go there
        
# The integrated decision matrix
p_cs_num = 1 - 1 / (np.array(cs_num) + 1)
# p_final = p_dist + cs_num * rng2.uniform(0.0008, 0.0012)
p_final = p_dist * p_cs_num


# sorted_p = p_final.sort(axis=1)
sorted_p_idx = p_final.argmax(axis=1) # get the index of CS for each EV

count_ev = []
# count number of EVs for each CS
for i in range(len(cs_num)):
    count_ev.append(list(sorted_p_idx).count(i))
print(count_ev)

# calculate the ratio of EV and CS
ratio = np.array(count_ev) * (1 / (np.array(cs_num) + 1))
print(np.round(ratio, 2))

# atmp1 = [] #select 20% EVs from the total EVs
# # Simulation start
# for i in range(len(ev_set)):
#     atmp1.append(np.floor(ev_set[i].shape[0] * 0.2))
