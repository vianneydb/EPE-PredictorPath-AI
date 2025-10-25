# app.py
import streamlit as st
import pandas as pd
import joblib

# Título
st.title("EPE Patch Priority Predictor")
st.write("Sube tu CSV con los datos del sistema y obtén las prioridades de parcheo.")

# Cargar modelo
model = joblib.load("model.pkl")

# Subida de archivo
uploaded_file = st.file_uploader("Elige un archivo CSV o TSV", type=["csv", "tsv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file, sep=None, engine='python')  # detecta CSV o TSV

    # Preprocesamiento
    df["Last Patch Age (days)"] = (pd.to_datetime("today") - pd.to_datetime(df["Last Patch Date"])).dt.days
    df["Days Until Next Window"] = (pd.to_datetime(df["Next Available Window"]) - pd.to_datetime("today")).dt.days
    df_encoded = pd.get_dummies(df, columns=["Regulatory Zone", "Requires Reboot"], drop_first=True)

    # Asegúrate de usar las mismas columnas que entrenaste
    drop_cols = ["System ID", "Patch Priority", "Last Patch Date", "Next Available Window"]
    X = df_encoded.drop(columns=[c for c in drop_cols if c in df_encoded.columns], errors='ignore')

    # Predicción
    df["Patch Priority"] = model.predict(X)

    # Mostrar resultados
    st.subheader("Resultados")
    st.dataframe(df[["System ID", "Patch Priority"]])
