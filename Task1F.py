from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

def run():
    print(sorted(inconsistent_typical_range_stations(build_station_list())))
    print(len(inconsistent_typical_range_stations(build_station_list())))

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()