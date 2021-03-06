from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level

def run():
    stations = build_station_list()
    warning_stations = stations_highest_rel_level(stations,10)
    for entry in warning_stations:
        print(entry[0].name,entry[1])



if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()