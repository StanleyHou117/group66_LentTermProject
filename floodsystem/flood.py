from floodsystem.station import MonitoringStation
from floodsystem.utils import sorted_by_key
from floodsystem.stationdata import update_water_levels

def stations_level_over_threshold(stations, tol):
    update_water_levels(stations)
    result_list = []
    for entry in stations:
        if not entry.relative_water_level():
            pass
        elif entry.relative_water_level() > tol:
            result_list.append((entry.name, entry.relative_water_level()))

    result_list = sorted_by_key(result_list,1,True)
    return result_list
