# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.utils import sorted_by_key  # noqa
import math
from floodsystem.stationdata import build_station_list
#Task 1B
def stations_by_distance(stations, p = (0,0)):
    '''This function returns a list includes the distance between the monitoring stations
        to point p and their corresponding names'''
    list_Tuple = []
    R = 6371
    for i in range (0,len(stations)):
        distance = 0
        # all units should be kilometers
        dLat = (stations[i].coord[0] - p[0]) * math.pi / 180.0
        dLon = (stations[i].coord[1] - p[1]) * math.pi / 180.0
        a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(stations[i].coord[0] * math.pi / 180.0) * \
            math.cos(p[0] * math.pi / 180.0) * math.sin(dLon / 2) * math.sin(dLon / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        # distance calculated via haversine formula
        distance = R * c
        temp_tuple = (stations[i].name, distance)
        list_Tuple += [temp_tuple]
        i += 1
    return sorted_by_key(list_Tuple,1,True)

# i mean integrating the above 3 lines into stations_by_distance function.


#task 1C Adding geographical information into the class MonitoringStation
def stations_within_radius(stations, centre = (0.0,0.0), r=0):
    '''This function find out the stations' names within a distance r from the given centre'''
    temp_List_Distance = stations_by_distance(stations, centre)
    Closestation = []
    for i in range(0, len(stations)):
        if temp_List_Distance[i][1] <= r:
            Chosen_Name = temp_List_Distance[i][0]
            Closestation += [Chosen_Name]
    return sorted(Closestation)

#task 1D i)
def rivers_with_station(stations):
    '''This function returns a set of river's name corresponding to the given station '''
    temp_list = []
    for i in range (0,len(stations)):
        temp_list += [stations[i].river]
    temp_set = set(temp_list)
    return temp_set

#task 1D ii)
def stations_by_river(stations):
    '''This function maps the river names to lists of stations'''
    temp_dict = {}
    river_list = [key for key in rivers_with_station(stations)]
    length = len(river_list)
    for i in range (0, length):
        temp_list_name = []
        for j in range (0,len(stations)):
            if stations[j].river == river_list[i]:
                temp_list_name += [stations[j].name]
            temp_dict[river_list[i]] = temp_list_name
    return temp_dict

#task 1E
def rivers_by_station_number(stations, N=0):
    '''This function returns a sorted list of the N rivers with the greatest number of monitoring stations.'''
    temp_list = []
    dict_data = stations_by_river(stations)
    list_river = [key for key in dict_data]
    for i in range (0, len(list_river)):
        temp_tuple = (list_river[i], len(dict_data[list_river[i]]))
        temp_list += [temp_tuple]
    sorted_list = sorted(temp_list, key = lambda tup: tup[1], reverse= True)

    length = len(sorted_list)
    j = length-1
    while j >= N:
        if sorted_list[N][1] == sorted_list[j][1]:
            return sorted_list [:j]             #return the required list to end the function
        j -= 1

    #the codes below can generate lists with same number of stations
    # dict_sorted = {}
    # for j in range (1, sorted_list[0][1]+1):
    #     times = 0
    #     temp_list = []
    #     for k in range (0, len(sorted_list)):
    #         if sorted_list[k][1] == j:
    #             temp_list += [sorted_list [k][0]]
    #             times += 1
    #     if times > 1:
    #         dict_sorted[j] = temp_list
    #     elif len(temp_list) > 0:
    #         dict_sorted[j] = temp_list[0]
    # keys_data = [key for key in dict_sorted]
    # list_final = []
    # for k in range (0, len(dict_sorted)):
    #     temp_tuple = (dict_sorted[keys_data[k]], keys_data[k])
    #     list_final += [temp_tuple]
    #
    # list_final.reverse()
    # return list_final [:N]








