from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit
import datetime

def run():
    stations = build_station_list()
    dt = 2
    data = stations_highest_rel_level(stations, 5)

    for entry in data:
        dates, levels = fetch_measure_levels(entry[0].measure_id, dt=datetime.timedelta(days=dt))
        if len(dates) != 0:
            plot_water_level_with_fit(entry[0], dates, levels, 4)


if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()