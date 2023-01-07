import numpy as np
import time

years = [i for i in range(1300,1700,100)]
years.extend(i for i in range(1700,1800,10))

nd = -9999.0

f = open("./Population_1300_to_1790.csv", "a")
f.write("Time,PopTotal")

st = time.time() # start time per ciclare su files

for year in years:
    source = "datasets/baseline/unzipped/"+ str(year) +"AD_pop/popc_"+ str(year) +"AD.asc"

    '''
    hdr = [linecache.getline(source, i) for i in range(1,7)]
    values = [float(h.split(" ")[-1].strip()) \
    for h in hdr]
    cols,rows,lx,ly,cell,nd = values
    xres = cell
    yres = cell * -1
    '''

    # print(source)
    grid = np.loadtxt(source, skiprows=6)

    tot_pop = 0
    for x in np.nditer(grid):
        if x != nd:
            tot_pop += x

    tot_pop = int(tot_pop)
    f.write(str(year) + "," + str(tot_pop))

et = time.time()
f.close()
elapsed_time = et - st
print("tempo in secondi:", elapsed_time) # lol, ci impiega due minuti, non male
