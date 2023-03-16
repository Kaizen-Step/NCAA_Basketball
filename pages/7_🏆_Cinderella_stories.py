# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from PIL import Image


# Global Variables
theme_plotly = None  # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday',
             'Thursday', 'Friday', 'Saturday', 'Sunday']

# Layout
st.set_page_config(page_title='Cinderella stories - NCAA Basketball',
                   page_icon=':bar_chart:', layout='wide')
st.title('🏆 Cinderella stories')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# SQL Codes
st.write(""" ## Game Prediction and Cinderella Story Probability ## """)

st.write("""
All the games were predicted using the model. Although almost all of the games were predicted as expected, there were cases there was only a slight edge for the favorite team. The only Cinderella story could be the win of Boise State (ranked 10) over Northwestern (ranked 7), which is marked by a red diamond beside it in the figure. The final is predicted to happen between the best two teams, namely Alabama and Houston. The final is supposed to occur in Houston, and the prediction for the final is the winning of Houston by a remarkable chance of over 68 percent.



""")

st.text(" \n")

st.image(Image.open('Images/charts.jpg'))
