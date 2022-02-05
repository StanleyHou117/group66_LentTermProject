#this file is to test the added item in class MonitoringStation
from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

#all distance quantities are in kilometres
print(sorted(stations_within_radius(build_station_list(),(52.2053,0.1218),10)))

'''what does it mean by a list of all stations(Type MonitoringStation)???'''
# it says a list of all stations within radius r

# simplified into one line (lollll), and modified to sort alphabetically.