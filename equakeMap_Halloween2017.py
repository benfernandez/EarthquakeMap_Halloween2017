import folium
import pandas
from folium.plugins import FloatImage



df= pandas.read_csv("equake_10_31_2017.csv")

lat=list(df["latitude"])
lon=list(df["longitude"])
magnitude=list(df["mag"])

pumpImage = ('pumpkinIcon.png')

def magColorChanger(magnitude):
    if magnitude <= 1.0:
        return 'green'
    elif 1.0 < magnitude <= 4.0:
        return 'orange'
    elif magnitude > 4.0:
        return 'red'

legend =   '''
                <div style="position: fixed;
                            bottom: 50px; left: 50px; width: 220px; height: 75px;
                            border:2px solid grey; z-index:9999; font-size:16px;
                            ">&nbsp; Green: mag < 1.0  <br>
                              &nbsp; Orange: 1.0 < mag < 4.0 &nbsp;<br>
                              &nbsp; Red: mag > 4.0 &nbsp;<br>

                </div>
                '''
map = folium.Map(location=[38.889931,-77.009003],zoom_start=5,tiles="stamenterrain")

FloatImage(pumpImage,bottom=5,left=90).add_to(map)

fgquake = folium.FeatureGroup(name="Earthquakes 10_31_2017")

for la,ln,ma in zip(lat,lon,magnitude):
    fgquake.add_child(folium.CircleMarker(location=[la,ln],radius = 8,popup="magnitude is: " +str(ma),fill_color=magColorChanger(ma),
    color='grey',fill_opacity=.6,fill=True))


map.add_child(fgquake)
map.get_root().html.add_child(folium.Element(legend))
map.save("EQMap_Hween2017.html")
