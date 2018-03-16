import folium
import pandas
from folium.plugins import FloatImage



df= pandas.read_csv("equake_10_31_2017.csv")

lat=list(df["latitude"])
lon=list(df["longitude"])
magnitude=list(df["mag"])

pumpImage = ('pumpkinIcon.png')

map = folium.Map(location=[38.889931,-77.009003],zoom_start=5,tiles="stamentoner")

FloatImage(pumpImage,bottom=5,left=90).add_to(map)

fgquake = folium.FeatureGroup(name="Earthquakes 10_31_2017")

for la,ln,ma in zip(lat,lon,magnitude):
    fgquake.add_child(folium.Marker(location=[la,ln],popup=folium.Popup("magnitude is: " +str(ma)),icon=folium.Icon(color='orange')))

map.add_child(fgquake)

map.save("EQMap_Hween2017.html")
