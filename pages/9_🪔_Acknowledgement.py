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
st.set_page_config(page_title='Aknowledgement - Insight of the Week',
                   page_icon=':bar_chart:', layout='wide')
st.title('🪔 References')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# SQL Codes
st.write(""" ## Acknowledgement ## """)

st.write("""
We are grateful to all who helped us develop this project specially [**Mr. Ali Taslimi**](https://twitter.com/AliTslm) with comprehensive streamlit open source project [Cross chain Monitoring](https://github.com/alitslm/cross_chain_monitoring) that provides streamlit functions and tools.
And also ****Bartorvik**** and  ****Kenpom**** with massive database and last but not least ****MetricsDao**** that is the reason behind this project.


""")

st.text(" \n")
st.text(" \n")

# Sources
st.write(""" ## Sources ## """)

st.write("""
Here are the reference numbers for all of the sources used in this project:
  


""")

st.write("""
 1.https://www.ncaa.org/news/2022/3/10/media-center-from-authorized-sources.aspx     
        2.https://www.bannersontheparkway.com/2023/2/13/23598002/rule-15-2-a-and-the-state-of-officials-in-college-basketball-big-east    
        3.https://kenpom.com/    
        4.https://barttorvik.com/trank.php#  
        5.https://www.sas.com/en_gb/insights/articles/analytics/machine-learning-algorithms.html#:~:text=At%20its%20most%20basic%2C%20machine,developing%20'intelligence'%20over%20time. 
    

""")
