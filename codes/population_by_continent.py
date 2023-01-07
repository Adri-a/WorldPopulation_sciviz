import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io
import matplotlib.ticker as ticker

populationByContinent = pd.read_csv("populationByContinent - API_SP.POP.TOTL_DS2_en_csv_v2_4701113.csv")

labels = ["AFRICA", "AMERICA", "ASIA", "EUROPA", "OCEANIA"]
colors = ["dimgray", "firebrick", "gold", "forestgreen", "midnightblue"]
fig, ax = plt.subplots()

plt.stackplot(populationByContinent["Anni"],
              populationByContinent["AFRICA"],
              populationByContinent["AMERICA"],
              populationByContinent["ASIA"],
              populationByContinent["EUROPA"],
              populationByContinent["OCEANIA"],
              colors = colors)

plt.legend(labels = labels, loc = "upper left")
plt.title("Popolazione per Continente (1960-2021)", loc = "left")
plt.xlabel("Anni")
plt.ylabel("Popolazione")
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))

plt.show()

labels = ["AFRICA", "AMERICA", "ASIA", "EUROPA", "OCEANIA"]
fig, ax = plt.subplots()

plt.plot(populationByContinent["Anni"], populationByContinent["AFRICA"], "dimgray")
plt.plot(populationByContinent["Anni"], populationByContinent["AMERICA"], "firebrick")
plt.plot(populationByContinent["Anni"], populationByContinent["ASIA"], "gold")
plt.plot(populationByContinent["Anni"], populationByContinent["EUROPA"], "forestgreen")
plt.plot(populationByContinent["Anni"], populationByContinent["OCEANIA"], "midnightblue")

plt.legend(labels = labels, loc = "upper left")
plt.title("Popolazione per Continente (1960-2021)", loc = "left")
plt.xlabel("Anni")
plt.ylabel("Popolazione")
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))

plt.show()
