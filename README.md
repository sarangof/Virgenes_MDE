# Las Vírgenes del Metro de Medellín

Mapa interactivo de las representaciones artísticas de la Virgen María en las estaciones del Metro de Medellín.

## Sobre el proyecto

El área de Cultura del Metro de Medellín facilitó al [Instituto Edgelands](https://www.edgelands.institute/) información sobre el proyecto de arte público Las Vírgenes del Metro. El Instituto Edgelands produjo este mapa en retribución, esperando que sea de servicio y agrado a la ciudadanía.

## Contexto

Fueron los primeros años de la Cultura Metro, una propuesta educativa y de gestión social y cultural con la que fue posible aportar al sentido de pertenencia por lo propio, a la cohesión social y a la creación de nuevos imaginarios que le brindaron la posibilidad de reinvención a una ciudad que estaba sitiada por la violencia del narcotráfico.

En ese entorno de crisis social y económica, el proyecto Metro de Medellín ayudó a recobrar la confianza y el primer vagón que comenzó a rodar no fue por obra de la ingeniería, sino de la cultura, y en ese vagón viajaron juntos: ciudadanía, sociedad civil, empresa privada y gobierno.

Ante este contexto, el Metro de Medellín comprendió que la vida se protegía si la sociedad permanecía unida, y que el mayor blindaje que podía tener la infraestructura pública era el acompañamiento social. Y para generar apropiación e identificación cultural, el Metro construyó un proyecto expositivo de obras de arte en las estaciones del sistema. Las primeras cuatro obras fueron instaladas en el año 1996, dando inicio a la serie que más tarde se conocería con el nombre de Las Vírgenes del Metro, que hoy suman veintidós. La instalación de obras de esta temática estuvo condicionada por su valor simbólico para la sociedad antioqueña. No se trataba de una exposición de obras para la devoción, sino para la admiración.

La curaduría estuvo encomendada al pintor, ilustrador y diseñador Humberto Pérez, quien expresó la importancia que tendrían las obras como protección a la infraestructura, no por efectos sobrenaturales, sino por el respeto a la imagen de la Virgen. Humberto Pérez invitó a distintos artistas a participar del proyecto con producciones originales y gestionó los permisos de reproducción de otras obras existentes.

Esta Galería de Arte Público está disponible para el disfrute de toda la ciudadanía, pues no es necesario ingresar al sistema para apreciar las obras. Quien decida hacer un recorrido va a encontrar diversas advocaciones de la Virgen, con una representación cultural cercana a nuestra realidad y en algunos casos juguetona, plasmadas a través de distintas técnicas: murales al fresco, mosaico, relieve en cemento, acrílico sobre lienzo, grabado en metal, cerámica, óleo sobre madera, entre otros.

*Carlos Mario Jiménez H., Área de Gestión Social, Metro de Medellín*

## Estructura del repositorio

```
index.html                  Visualización interactiva (página principal)
Virgenes/Originales/        Fotografías de las obras originales
Virgenes/Procesadas/        Imágenes simplificadas para los íconos del mapa
Virgenes_detalles.csv       Datos de cada obra (estación, artista, técnica, año, detalles)
Lineas_metro.geojson        Trazado geográfico de las líneas del Metro
virgin_map.py               Script original en Python (Folium) para generar el mapa
```

## Visualización

La visualización está disponible en: **https://sarangof.github.io/Virgenes_MDE/**

Es un archivo HTML autocontenido con un mapa interactivo (Leaflet) donde cada estación del Metro muestra un ícono con la imagen simplificada de la virgen correspondiente. Al hacer clic se despliega la fotografía de la obra original junto con la información del artista, la técnica y detalles históricos. Debajo del mapa hay un listado de todas las obras ordenadas según el recorrido de las líneas del Metro.

## Créditos

Información y contenido: Área de Cultura, Metro de Medellín.

Producción del mapa: [Instituto Edgelands](https://www.edgelands.institute/).