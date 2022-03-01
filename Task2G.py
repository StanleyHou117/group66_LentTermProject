from floodsystem.riskwarning import risktest
from floodsystem.stationdata import build_station_list

def run():
    '''printing out the name of the stations at each risk level'''
    stations = build_station_list()
    towns_l, towns_m, towns_h, towns_s = risktest(stations)
    #print(type(towns_l))
    print("Towns having severe risk of flooding \n", towns_s)
    print("Towns having high risk of flooding \n", towns_h)
    print("Towns having moderate risk of flooding \n", towns_m)
    print("Towns having low risk of flooding \n", towns_l)


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
