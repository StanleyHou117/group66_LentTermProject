from matplotlib.dates import date2num
import numpy as np
import matplotlib.pyplot as plt

def polyfit(dates, levels, p):

    float_dates = []
    for entry in dates:
        float_dates.append(date2num(entry))
    
    dates_offset = float_dates[0]
    lsf_coeff = np.polyfit(float_dates - dates_offset, levels, p)
    lsf_eqn = np.poly1d(lsf_coeff)

    return(lsf_eqn, dates_offset)
