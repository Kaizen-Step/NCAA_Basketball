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
And also ****IMDB Box Office Mojo**** and  ****Kaggle**** with massive database and last but not least ****MetricsDao**** that is the reason behind this project.


""")

st.text(" \n")
st.text(" \n")

# Sources
st.write(""" ## Sources ## """)

st.write("""
Here are the reference numbers for all of the sources used in this project:
  


""")

st.write("""
 1.https://en.wikipedia.org/wiki/Cinema_of_the_United_States#Hollywood     
        2.https://en.wikipedia.org/wiki/Box_office#cite_note-1    
        3.https://help.imdb.com/article/imdbpro/industry-research/box-office-mojo-by-imdbpro-faq/GCWTV4MQKGWRAUAP?ref_=mojo_ftr_help#  
        4.http://uis.unesco.org/en/glossary-term/gross-box-office   
        5.https://www.enterpriseappstoday.com/stats/film-industry-statistics.html#:~:text=In%20the%20year%202023%2C%20the,States%20of%20America%20is%203.3%25       
        6.https://en.wikipedia.org/wiki/Film_genre  
        7.https://en.wikipedia.org/wiki/Major_film_studios   
        8.https://en.wikipedia.org/wiki/Motion_Picture_Association_film_rating_system        
        9.https://medium.com/ipg-media-lab/movies-no-longer-occupy-the-center-of-pop-culture-can-hollywood-stage-a-comeback-1a79600a5648    
        10.https://www.boxofficemojo.com/   
    

""")
