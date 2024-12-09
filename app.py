import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv("./vehicles_us.csv") #Le el DataSet y lo guarda como DataFrame
st.header("ANÁLISIS ANUNCIO VENTA DE COCHES") #Agrega un encabezado utilizando streamlit

build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')
    fig = px.histogram(car_data, x="odometer") #Crea un gráfico a partir del DF car_data
    st.plotly_chart(fig, use_container_width=True) #muetra el gráfico guardado en fig


build_scatter = st.checkbox("Construir un gráfico de dispersión")

if build_scatter: #Si se oprime el botón ejecuta:
    st.write("Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches")
    fig = px.scatter(car_data, x="odometer", y="price") #Crea un gráfico
    st.plotly_chart(fig,use_container_width=True) #muetra el gráfico guardado en fig
