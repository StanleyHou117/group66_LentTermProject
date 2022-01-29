from floodsystem.geo import rivers_with_station

#list_geo =  rivers_with_station()
#print(list_geo)
#print(type(list_geo))
#print(len(list_geo))
#for i in range (0, len(list_geo)):
 #   for j in range (0, len(list_geo)):
   #     list_lll = [key for key in list_geo]
    #    if list_lll [i] == list_lll [j] and i != j:
     #       print("repetition")

# some testing during programming, please ignore



#first test:
'''temp_set = rivers_with_station()
temp_list = [key for key in temp_set]       #creating the list
sorted_list = sorted(temp_list)             #sorted in alphabetical order
print(sorted_list)
First_ten = []
for i in range (0,10):
    First_ten = sorted_list[0:10]
print(len(sorted_list),"stations, First 10: ", First_ten)
'''
#the problem in this programme is that the river's actual names, whose fullnames starting with "river", are not included in the sorting.
#to fix it:

def exclude_river(raw_list):
    for i in range (0, len(raw_list)):
        if str(raw_list[i])[0:5] == 'River':
            raw_list[i] = str(raw_list[i])[6:len(raw_list[i])]
    return raw_list

temp_set = rivers_with_station()
temp_list = [key for key in temp_set]       #creating the list
temp_list = exclude_river(temp_list)
sorted_list = sorted(temp_list)             #sorted in alphabetical order
First_ten = []
for i in range (0,10):
    First_ten = sorted_list[0:10]
print(len(sorted_list),"stations, First 10: ", First_ten)

#secondtest
from floodsystem.geo import stations_by_river
dict_river = stations_by_river()
print(sorted(dict_river['River Aire']))
print(sorted(dict_river['River Cam']))
print(sorted(dict_river['River Thames']))