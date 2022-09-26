import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu

st.set_option('deprecation.showPyplotGlobalUse', False)


# Read data
data = pd.read_csv("/Users/sarasadaka/Desktop/MSBA325/Assignment 2/cardio_train.csv")

Menu = option_menu(None, ["Pie Chart","Histogram","Boxplot"],icons=["pie","bar-chart-line","sliders"],menu_icon="cast", default_index=0, orientation="horizontal", styles={"container": {"padding": "0!important", "background-color": "#fafafa"},"icon": {"color": "black", "font-size": "25px"}, "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},"nav-link-selected": {"background-color": "pink"},})
if Menu == "Pie Chart": st.title('Gender Distribution in Dataset')
if Menu == "Histogram": st.title('Height & Weight Distribution in Dataset')
if Menu == "Boxplot": st.title('Variable Distribution with respect to Cardiovascular Disease')


if Menu == "Pie Chart": st.text("As we can see we have 48.2% as females and 51.8% as males in the dataset.")

fig = px.pie(data, values='gender', names='gender')
if Menu == "Pie Chart": st.write(fig)



if Menu == "Histogram": st.text("This page displays the ditribution of Height & Weight in the dataset.")
if Menu == "Histogram": st.text("As we can see we have that the majority of the sample has a height of 165m & a weight range of [64.75, 65.24] kg.")
col1, col2 = st.columns(2)
with col1:
    hist1 = px.histogram(data, x="height")
    if Menu == "Histogram": st.plotly_chart(hist1)
with col2:
    hist2 = px.histogram(data, x="weight")
    if Menu == "Histogram": st.plotly_chart(hist2)



if Menu == "Boxplot": st.text("The final page in the dashboard display two boxplots.")
if Menu == "Boxplot": st.text("The first one show the variation of Systolic Blood Pressure for females and males")
if Menu == "Boxplot": st.text("and the second boxplot shows the variation of Cardiovascular disease with respect to weight.")
if Menu == "Boxplot": st.text("From both boxplots we can see that the dataset has outliers and they should be handled so that results can be conclusive in further steps.")
col3, col4 = st.columns(2)
with col3:
    box1 = px.box(data, x="gender", y="ap_hi")
    if Menu == "Boxplot": st.plotly_chart(box1)
with col4:
    box2 = px.box(data, x="cardio", y="weight")
    if Menu == "Boxplot": st.plotly_chart(box2)







                