'''Unit test for geo module'''
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number
from floodsystem.station import MonitoringStation

# in case that the real data are always changing, we tend to use a set of static data we create as below
s_id1 = "test_s_id1"
m_id1 = "test_m_id1"
label1 = "station1"
coord1 = (0.0, 1.0)
trange1 = (3.4, 1.2)
river1 = "x1"
town1 = "a1"

s_id2 = "test_s_id2"
m_id2 = "test_m_id2"
label2 = "station2"
coord2 = (0.0, 0.0)
trange2 = (0.4, 1.2)
river2 = "x2"
town2 = "a2"

s_id3 = "test_s_id3"
m_id3 = "test_m_id3"
label3 = "station3"
coord3 = (2.0, 0.0)
trange3 = (10, 2.4)
river3 = "x3"
town3 = "a3"

a = MonitoringStation(s_id1, m_id1, label1, coord1, trange1, river1, town1)
b = MonitoringStation(s_id2, m_id2, label2, coord2, trange2, river2, town2)
c = MonitoringStation(s_id3, m_id3, label3, coord3, trange3, river3, town3)
test_stations = [a, b, c]

def test_stations_by_distance():
    stations = test_stations
    result = stations_by_distance(stations)
    assert type(result) == list
    assert type(result[0]) == tuple
    assert result == [('station1', 5805.544860297416), ('station2', 5804.975668111422), ('station3', 5582.586125587015)]

def test_stations_within_radius():
    stations = test_stations
    result = stations_within_radius(stations, (0.0,0.0), 0.1)
    assert type(result) == list
    assert result[0] == 'station2'

def test_rivers_with_stations():
    stations = test_stations
    result = rivers_with_station(stations)
    assert type(result) == set
    assert result == {'x2', 'x3', 'x1'}

def test_stations_by_number():
    stations_river = stations_by_river(test_stations)
    assert stations_river == {"x3": ["station3"], "x2": ["station2"], "x1": ["station1"]}

def test_rivers_by_station_number():
    temp_list = rivers_by_station_number(test_stations, N = 3)
    assert sorted(temp_list, key = lambda tup:tup[0], reverse = True) == [("x3", 1), ("x2", 1), ("x1", 1)]


