import numpy as np
import pandas as pd

def select_population(start, end):
    # anni 1950 - 2022
    population = pd.read_csv("datasets/WPP2022_TotalPopulationBySex.csv", \
        dtype = {'Notes' : str, 'ISO3_code' : str, 'ISO2_code' : str, 'LocTypeName' : str})

    # moltiplico per mettere tutto a sx della virgola
    population.PopTotal = np.multiply(population.PopTotal, 10**3)
    population.PopMale = np.multiply(population.PopMale, 10**3)
    population.PopFemale = np.multiply(population.PopFemale, 10**3)
    population = population.astype({'PopTotal' : 'int64'})

    if start >= 1950:
        return population.loc[start:end]
    
    # anni 1800 - 1950
    population_1800 = pd.read_csv("datasets/GM_PopulationV6_WorldData_ByYear_1800Forward.csv", \
        dtype={'geo' : str, 'name' : str, 'time' : np.int32, 'Population' : np.int64})

    # cambio nomi indice e colonna per adattarlo a quello che avrò dall'altro
    # (ovvero time -> Time e Population -> PopTotal)
    population_1800.drop(columns=['geo', 'name'], inplace=True)
    population_1800.rename(columns={'time' : 'Time', 'Population' : 'PopTotal'}, inplace=True)
    population_1800.set_index('Time', inplace=True)
    population_1800 = population_1800.loc[:1949]

    pop_valid = population[population['ISO3_code'].notna()]
    # interessano solo quelli con variant = Medium
    pop_valid = pop_valid[pop_valid['Variant'] == 'Medium']

    # crea nuovo dataframe, con time come index
    summed = pop_valid.groupby(["Time"])[['PopTotal']].sum()
    summed = summed.loc[:end]

    # concateno a summed i dati dal 1800 al 1949
    summed = pd.concat([population_1800, summed])

    if start >= 1800:
        return summed.loc[start:end]
    
    # anni 1300 - 1790 + concateno a summed
    population_1300 = pd.read_csv("datasets/Population_1300_to_1790.csv")
    population_1300.set_index('Time', inplace=True)
    summed = pd.concat([population_1300, summed])

    return summed.loc[start:end]