

import streamlit as st
from controller.controller import *
import pandas as pd


st.write("Make prediction on a dataset")


if 'username' not in st.session_state :
    st.sidebar.success("welcome sir !!")


tab1, tab2= st.tabs(["Iris", "Diabetes"])

with tab1:

    message = st.text('')

    st.subheader("Iris data")

    def pred():
        pass

    uploaded_file = st.file_uploader("Choose a file (iris)", type=["csv"])
    if uploaded_file is not None:
        # Can be used wherever a "file-like" object is accepted:
        dataframe = pd.read_csv(uploaded_file)
        # select vars to predict on
        vars= st.multiselect("select the variable to predict on. (Must be four): ", dataframe.columns, max_selections=4, help="must be all float")
        if len(vars)==4:
            #arr= dataframe.iloc[:,:-1].to_json()
            arr=dataframe[vars].to_dict(orient="split")
            try:
                rep= doBigPrediction(arr, "iris")
                preds= rep["prediction"]
                proba= rep["proba"]
                dataframe["prediction"]= preds
                dataframe["probability"]= proba
                if st.checkbox('display/hide dataset', True):
                    st.header("Dataset with predictions")
                    st.write(dataframe)
            except Exception:
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.warning("Please check the selected columns. They doesn't match the model vars!!")




with tab2:

    st.subheader("Diabetes data")

    diabete_file = st.file_uploader("Choose a file (diabetes)", type=["csv"], help="must be csv files")
    if diabete_file is not None:
        df = pd.read_csv(diabete_file)
        # select vars to predict on
        variables= st.multiselect("select the variables to predict on. (Must be 8): ", df.columns, max_selections=8, help="must be all float")
        if len(variables)==8:
            #arr= dataframe.iloc[:,:-1].to_json()
            arr2=df.iloc[:,:-1].to_dict(orient="split")
            try:
                rep2= doBigPrediction(arr2, "diabete")
                pred2= rep2["prediction"]
                proba2= rep2["proba"]
                df["prediction"]= pred2
                df["probability"]= proba2
                if st.checkbox('display or hide dataset', True):
                    st.header("Dataset with predictions")
                    st.write(df)
            except Exception:
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.warning("Please check the selected columns. They doesn't match the model vars!!")








