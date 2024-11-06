import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carga el archivo CSV "database_titanic.csv" en un DataFrame de pandas.
df = pd.read_csv("agriculture_dataset.csv")

# Muestra un título y una descripción en la aplicación Streamlit.
st.write("""
# Comparacion entre dos tipos de cosechas
## Gráfico usando la base de datos de agricultura
""")

# Tomando datos para arroz y contando la cantidad
df_rice = df[df["Crop_Type"] == "Rice"]
cant_rice = len(df_rice)

# Tomando datos para Maiz y contando la cantidad
df_maize = df[df["Crop_Type"] == "Maize"]
cant_maize = len(df_maize)

# Si el checkbox está activado, usar un color diferente
with st.sidebar:
    st.write("# Opciones")
    casilla_colorbarra = st.checkbox("Color de barras alternativo", value=False)
if casilla_colorbarra == True:
    colore = "#EB840E"  # si esta marcado
else:
    colore = "#2EAEB8"  

fig,ax = plt.subplots()
ax.bar(["Arroz", "Maiz"], [cant_rice, cant_maize], color = colore)
ax.set_xlabel("Tipo de cosecha")
ax.set_ylabel("Cantidad")
ax.set_title('Distribución entre arroz y maiz plantados')
st.pyplot(fig)

#Botones
if st.button("Informacion sobre el arroz"):
  st.image("arorooz.jpg", caption="Brotes de arroz")
  st.write("""Siembra: Primavera-Verano (mayo-junio).
Cosecha: 6-8 meses después de la siembra (octubre-diciembre).
Condiciones: Clima cálido, mucha agua, suelos ricos en nutrientes y buena exposición al sol.""")  
    
if st.button("Información sobre el maíz"):
  st.image("maiztoiuhs.jpg", caption="Brotes de maíz")
  st.write("""Siembra: Primavera (marzo-mayo).
Cosecha: 2-4 meses después de la siembra (julio-octubre).
Condiciones: Clima cálido, suelo bien drenado, luz solar abundante, y riego moderado.""")

# Pregunta al usuario sobre el tipo de cosecha en mayor cantidad
correctooo = "Arroz"
respuesta = st.radio(
    "Según la tabla, ¿cuál es el tipo de cosecha en mayor cantidad?",
    ["Maíz", "Arroz"], index = None) #None para que no este seleccionada alguna desde el principio

# Mostrar si la respuesta del usuario es correcta o incorrecta
if respuesta == correctooo:
    st.success(f"¡Correcto! El tipo de cosecha en mayor cantidad es {correctooo}.") # sucess resalta lo correcto
    video_url = "https://www.youtube.com/watch?v=9vlNMTLqzWo"  # del youtube por que pesa 10 mb?
    st.write("Aquí tienes un video sobre el arroz")
    st.video(video_url)
elif respuesta == "Maíz":
    st.error(f"Incorrecto. El tipo de cosecha en mayor cantidad es {correctooo}.") # error resalta la equivocacion

# Pregunta al usuario sobre el tipo de cosecha en mayor cantidad
corpregdos = "Primavera"
respuesdos = st.radio(
    "Según la información acerca del maíz, ¿Cuando se siembra?",
    ["Otoño", "Primavera", "Verano"], index = None) #None para que no este seleccionada alguna desde el principio

if respuesdos == "Otoño":
    st.error(f"Incorrecto. El maíz se siembra en {corpregdos}.")
if respuesdos == corpregdos:
    st.success(f"¡Correcto! El maíz se siembra en {corpregdos}.") 
if respuesdos == "Verano":
    st.error(f"Incorrecto. El maíz se siembra en  {corpregdos}.") 
# Usando la notación "with" para crear una barra lateral en la aplicación Streamlit.
with st.sidebar:
    div = st.slider('Número de bins:', 0, 50, 10)
    st.write("Bins=", div)

# Desplegamos un histograma con los datos del eje X
figg, axx = plt.subplots(figsize=(8, 5))  
axx.hist(df["Fertilizer_Used(tons)"], bins=div, color="#078385", edgecolor="#B77D26")
axx.set_xlabel("Toneladas")
axx.set_ylabel("Frecuencia")
axx.set_title("Histograma Fertilizante usado")
st.pyplot(figg)


st.write("""
## Muestra de datos cargados
""")
# Graficamos una tabla
st.table(df.head())
