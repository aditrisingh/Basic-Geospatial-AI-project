import osmnx as ox
import geopandas as gpd
import matplotlib.pyplot as plt
place_name="New Delhi,India"
G=ox.graph_from_place(place_name,network_type='all')
green_spaces=ox.geometries_from_place(place_name,tags={'leisure': ['park','garden'],'landuse':['forest','grass']})
fig,ax=plt.subplots(figsize=(10,10))
green_spaces.plot(ax=ax,color='green')
plt.show()
plt.savefig("green_spaces_map.png")


