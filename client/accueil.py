

import streamlit as st
from controller.controller import *


st.write("Here are the data on which we do our work!")

if 'username' not in st.session_state :
    st.sidebar.success("welcome sir !!")

tab1, tab2= st.tabs(["Iris", "Diabetes"])

with tab2:
    diabete= getDb("diabete")
    if st.checkbox('Show diabete', True):
        st.header("Diabetes dataset")
        st.write(diabete)
    st.text("The diabetes data description")
    st.write(diabete.describe())

   
with tab1:
    iris= getDb("iris")
    if st.checkbox('Show iris', True):
        st.header("Iris dataset")
        st.write(iris)
    st.text("The iris data description")
    st.write(iris.describe())




