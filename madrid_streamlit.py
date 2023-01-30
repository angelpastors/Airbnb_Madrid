# ------------LIBRERIAS----------------

import streamlit as st
import matplotlib as plt
import numpy as np
import pandas as pd
import seaborn as sns
import plotly_express as px
import requests
import folium
from folium.plugins import FastMarkerCluster
from streamlit_folium import st_folium
import leafmap.foliumap as leafmap
import plotly.graph_objects as go


# ----------CONFIGURACIÓN DE LA PÁGINA----------

st.set_page_config(page_title ="Madrid", layout = "centered")


# ----------DATAFRAME--------------

df = pd.read_csv("airbnb_anuncios.csv")


# -----------PREPROCESAMIENTO DATAFRAME-------------

df.drop(["name","id","host_name","last_review"], axis = 1, inplace = True)
df["reviews_per_month"].fillna(0, inplace = True)


# --------------APP----------------

# Utilizo este comando para cambiar el color de diferentes lugares de la página y el icono a pie de página.
st.markdown(
    """
    <style>
    .stApp {
        background-color: #ebd8d8
    }
    .css-6qob1r {
        background-color: #77224e
    }
    .st-ck{
        background-color: transparent
    }
    .css-18ni7ap {
        background-color: transparent
    }
    .st-ax {
        background-color: 
    }
    .css-629wbf {
        background-color: transparent
    }
    .css-1x8cf1d {
        background-color: transparent
    }

    
    footer {visibility: hidden;}
    footer:hover,  footer:active {
        color: #ffffff;
        background-color: transparent; 
    }
    footer:after {
        content:'🐈‍⬛'; 
        visibility: visible;
        display: block;
        position: relative;
        padding: 5px;
        top: 2px;
    }
    
    </style>
    """,
    unsafe_allow_html=True
)

# SIDEBAR

# Pongo la información de sidebar empleando codigo latex para poner el color del texto.
st.sidebar.markdown("$\color{#ffffff}{Autor:}$")
st.sidebar.markdown("$\color{#ffffff}{Ángel\hspace{2mm}Pastor\hspace{2mm}Sánchez}$")
st.sidebar.markdown("$\color{#ffffff}{Fecha:}$")
st.sidebar.markdown("$\color{#ffffff}{30/01/2023}$")
st.sidebar.write("-----")
directorio = ["Portada", "Información", "Proyecto", "Gráficos y análisis"]
seleccionar_direccion = st.sidebar.selectbox("$\color{#ffffff}{¿Qué\hspace{2mm}quieres\hspace{2mm}ver?}$", directorio)
if st.sidebar.button("*"):
    st.balloons()


# CUERPO CENTRAL
# Página de portada.
if seleccionar_direccion == "Portada":
    st.markdown("# **MADRID**")
    st.image("https://www.barnes-madrid.com/images/titres_personnalises/-titre-aze4T.jpg")
    st.caption("barnes-madrid.com")


