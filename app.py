import pandas as pd
import plotly.express as px
import streamlit as st
st.header('Anuncios de venta de vehiculos en los Estados Unidos')
car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
# crear casilla de verificacion
build_histogram = st.checkbox('Construir un histograma')
if build_histogram:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# crear casilla de verificacion
build_scatter = st.checkbox('Construir diagrama de dispersion')
if build_scatter:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches, graficando la variación del precio de los vehiculos con respecto al modelo')

    # crear un histograma
    fig = px.scatter(car_data, x="model_year", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
