'''Unit test for geo module'''
'''Due to the rapidly varying database, the tests below mainly focus on the types of returned elements and some
    typical contents, which are not likely to change in a short term, such as the data within Cambridgeshire. However
    there will still be a possibility that the test cannot undergo successfully because of the change in database.'''
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number

def test_stations_by_distance():
    stations = build_station_list()
    result = stations_by_distance(stations)
    assert type(result) == list
    assert type(result[0]) == tuple

def test_stations_within_radius():
    stations = build_station_list()
    result = stations_within_radius(stations, (52.2053, 0.1218), 10)
    assert type(result) == list
    assert result[0] == 'Bin Brook'

def test_rivers_with_stations():
    stations = build_station_list()
    result = rivers_with_station(stations)
    assert type(result) == set
    list_result = [key for key in result]
    assert sorted(list_result)[0] == 'Addlestone Bourne'

def test_stations_by_number():
    stations  = build_station_list()
    result = stations_by_river(stations)
    assert type(result) == dict
    assert type(result['Baguley Brook']) == list
    assert result['Baguley Brook']== ['Northern Moor']

def test_rivers_by_station_number():
    stations = build_station_list()
    result = rivers_by_station_number(stations, N = 1)
    assert type(result) == list
    assert type(result[0]) == tuple
