import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from os import listdir
from matplotlib import ticker

def y_format(x, pos):
    x = x / 10**6
    tick = "%.1f" % x
    return tick

dir = 'datasets/Deaths_5x1'
composed_df = pd.DataFrame()
countries = []

for filename in listdir(dir):
    df = pd.read_table(dir + '/' + filename, skiprows=2, delim_whitespace=True)
    country = filename.split('.')[0]
    df['Country'] = country
    countries.append(country)
    composed_df = pd.concat([composed_df, df])

composed_df['Total'] = pd.to_numeric(composed_df['Total'], 'coerce')

summed = composed_df.groupby(composed_df['Year'])['Total'].sum()

print(max(summed))
pre_forties = summed.loc[1900:1940]
forties = summed.loc[1940:1950]
post_forties = summed.loc[1950:2010]

plt.rcParams["figure.figsize"] = (16, 9)
fig, ax = plt.subplots()

ax.plot(pre_forties, color='#1f77b4', alpha=0.255)
ax.plot(forties, color='#1f77b4')
ax.plot(post_forties, color='#1f77b4', alpha=0.25)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

ax.set_xticks([i for i in range(1900, 2010, 10)])
ax.set_xbound(1900, 2000)
ax.set_title('Numero morti in 53 Stati sviluppati', loc='left', size=18)
ax.set_xlabel("Anno", size=13)
ax.set_ylabel("Numero morti (in milioni)", size=13)

ax.yaxis.set_major_formatter(ticker.FuncFormatter(y_format))
plt.show()