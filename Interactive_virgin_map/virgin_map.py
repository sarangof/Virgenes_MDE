import geopandas as gpd
import folium
import pandas as pd

# Load shapefile
gdf = gpd.read_file('/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Lineas_metro/Lineas_metro.shp')
detalles = pd.read_csv('/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Virgenes_detalles.csv',sep=';')
gdf = gdf.merge(detalles, on='ESTACION', how='left')

# Dictionary mapping station names to image paths
station_to_original_image = {
    'ACEVEDO': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Originales/Acevedo.png',
    'AGUACATALA': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Originales/Aguacatala.png',
    'AYURA': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Originales/Ayura.png',
    'BELLO': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Originales/Bello.png',
    'CARIBE': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Originales/Caribe.png',
    'CISNEROS': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Originales/Cisneros.png',
    'ENVIGADO': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Originales/Envigado.png',
    'ESTADIO': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Originales/Estadio.png',
    'FLORESTA': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Originales/Floresta.png',
    'HOSPITAL': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Originales/Hospital.png',
    'INDUSTRIALES': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Originales/Industriales.png',
    'ITAGUÍ': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Originales/Itaguí.png',
    'MADERA': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Originales/Madera.png',
    'PARQUE BERRÍO': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Originales/Parque_Berrío.png',
    'POBLADO': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Originales/Poblado.png',
    'PRADO': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Originales/Prado.png',
    'SAN ANTONIO': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Originales/San_Antonio_B.png',
    'SAN JAVIER': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Originales/San_Javier.png',
    'SURAMERICANA': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Originales/Suramericana.png',
    'TRICENTENARIO': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Originales/Tricentenario.png',
    'UNIVERSIDAD': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Originales/Universidad.png'
    # Add more stations and image paths as needed
}

station_to_image = {
    'ACEVEDO': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Procesadas/Acevedo.png',
    'AGUACATALA': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Procesadas/Aguacatala.png',
    'AYURA': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Procesadas/Ayura.png',
    'BELLO': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Procesadas/Bello.png',
    'CARIBE': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Procesadas/Caribe.png',
    'CISNEROS': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Procesadas/Cisneros.png',
    'ENVIGADO': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Procesadas/Envigado.png',
    'ESTADIO': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Procesadas/Estadio.png',
    'FLORESTA': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Procesadas/Floresta.png',
    'HOSPITAL': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Procesadas/Hospital.png',
    'INDUSTRIALES': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Procesadas/Industriales.png',
    'ITAGUÍ': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Procesadas/Itaguí.png',
    'MADERA': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Procesadas/Madera.png',
    'PARQUE BERRÍO': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Procesadas/Parque Berrío.png',
    'POBLADO': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Procesadas/Poblado.png',
    'PRADO': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Procesadas/Prado.png',
    'SAN ANTONIO': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Procesadas/San Antonio B.png',
    'SAN JAVIER': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Procesadas/San Javier.png',
    'SURAMERICANA': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Procesadas/Suramericana.png',
    'TRICENTENARIO': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Procesadas/Tricentenario.png',
    'UNIVERSIDAD': '/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Vírgenes/Procesadas/Universidad.png'
    # Add more stations and image paths as needed
}

# Initialize map centered at median coordinates with a "sober" basemap
map_center = [gdf.geometry.y.median(), gdf.geometry.x.median()]
m = folium.Map(location=map_center, zoom_start=12, tiles='Stamen Terrain', attr='Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, Imagery © <a href="http://stamen.com">Stamen Design</a>')

lineas_transporte = gpd.read_file('/Users/sarangof/Documents/Personal/Edgelands/Art_visualizations/MDE_art_book/Corredores_para_Transporte_de_Pasajeros/Corredores_para_Transporte_de_Pasajeros.shp')        
folium.GeoJson(
    lineas_transporte,
        style_function=lambda feature: {
        'color': 'gray',  # Line color
        'weight': 0.5  # Line width
    }
).add_to(m) 

# Add markers with custom icons and hover information
for _, row in gdf.iterrows():
    # Get station name
    station = row['ESTACION']
    # Get corresponding image path from the dictionary
    icon_url = station_to_image.get(station, None)
    original_image_path = station_to_original_image.get(station, None)
    if icon_url:
        # Add marker with custom icon and hover information
        folium.Marker(
            location=[row.geometry.y, row.geometry.x],
            #marker_size = (32,32),
            icon=folium.CustomIcon(icon_url, icon_size=(32, 32)),
            tooltip=f'<div style="width: 200px; padding-top:0px; padding-bottom:0px">'
                f'<div style="text-align: center; padding-top:0px; padding-bottom:0px"><b>{row["ESTACION"]}</b></div><br>'
                f'<div style="text-align: center;padding-top:0px; padding-bottom:0px">' 
                f'<img src='+original_image_path+' alt="Image" style="width:100px; padding-top:0px; padding-bottom:5px"><br>'
                f'</div>'  # Close div for centered image
                f'{row["Título"]}<br>'  
                f'{row["Artista"]}, {row["Año"]}<br>' 
                f'{row["Técnica"]}<br>'  
                f'<div style="text-align: left;" white-space: nowrap; overflow: hidden; text-overflow: ellipsis;>{row["Detalles"]}</div><br>'
                f'</div>'  # Close div for tooltip 
        ).add_to(m)
    else:
        folium.CircleMarker(
            location=[row.geometry.y, row.geometry.x],
            tooltip=row['ESTACION'],  # Display station name on hover
            color='gray',  # Marker color
            fill=True,
            fill_color='gray',  # Marker fill color
            fill_opacity=0.8,  # Marker fill opacity
            radius=0.7  # Marker size
        ).add_to(m)

# Show map


m.save('./virgenes_metro.html')