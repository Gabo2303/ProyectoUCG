import os

import pandas as pd
import streamlit as st


st.set_page_config(page_title="Proyecto Integrador - Ciencia de Datos", layout="wide")


@st.cache_data

def load_dataset(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


st.title("Proyecto Integrador de Ciencia de Datos")
st.markdown(
    """
    Esta aplicación permite cargar un dataset, explorar su estructura, analizar variables clave
    y visualizar patrones relevantes para un proyecto aplicado de análisis de datos.
    """
)

DEFAULT_DATASET = os.path.join("archive", "material.csv")

uploaded_file = st.sidebar.file_uploader("Cargar un dataset CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    source_label = uploaded_file.name
else:
    df = load_dataset(DEFAULT_DATASET)
    source_label = DEFAULT_DATASET

st.sidebar.caption(f"Dataset cargado: {source_label}")

st.subheader("1. Exploración inicial")
col1, col2, col3 = st.columns(3)
col1.metric("Filas", df.shape[0])
col2.metric("Columnas", df.shape[1])
col3.metric("Valores nulos", int(df.isna().sum().sum()))

st.dataframe(df.head(10), use_container_width=True)

st.write("### Tipos de columnas")
info = pd.DataFrame({
    "Columna": df.columns,
    "Tipo": df.dtypes.astype(str).values,
    "Nulos": df.isna().sum().values,
    "Únicos": df.nunique().values,
})
st.dataframe(info, use_container_width=True)

st.write("### Resumen estadístico")
numeric_cols = df.select_dtypes(include="number").columns.tolist()
if numeric_cols:
    st.dataframe(df[numeric_cols].describe().T, use_container_width=True)
else:
    st.info("No hay columnas numéricas disponibles para resumir.")

st.subheader("2. Análisis de variables")
left, right = st.columns(2)
with left:
    selected_col = st.selectbox("Selecciona una variable para visualizar", df.columns.tolist())
    st.bar_chart(df[selected_col].value_counts().head(10))

with right:
    if "Use" in df.columns:
        st.write("Distribución de la variable objetivo 'Use'")
        st.bar_chart(df["Use"].value_counts())

st.subheader("3. Visualizaciones clave")
if numeric_cols:
    st.write("Correlación entre variables numéricas")
    corr = df[numeric_cols].corr().fillna(0)
    st.dataframe(corr, use_container_width=True)

    st.write("Comparación rápida de variables numéricas")
    feature = st.selectbox("Variable para comparar", numeric_cols, key="feature_compare")
    st.line_chart(df[feature].astype(float).reset_index(drop=True))

st.subheader("4. Interpretación del análisis")
if "Use" in df.columns:
    use_counts = df["Use"].value_counts(normalize=True).mul(100).round(1)
    st.write("Proporción estimada por clase:")
    st.write(use_counts.to_dict())

st.caption("Proyecto desarrollado con Streamlit para análisis exploratorio y visualización aplicada del dataset.")