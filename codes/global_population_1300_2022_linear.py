import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from prep_population import select_population

summed = select_population(1300, 2022, 'Medium')
# disegno grafico

plt.rcParams["figure.figsize"] = (16, 9) # proporzioni di schermo 16:9
fig, ax = plt.subplots()

ax.plot(summed.index, summed["PopTotal"], marker='o', markersize=4)
ax.ticklabel_format(useOffset=False, style='plain', useLocale=True)

ax.axhline(8*(10**9), color='red', linewidth=1)
for i in range (1*10**9, 8*10**9, 1*10**9):
    ax.axhline(i, color='grey', linewidth=1, alpha=0.25)

ax.set_title("Popolazione mondiale 1300-2022", loc='left', size=18)
ax.set_xlabel("Anno", size=13)
ax.set_ylabel("Abitanti", size=13)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)


ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
# ax.yaxis.set_major_formatter(ticker.ScalarFormatter())
ax.get_yticklabels()[8].set_color('red')
ax.set_xbound(1300, 2025)
plt.show()