from floodsystem.stationdata import update_water_levels

def risktest(stations):
    '''This function manually set up several ranges for the risk levels.'''
    update_water_levels(stations)
    towns_s = set()
    towns_h = set()
    towns_m = set()
    towns_l = set()
    for station in stations:
        rel_level = station.relative_water_level()
        if rel_level is None:
            pass
        elif rel_level > 0.8 and rel_level < 1.0 and station.town is not None:
            towns_l.add(station.town)
        elif rel_level > 1.0 and rel_level < 1.2 and station.town is not None:
            towns_m.add(station.town)
        elif rel_level > 1.2 and rel_level < 1.6 and station.town is not None:
            towns_h.add(station.town)
        elif rel_level > 1.6 and station.town is not None:
            towns_s.add(station.town)
    return towns_l, towns_m, towns_h, towns_s
#more precise testing can be introduced if more modules are added such as weather forecast and geographical factors.
#However, it might not be feasible in this project, so a simple criteria based on the given modules is used.
