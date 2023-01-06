import geopandas as gpd
import pandas as pd
import numpy as np
from branca.colormap import linear
import folium
from folium.plugins import TimeSliderChoropleth

#GET WORLD SHAPES

assert "naturalearth_lowres" in gpd.datasets.available
datapath = gpd.datasets.get_path("naturalearth_lowres")
gdf = gpd.read_file(datapath)
gdf["pop_est"] = gdf["pop_est"].astype(int)

#GET WORLD DATA

world = pd.read_csv("datasets/HeatMapData.csv", low_memory=False)

#preserve original population
world['PopNotScaled'] =  world["PopTotal"]*1000
world['PopNotScaled'] =  world["PopNotScaled"].astype(int)
world['PopNotScaled'] = world.apply(lambda x: "{:,}".format(x['PopNotScaled']), axis=1)

#Scale
world["PopTotal"] = world["PopTotal"]/1000
world["PopTotal"] = world["PopTotal"].astype(int)

#getting right time format
world['Time']  = world['Time'].astype(str) + '-1-1'
world['date_sec'] = pd.to_datetime(world['Time']).astype(np.int64) / 10**9
world['date_sec'] = world['date_sec'].astype(int)

#GET DICTONARY

styledata = {}

for country in gdf.index:

    iso3 = gdf.iloc[country][3]
    state = world[world['ISO3_code'] == iso3]
    pop = state['PopTotal'].values

    df = pd.DataFrame(
        {
            "color": pop,
            "opacity": 0.7,
        },
        index=state['date_sec'],
    )
    styledata[country] = df

#SET COLORS

max_color, min_color = 0, 0

for country, data in styledata.items():
    max_color = max(max_color, data["color"].max())
    min_color = min(max_color, data["color"].min())

cmap = linear.Reds_09.scale(min_color, max_color)

for country, data in styledata.items():
    data["color"] = data["color"].apply(cmap)
    data["opacity"] = data["opacity"]

#CREATE MAP

styledict = {
    str(country): data.to_dict(orient="index") for country, data in styledata.items()
}

m = folium.Map(min_zoom=2, max_bounds=True, tiles="cartodbpositron")

g = TimeSliderChoropleth(
    gdf.to_json(),
    styledict=styledict,
).add_to(m)

_ = cmap.add_to(m)
cmap.caption = "World Population by State"

for country in gdf.index:

    iso3 = gdf.iloc[country][3]
    state = world[(world['ISO3_code'] == iso3) & (world['Time'] == '2022-1-1')]

    if not state.empty:
        pop = state.iloc[0]['PopNotScaled']
        gdf.at[country,'pop_est'] = pop
    else:
        gdf.at[country,'pop_est'] = float('NaN')


style_function = lambda x: {'weight':0.5, 
                            'color':'white',
                            'fillOpacity':0}

folium.features.GeoJson(
        gdf.to_json(),
        name='World Population 2022',
        style_function=style_function,
        tooltip=folium.features.GeoJsonTooltip(fields=['name','pop_est'], labels=True)
    ).add_to(m)

m.save('TimeSliderChoropleth.html')