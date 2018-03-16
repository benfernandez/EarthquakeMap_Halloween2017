import folium
import pandas

df= pandas.read_csv("equake_10_31_2017.csv")

lat=list(df["latitude"])
lon=list(df["longitude"])
