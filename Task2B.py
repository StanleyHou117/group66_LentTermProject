from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    stations = build_station_list()

    Threshold = 0.8
    flood_list = stations_level_over_threshold(stations,Threshold)
    for entry in flood_list:
        print(entry[0],entry[1])



if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()