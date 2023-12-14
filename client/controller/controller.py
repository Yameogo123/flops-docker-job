import streamlit as st
import requests
import pandas as pd

root= "http://server:8000/"  #"https://yameogo123-backend.hf.space/" 

@st.cache_data
def getDb(dt="diabete"):
    data_load_state = st.text('Loading data...')
    res= requests.get(root+dt)
    res= res.json()[dt]
    data_load_state.text("")
    return pd.DataFrame(res[1:], columns=res[0])


def doPrediction(x, db="iris"):
    res= requests.post(root+"predict/"+db, json=x).json()
    return res

def doBigPrediction(arr, db="iris"):
    res= requests.post(root+"predict/all/"+db, json=arr)
    rep= res.json()
    return rep