# Página de información.
if seleccionar_direccion == "Información":

    # Establezco un título como encabezado de la página.
    st.title("Un vistazo a la ciudad")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Avenida_de_Monforte_de_Lemos_%28Madrid%29_06.jpg/1920px-Avenida_de_Monforte_de_Lemos_%28Madrid%29_06.jpg")
    st.caption("wikipedia.com")
    # Texto introductorio.
    st.header("Información")
    st.write("""Madrid es un municipio español, con categoría de villa, además de ser la capital del Estado. Su termino municipal es el más 
                poblado de España y es la segunda ciudad más poblada de Europa. Es un influyente centro cultural y cuenta con museos de referencia
                internacional. Los orígenes de la ciudad son objeto de revisión histórica tras los diferentes hallazgos realizados, pero quedando 
                claro que diferentes pueblos se asentaron en Madrid.""")
    st.header("Qué ver en Madrid")
    st.write("""Madrid es una de las ciudades más visitadas de nuestro país. Esto se debe a que es una ciudad realmente atractiva, cargada 
                de lugares para visitar, con una amplia oferta cultural y de ocio.""")
    # Sección Gran Vía.
    st.subheader("La Gran Vía")
    st.image("https://www.elplural.com/uploads/s1/27/20/4/granvia-0.jpeg")
    st.caption("elplural.com")
    st.write("""Es una de las calles más transitadas de la capital. En ella encontrarás lugares emblemáticos, cines y teatros, además de tiendas 
                de cadenas de ropa. Disfruta de ella con calma, con la mochila por delante, y mirando hacia arriba para ver sus edificios y curiosidades.""")
    # Sección Museo del Prado.
    st.subheader("Museo del Prado")
    st.image("https://artemisialatenebrista.com/wp-content/uploads/2020/11/Fusilamiento-de-Torrijos-y-sus-companeros-en-las-playas-de-Malaga-copia-copia-7-1024x277.jpg")
    st.caption("@AntonioGisbert")
    st.write("""Fundado a principios del siglo XIX, el museo del prado es una de las pinacotecas más importantes y visitadas del mundo, con una colección 
                que ronda las 1700 obras, entre las que se incluyen obras de Velazquez, Goya o El Bosco entre otros. """)
    # Sección Parque del Retiro.
    st.subheader("Parque del Retiro")
    st.image("https://pequeviajes.com/wp-content/uploads/2018/12/parque-del-retiro.jpg")
    st.caption("pequeviajes.com")
    st.write("""El Retiro es el parque público más emblemático de Madrid. Un lugar ideal para dar un agradable paseo mientras descubres los bellos 
                rincones que guarda. Considerado como una de las principales atracciones turisticas de la ciudad, allí podrás encontrar el Palacio 
                de Cristal, la escultura del Ángel Caído, el Parterre o el Estanque Grande.""")
    # Sección teatros y musicales.
    st.subheader("Teatros y musicales")
    st.image("https://decoratel.com/wp-content/uploads/2019/04/distribucion-de-butacas-teatro-lope-de-vega-de-madrid-1024x505.jpg")
    st.caption("decoratel.com")
    st.write("""Madrid cuenta con la mayor oferta de teatros y musicales de España, entre los que destaca el ya mítico El rey león. Especialmente conocida en 
                este ámbito es la Gran Via, conocida como el Broadway madrileño por la cantidad de musicales que allí se pueden disfrutar.""")
    st.subheader("Y un largo etcétera...")
    st.write("----")
    # Fuentes enlazadas de donde he obtenido la información.
    st.markdown("Fuentes:")
    st.markdown("""[sitiosdeespaña.es](https://www.sitiosdeespana.es/articulo/que-ver-y-hacer-en-madrid-33-cosas-que-no-debes-pederte)""")
    st.markdown("""[Wikipedia](https://es.wikipedia.org/wiki/Madrid)""")


# Página de proyecto.
if seleccionar_direccion == "Proyecto":

    # Establezco un título como encabezado de la página.

    st.title("Proyecto")

    # Diseño la página.
        # Introduzco texto para indicar el preprocesamiento realizado.
    cantidad = df.value_counts().sum()
    st.write("____")
    st.write("""El ejercicio final del módulo 2 consiste en estudiar la problemática de los pisos de alquiler en la ciudad de Madrid.
                La realización del proyecto ha constado de los siguientes pasos:\n\n -Importación de librerías necesarias (numpy, 
                pandas, plotly_express, etc.).\n\n -Lectura del archivo de trabajo. \n\n -Limpieza del dataset. \n\n -Ánalisis y 
                realización de gráficos.\n\n La limpieza del dataset se ha realizado siguiendo las recomendaciones del enunciado y ha 
                consistido en la eliminación de las columnas 'name', 'id', 'host_name', 'last_review' y en la sustitución de los 
                valores nulos de la columna 'reviews_per_month' por el valor 0. Una vez realizado este paso he comprobado la información 
                resultante y he comenzado con el análisis y la realización de gráficos. Más adelante se puede ver el dataset 
                una vez procesado e información relacionada con la media, percentiles, máximos y mínimos, etc.""")
    

    # Inserto el dataframe utilizando un botón para ello.

    if st.button ("Dataframe", disabled=False, type = "secondary"):
        st.dataframe(df)
    st.write("----")

    if st.button ("Información de los datos", disabled = False, type = "secondary"):
        st.table(df.describe())
    st.write("-----")
    

