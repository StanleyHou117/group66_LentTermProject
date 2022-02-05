#this file is to test the added item in class MonitoringStation
from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
def run():
    # all distance quantities are in kilometres
    stations = build_station_list()
    print(stations_within_radius(stations, (52.2053, 0.1218), 10))

    '''what does it mean by a list of all stations(Type MonitoringStation)???'''
    # it says a list of all stations within radius r

    # simplified into one line (lollll), and modified to sort alphabetically.

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
