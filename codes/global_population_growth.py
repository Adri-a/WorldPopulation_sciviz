import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from prep_population import select_population

population = select_population(1300, 2022)

plt.rcParams["figure.figsize"] = (12, 4.5) # proporzioni di schermo 16:9

fig, ax = plt.subplots()

growth_values = np.append([0], np.array([np.exp(np.diff(np.log(population['PopTotal']))) - 1]))
population['growth'] = np.multiply(growth_values, 100)
pop_2 = population.copy()
pop_2.drop('PopTotal', axis=1, inplace=True)
pos_growths = pop_2.copy()
neg_growths = pop_2.copy()

pos_growths[pos_growths < 0] = np.nan
neg_growths[neg_growths > 0] = np.nan

ax.bar(pos_growths.index, pos_growths.growth, width=2)
ax.bar(neg_growths.index, neg_growths.growth, width=2, color='r')
ax.axhline(color='grey', linewidth=0.75)

ax.set_xbound(1350, 2022)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.title('Crescita popolazione mondiale, 1300-2022', loc='left')
ax.set_xlabel('Anno', size=11)
ax.set_ylabel('% Crescita', size=11)

'''
a = np.polyfit(population.index, population.growth, 7)
p = np.poly1d(a)
ax.plot(population.index, p(population.index))
'''
plt.show()