import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from prep_population import select_population
import matplotlib.ticker as ticker

def y_format(x, pos):
    x = x / 10**9
    tick = "%.1f" % x
    return tick

pop_prevista_high = select_population(2022, 2100, 'High')
pop_prevista_medium = select_population(2022, 2100, 'Medium')
pop_prevista_low = select_population(2022, 2100, 'Low')

plt.rcParams["figure.figsize"] = (7, 4.5)
fig, ax = plt.subplots()

ax.plot(pop_prevista_medium, linestyle='--', label=None)
ax.plot(pop_prevista_high, color='#1f77b4', linewidth=0.5)
ax.plot(pop_prevista_low, color='#1f77b4', linewidth=0.5)
ax.fill_between(pop_prevista_medium.index, pop_prevista_low.PopTotal, pop_prevista_high.PopTotal, alpha=0.25)

max_point = pop_prevista_medium.loc[pop_prevista_medium['PopTotal'].eq(pop_prevista_medium['PopTotal'].max())]

ax.plot(max_point, 'ro', label='Popolazione massima')
ax.legend(loc='upper left')
# print(max_point.iloc[0])

ax.yaxis.set_major_formatter(ticker.FuncFormatter(y_format))
ax.set_title('Popolazione mondiale, previsioni fino al 2100', loc='left', size=16)
ax.set_xlabel('Anno', size=13)
ax.set_xbound(2022, 2100)
ax.set_ylabel('Abitanti (in miliardi)', size=13)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

plt.show()