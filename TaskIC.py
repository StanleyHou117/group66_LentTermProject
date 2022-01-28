#this file is to test the added item in class MonitoringStation
from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

#all distance quantities are in kilometres
stations = build_station_list()
Stations_Within_10 = stations_within_radius(stations,(52.2053,0.1218),10)
print(Stations_Within_10)

'''what does it mean by a list of all stations(Type MonitoringStation)???'''