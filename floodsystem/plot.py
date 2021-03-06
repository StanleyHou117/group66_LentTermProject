import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.analysis import polyfit
from matplotlib.dates import date2num

def plot_water_levels(station, dates, levels):
    plt.plot(dates, levels)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    #plot typical high/low
    typical_low = []
    typical_high = []
    for i in range(0, len(dates)):
        typical_low.append(station.typical_range[0])
        typical_high.append(station.typical_range[1])
    plt.plot(dates, typical_low, label = "Typical Low")
    plt.plot(dates, typical_high, label = "Typical High")

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    plt.plot(dates, levels, label = "measured water levels")

    lsf_poly, offset = polyfit(dates,levels,p)
    print(lsf_poly,offset,station.name)
    plt.plot(dates, lsf_poly(date2num(dates)-offset), label="LSF prediction")

    typical_low = []
    typical_high = []
    for i in range(0, len(dates)):
        typical_low.append(station.typical_range[0])
        typical_high.append(station.typical_range[1])
    plt.plot(dates, typical_low, label = "typical low")
    plt.plot(dates, typical_high, label = "typical high")

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.legend()

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.show()