import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('datasets/tfr-by-gapminder_fertility_world_total.csv')
df.drop(['geo.name','indicator.name','geo','indicator'], axis=1, inplace=True)
df.rename(index={0 : 'TotalFertility'}, inplace=True)
df = df.transpose()
df['TotalFertility'] = df['TotalFertility'].str.replace(',', '.', regex=False).astype(np.float32)
df.index = pd.to_numeric(df.index)
# df['TotalFertility'] = pd.to_numeric(df['TotalFertility'])

df = df.loc[1900:2020]
df.loc[1956] = 5
df.loc[1958] = 5

pre_forties = df.loc[1900:1940]
forties = df.loc[1940:1950]
post_forties = df.loc[1950:2020]

plt.rcParams["figure.figsize"] = (16, 9)
fig, ax = plt.subplots()

ax.plot(pre_forties, color='#1f77b4', alpha=0.255)
ax.plot(forties, color='#1f77b4')
ax.plot(post_forties, color='#1f77b4', alpha=0.25)

ax.set_xticks([i for i in range(1900, 2020, 10)])

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

ax.set_title('Tasso di fertilità', loc='left', size=18)
ax.set_xlabel('Anno', size=13)
ax.set_ylabel('Figli per donna', size=13)

ax.set_xbound(1900, 2022)

plt.show()