# Página de gráficos.
if seleccionar_direccion == "Gráficos y análisis":    

    # Doy título a la página.

    st.title("Gráficos y análisis")

    # Creo pestañas para los diferentes gráficos.

    tabs = st.tabs(["Correlaciones",
                    "Alojamientos",
                    "Disponibilidad",
                    "Localización"
                    ])

    # Creo todas las gráficas.

    # Gráficas de la primera pestaña.
    tab_plot = tabs[0] 
    # Mapa de calor con las correlaciones.
    with tab_plot:
        grafico0 = px.imshow(df.corr(), text_auto = True, title = "Gráfico de correlaciones", zmin = -1, zmax = 1, color_continuous_scale = 'rdbu',width=800, height=800)
        grafico0.update_layout(overwrite=True)
        grafico0.add_layout_image(go.layout.Image(
        source="https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Gran_V%C3%ADa_%28Madrid%29_1.jpg/1200px-Gran_V%C3%ADa_%28Madrid%29_1.jpg",
        x=-0.4,
        y=1.2,
        sizex=1.9,
        sizey=1.5,
        sizing='stretch',
        opacity=0.2,
        layer='below'
        ))
        st.plotly_chart(grafico0)
        st.write("----")
        st.write("""Se observa que, al igual que ocurria con los datos de otras ciudades, no existe gran correlación entre ninguna de las variables de 
                    de estudio, con la exepción del número de reviews y las reviews por mes, que llegan a tener una correlación cercana al 70%. Curiosamente, 
                    el precio no guarda especial correlación con nada.""")

    # Gráficas de la segunda pestaña.
    tab_plot = tabs[1] 
    # Histograma de alojamientos por distrito.
    with tab_plot:
        # Total alojamientos.
        alojamientos_total = df["neighbourhood_group"].value_counts().sum()
        # Alojamientos distrito centro.
        alojamientos_centro = df[df["neighbourhood_group"] == "Centro"].value_counts().sum()
        # Histograma.
        grafico1 = px.histogram(df, x ="neighbourhood_group", color = "neighbourhood_group", title = "Alojamientos por distrito", labels = {"neighbourhood_group":"Distritos"}, width=800, height=600)
        grafico1.update_layout(showlegend=False)
        grafico1.add_layout_image(go.layout.Image(
        source="https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Gran_V%C3%ADa_%28Madrid%29_1.jpg/1200px-Gran_V%C3%ADa_%28Madrid%29_1.jpg",
        x=-0.4,
        y=1.3,
        sizex=1.9,
        sizey=1.8,
        sizing='stretch',
        opacity=0.2,
        layer='below'
        ))
        st.plotly_chart(grafico1)
        st.write("----")
        st.write(f"""En el histograma anterior se puede observar la disponibilidad de alojamientos por distrito. El distrito Centro tiene {alojamientos_centro} 
                    alojamientos disponibles de los {alojamientos_total} totales, muchos más que el resto de distritos, que apenas sobrepasan los mil en algunos casos, y no llegan a ellos en otros. 
                    Esto se debe a que el distrito Centro es la zona más turistica y concurrida de la ciudad, lo que confirmaría la hipótesis de partida de que muchos
                    propietarios privados encuentran más rentable alquilar a turistas.""")
        st.write("----")
    
    with tab_plot:
        # Histograma de alojamientos por barrio.
        grafico2 = px.histogram(df, x ="neighbourhood", color = "neighbourhood", title = "Alojamientos por barrio", labels = {"neighbourhood":"Barrios"}, width=800, height=600)
        grafico2.update_layout(showlegend=False)
        grafico2.add_layout_image(go.layout.Image(
        source="https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Gran_V%C3%ADa_%28Madrid%29_1.jpg/1200px-Gran_V%C3%ADa_%28Madrid%29_1.jpg",
        x=-0.4,
        y=1.4,
        sizex=1.9,
        sizey=2.1,
        sizing='stretch',
        opacity=0.2,
        layer='below'
        ))
        st.plotly_chart(grafico2)
        st.write("----")
        st.write("""Por barrios, los que cuentan con más alojamientos son aquellos que pertenecen al distrito centro, como cabría esperar. Entre ellos, el que
                    tiene más alojamientos es Embajadores, con más de 2500, seguido de Universidad, que apenas llega a los dos mil. El resto de barrios no llegan 
                    en ningún caso a los 500 alojamientos disponibles.""")
        st.write("----")
    
    with tab_plot:
        # Histograma de tipos de alojamientos.
        grafico3 = px.histogram(df, x ="room_type", color = "room_type", title = "Tipos de alojamientos", labels = {"room_type":"Tipos"}, width=800, height=600, color_discrete_sequence=px.colors.qualitative.Pastel)
        grafico3.update_layout(showlegend=False)
        grafico3.add_layout_image(go.layout.Image(
        source="https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Gran_V%C3%ADa_%28Madrid%29_1.jpg/1200px-Gran_V%C3%ADa_%28Madrid%29_1.jpg",
        x=-0.4,
        y=1.3,
        sizex=1.9,
        sizey=1.7,
        sizing='stretch',
        opacity=0.2,
        layer='below'
        ))
        st.plotly_chart(grafico3)
        st.write("----")
        st.write("""En cuanto a tipos de alojamientos ocurre como en todos los casos estudiados con anterioridad, la mayoría de alojamientos son casas o apartamentos 
                    completos, más de doce mil. Le siguen, por número de alojamientos, habitaciones privadas, con más de siete mil. El resto de tipos tienen valores 
                    residuales.""")
        st.write("----")
    
    # Gráficas de la tercera pestaña.
    tab_plot = tabs[2]
    # Gráfico de caja de disponibilidad por distrito.
    with tab_plot:
        grafico4 = px.box(df, x = "neighbourhood_group", y = "availability_365", title = "Disponibilidad por distrito", color = "neighbourhood_group", width=800, height=600)
        grafico4.update_layout(showlegend=False)
        grafico4.add_layout_image(go.layout.Image(
        source="https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Gran_V%C3%ADa_%28Madrid%29_1.jpg/1200px-Gran_V%C3%ADa_%28Madrid%29_1.jpg",
        x=-0.4,
        y=1.3,
        sizex=1.9,
        sizey=1.6,
        sizing='stretch',
        opacity=0.2,
        layer='below'
        ))
        st.plotly_chart(grafico4)
        st.write("----")
        st.write("""En este gráfico podemos observar la disponibilidad media por distrito. El rango intercuartílico q3-q1, es decir, el 50% de la disponibilidad 
                    diaria anual está comprendida dentro de la caja. Los bigotes indican la variabilidad fuera de los cuartiles superior e inferior, que puede ir 
                    desde 0 dias al año, hasta 65.""")
        st.write("----")
    
    # Gráficas de la tercera pestaña.
    tab_plot = tabs[3]
    with tab_plot:
        # Mapa con la localización de los alojamientos en los diferentes distritos.
        grafico5 = px.scatter_mapbox(df, lat='latitude', lon='longitude', color='neighbourhood_group', title = "Alojamientos por distrito", zoom=10, width = 800, height = 600)
        grafico5.update_layout(mapbox_style='open-street-map')
        grafico5.add_layout_image(go.layout.Image(
        source="https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Gran_V%C3%ADa_%28Madrid%29_1.jpg/1200px-Gran_V%C3%ADa_%28Madrid%29_1.jpg",
        x=-0.4,
        y=1.3,
        sizex=1.9,
        sizey=1.6,
        sizing='stretch',
        opacity=0.2,
        layer='below'
        ))
        st.plotly_chart(grafico5)
        st.write("----")
        st.write("""Los mapas indican la localización geográfica de los alojamientos sobre un plano de la ciudad. Sin hacer zoom tendrían poca utilidad porque no 
                    permiten ver la localización exacta. Sin embargo, podrían ser utiles para ver la densidad de alomientos por distrito o una representación 
                    sobre el mapa de la localización de los diferentes distritos. Así, podríamos ver como la densidad es mayor en distrito Centro. Aun así, para 
                    esto hay mejores gráficos, como los vistos en el apartado anterior.""")
        st.write("----")
    
    with tab_plot:
        # Mapa con la localización de los alojamientos en los diferentes barrios.
        grafico6 = px.scatter_mapbox(df, lat='latitude', lon='longitude', color='neighbourhood', title = "Alojamientos por barrio",zoom=10, width = 800, height = 600)
        grafico6.update_layout(mapbox_style='open-street-map')
        grafico6.add_layout_image(go.layout.Image(
        source="https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Gran_V%C3%ADa_%28Madrid%29_1.jpg/1200px-Gran_V%C3%ADa_%28Madrid%29_1.jpg",
        x=-0.4,
        y=1.3,
        sizex=1.9,
        sizey=1.6,
        sizing='stretch',
        opacity=0.2,
        layer='below'
        ))
        st.plotly_chart(grafico6)
        st.write("----")
        st.write("""Cómo en el gráfico anterior, en este podemos observar la localización de los alojamientos por barrio sobre un plano de la ciudad. Podemos ver 
                    en el cómo la mayor aglomeración de alojamientos se encuentra en los barrios del distrito Centro. Si ampliamo, además, podemos ver la 
                    localización exacta.""")
        st.write("----")

    with tab_plot:
        # Mapa con la localización de los diferentes tipos de alojamientos.
        grafico7 = px.scatter_mapbox(df, lat='latitude', lon='longitude', color='room_type', title = "Tipos de alojamientos",zoom=10, width = 800, height = 600, color_discrete_sequence=px.colors.qualitative.Bold)
        grafico7.update_layout(mapbox_style='open-street-map')
        grafico7.add_layout_image(go.layout.Image(
        source="https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Gran_V%C3%ADa_%28Madrid%29_1.jpg/1200px-Gran_V%C3%ADa_%28Madrid%29_1.jpg",
        x=-0.4,
        y=1.3,
        sizex=1.9,
        sizey=1.6,
        sizing='stretch',
        opacity=0.2,
        layer='below'
        ))
        st.plotly_chart(grafico7)
        st.write("----")
        st.write("""Se puede apreciar la localización de los diferentes tipos de alojamiento en la ciudad. En el mapa se ve una mayor densidad de alojamientos 
                    de tipo casa entera, habitaciones compartidas y habitaciones de hotel en la zona centro y habitaciones privadas distribuida principalmente 
                    por la periferia. Sin embargo, sospecho que en el gráfico se produce cierto solapamiento.""")
        st.write("----")
    
    with tab_plot:
        # Mapa con la disponibilidad de los alojamientos.
        grafico8 = px.scatter_mapbox(df, lat='latitude', lon='longitude', color='availability_365', title = "Disponibilidad de alojamientos",zoom=10, width = 800, height = 600)
        grafico8.update_layout(mapbox_style='open-street-map')
        grafico8.add_layout_image(go.layout.Image(
        source="https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Gran_V%C3%ADa_%28Madrid%29_1.jpg/1200px-Gran_V%C3%ADa_%28Madrid%29_1.jpg",
        x=-0.4,
        y=1.3,
        sizex=1.9,
        sizey=1.6,
        sizing='stretch',
        opacity=0.2,
        layer='below'
        ))
        st.plotly_chart(grafico8)
        st.write("----")
        st.write("""En este mapa se aprecia la localización de los alojamientos por su disponibilidad y cómo esta se distribuye de forma uniforme por toda la ciudad.""")
        st.write("----")
