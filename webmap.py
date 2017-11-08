import folium

map = folium.Map(location=[48.725147, 19.569057], zoom_start=8, tiles='Stamen Terrain')

folium.GeoJson(open('custom.geo.json').read()).add_to(map)

folium.CircleMarker(location=[49.194906, 21.147435], radius=6, fill_color='green',
    popup='Rezervacia Vlcia').add_to(map)

map.save('mapa.html')
