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
def stations_by_distance(stations, p = (52.2053,0.1218)):
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
    return list_Tuple

stations = build_station_list()
distance_List = stations_by_distance(stations)
sorted_List = sorted_by_key(distance_List,1,True)

#task 1C Adding geographical information into the class MonitoringStation
def stations_within_radius(stations, centre = (0.0,0.0), r=0):
    temp_List_Distance = stations_by_distance(stations, centre)
    Closestation = []
    for i in range(0, len(stations)):
        if temp_List_Distance[i][1] <= r:
            Chosen_Name = temp_List_Distance[i][0]
            Closestation += [Chosen_Name]
    return Closestation