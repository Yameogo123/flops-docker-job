

import streamlit as st
from controller.controller import *


st.write("Make prediction on new data")


if 'username' not in st.session_state :
    st.sidebar.success("welcome sir !!")


tab1, tab2= st.tabs(["Iris", "Diabetes"])

with tab1:

    message = st.text('')

    st.subheader("Iris data")

    def pred():
        db= {"sepal_length": sepal_length, "sepal_width":sepal_width, "petal_length":petal_length, "petal_width": petal_width}
        rep = doPrediction(db, "iris")
        prediction= rep["prediction"]
        prob= rep["proba"]
        st.write("the predicted flower is : "+prediction+ " with a probability of "+str(prob) )

    with st.form('Iris prediction'):
        sepal_length= st.number_input('enter the sepal length', key = 'w')
        sepal_width= st.number_input('enter the sepal width', key = 'x')
        petal_length= st.number_input('enter the petal length', key = 'y')
        petal_width= st.number_input('enter the petal width', key = 'z')
        
        st.form_submit_button('predict', on_click=pred())



with tab2:

    def pred2():
        db= {"Pregnancies": pregnancies, "Glucose":glucose, "BloodPressure":bloodPressure, "SkinThickness": skin, "Insulin":insulin, "BMI": bmi, "DiabetesPedigreeFunction":dpf, "Age": age}
        rep = doPrediction(db, "diabete")
        prediction= rep["prediction"]
        prob= rep["proba"]
        st.write("the patient possible diabetes status is : "+str(bool(prediction))+" with the probability of "+str(prob))

    with st.form('Diabetes prediction'):
        pregnancies= st.number_input('number of pregnancies: ', key = 'a')
        glucose= st.number_input('enter glucose: ', key = 'b', help="the patient glucose level")
        bloodPressure= st.number_input('enter a blood pressure: ', key = 'c', help="the patient blood pressure")
        skin= st.number_input('enter skin thickness: ', key = 'd', help="the patient skin thickness")
        insulin= st.number_input('enter the insulin: ', key = 'e', help="the patient insulin quantity")
        bmi= st.number_input('enter a BMI: ', key = 'f', help="the patient BMI (weight over height square: kg/m^2)")
        dpf= st.number_input('enter the DiabetesPedigreeFunction: ', key = 'g', help="diabetes likelihood depending on the subject's age and his/her diabetic family history")
        age= st.number_input('enter the age: ', key = 'h', help="patient age")
        
        st.form_submit_button('predictuon', on_click=pred2())







