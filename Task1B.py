from floodsystem.geo import stations_by_distance
from floodsystem.utils import sorted_by_key
from floodsystem.stationdata import build_station_list
def run():
    stations = build_station_list()
    Unsorted_Data = stations_by_distance(stations, (52.2053, 0.1218))
    Sorted_Data = sorted_by_key(Unsorted_Data, 1)

    # probably we need to integrate the sort in the stations_by_distance function

    def List_Create(Sorted_Data, Stations, reverse=False, p=0, q=0, Town=0):
        blankList = []
        if reverse:
            p = len(stations) - 10
            q = len(stations)
        if reverse == False:
            p = 0
            q = 10
        for i in range(p, q):
            name = Sorted_Data[i][0]
            distance = Sorted_Data[i][1]
            for j in range(0, len(stations)):
                if stations[j].name == name:
                    Town = stations[j].town
            temp_element = (name, Town, distance)
            blankList += [temp_element]
        return blankList
    # can we just calculate the distance of all stations and extract out using
    # x[:10] (closest) and x[-10:] (farthest)?

    print("the nearest 10 stations are:", List_Create(Sorted_Data, stations))
    print("the furthest 10 stations are:", List_Create(Sorted_Data, stations, reverse=True))

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()



