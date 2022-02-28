from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level
import datetime


def run():
    stations = build_station_list()
    dt = 10
    data = stations_highest_rel_level(stations, 5)
    #print(data)
    for entry in data:
        dates, levels = fetch_measure_levels(entry[0].measure_id, dt=datetime.timedelta(days=dt))
        print('The graph for ', entry[0].name, ' is printed')
        plot_water_levels(entry[0], dates, levels)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
