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
st.write("""
## Muestra de datos cargados
""")
# Graficamos una tabla
st.table(df.head())