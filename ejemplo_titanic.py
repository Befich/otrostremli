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
fig,ax = plt.subplots()
ax.bar(["Arroz", "Maiz"], [cant_rice, cant_maize], color = "#2EAEB8")
ax.set_xlabel("Tipo de cosecha")
ax.set_ylabel("Cantidad")
ax.set_title('Distribución entre arroz y maiz plantados')
st.pyplot(fig)
#Boton
if st.button("Arroz(foto)"):
  st.image("arorooz.jpg", caption="Brotes de arroz")
if st.button("Maiz(foto)"):
  st.image("maiztoiuhs.jpg", caption="Brotes de maiz")

# Usando la notación "with" para crear una barra lateral en la aplicación Streamlit.
with st.sidebar:
    # Título para la sección de opciones en la barra lateral.
    st.write("# Opciones")
    
    # Crea un control deslizante (slider) que permite al usuario seleccionar un número de bins
    # en el rango de 0 a 10, con un valor predeterminado de 2.
    div = st.slider('Número de bins:', 0, 50, 10)
    
    # Muestra el valor actual del slider en la barra lateral.
    st.write("Bins=", div)

# Desplegamos un histograma con los datos del eje X
fig, ax = plt.subplots(1, 2, figsize=(10, 3))
ax.hist(df["Fertilizer_Used(tons)"], bins=div)
ax.set_xlabel("Toneladas")
ax.set_ylabel("Frecuencia")
ax.set_title("Histograma Fertilizante usado")
st.pyplot(fig)



st.write("""
## Muestra de datos cargados
""")
# Graficamos una tabla
st.table(df.head())
