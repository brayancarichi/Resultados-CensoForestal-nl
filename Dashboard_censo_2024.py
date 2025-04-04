#streamlit run Dashboard_censo_2024.py

import streamlit as st
import pandas as pd
import plotly.express as px

# Definimos los parámetros de configuración de la aplicación
st.set_page_config(
    page_title="Tablero de resultados censo forestal año 2024 zona metropolitana de Monterrey, NL", #Título de la página
    page_icon="📊", # Ícono
    layout="wide", # Forma de layout ancho o compacto
    initial_sidebar_state="expanded" # Definimos si el sidebar aparece expandido o colapsado
)


# Cargamos el dataframe desde un CSV
dfDatos = pd.read_csv('datosTiendaTecnologiaLatam.csv')
Datos = pd.read_csv('Datos.csv')
Año = 2024

# Declaramos los parámetros en la barra lateral
with st.sidebar:
    # Filtro de años
    imagen = st.image('WhatsApp Image 2024-11-15 at 12.25.46 PM (1).jpeg')
    texto_intro = st.text('Central de Geoninteligencia S.A. de C.V.')
    parAno=st.selectbox('Año',options=dfDatos['anio'].unique(),index=0)
    # Filtro de Mes    
    
    # Filtro de País
    

# Si hay parametros seleccionados aplicamos los filtros
if parAno:
    dfDatos=dfDatos[dfDatos['anio']==parAno]




# Obtenemos los datos del mes seleccionado

# Obtenemos los datos del año anterior


st.title('Tablero de resultados censo forestal año 2024 zona metropolitana de Monterrey, NL')


# Mostramos las métricas
# Declaramos 5 columnas de igual tamaño
c1,c2,c3,c4 = st.columns(4)
with c1:
    Zona_analizada = 32440
    Zonas = Zona_analizada
    
    st.metric(f"Extensión analizada",f'{Zonas:,.0f} Hectáreas')
    
with c2:
    imagenes = 450
    
    
    st.metric(f"Imágenes satelitales analizadas",f'{imagenes:.0f}')
with c3:
    arboles = 6016805
    
    
    st.metric(f"Arboles detectados",f' {arboles:,.0f}')
with c4:
    colonias = 630
    
    
    st.metric(f"Colonias analizadas ",f' {colonias:,.0f}')


# Declaramos 2 columnas en una proporción de 60% y 40%
c1,c2 = st.columns([60,40])
with c1:
    dfVentasMes = dfDatos.groupby('mes').agg({'Total':'sum'}).reset_index()
    fig = px.line(dfVentasMes,x='mes',y='Total', title='Arboles detectados por mes (Censo forestal estatal) (próximamente)')    
    st.plotly_chart(fig,use_container_width=True)
with c2:
    analisis_colonia = pd.DataFrame(dict(
        Zona = ["Noroeste","Noreste","Sureste","Suroeste"],
        Arboles = [2053962,393922,1082902,2486019]
    ))
    analisis_colonia2 = analisis_colonia.sort_values(by='Arboles', ascending=False)
    
    fig = px.bar(analisis_colonia2,x='Zona',y='Arboles', title=f'Arboles detectados por zona: ',color='Arboles',text_auto=',.0f')
    fig.update_layout(showlegend=False) #Determina si se muestra o no la leyenda
    st.plotly_chart(fig,use_container_width=True)

imagen_censo = st.image('Censo2.png')
texto = st.text('Figura 1. Resultados obtenidos del censo forestal urbano de la ciudad de Monterrey (2024). Fuente: Elaboración propia.')

subtitulo = st.header('Dinámica en el cambio en el uso del suelo')

# Declaramos 2 columnas en una proporción de 60% y 40%
c1,c2 = st.columns([60,40])
with c1:
    analisis_suelo2 = pd.DataFrame(dict(
        Suelo = ["Pastizal","Área urbana","Agricultura","Bosque"],
        Hectáreas = [83444,0,43886,176845]
    ))
   
    analisis_suelo2 = analisis_suelo2.sort_values(by='Hectáreas', ascending=False)
    fig = px.bar(analisis_suelo2,x='Suelo',y='Hectáreas', title=f'Pérdidas en hectáreas de las coberturas del suelo en la región:', color='Hectáreas',text_auto=',.0f')
    fig.update_layout(showlegend=False) #Determina si se muestra o no la leyenda
    st.plotly_chart(fig,use_container_width=True)
    
    
with c2:
    analisis_suelo = pd.DataFrame(dict(
        Suelo = ["Pastizal","Área urbana","Agricultura","Bosque"],
        Hectáreas = [204165,31506,32757,47502]
    ))
    
    analisis_suelo = analisis_suelo.sort_values(by='Hectáreas',ascending=False)
    fig = px.bar(analisis_suelo,x='Suelo',y='Hectáreas', title=f'Ganancias en hectáreas de las coberturas del suelo en la región:', color='Hectáreas',text_auto=',.0f')
    fig.update_layout(showlegend=False) #Determina si se muestra o no la leyenda
    st.plotly_chart(fig,use_container_width=True)

imagen_suelo = st.image('Usos del suelo.png')
st.text('Figura 2. Cambios en las coberturas de uso del suelo. Fuente: elaboración propia ')

