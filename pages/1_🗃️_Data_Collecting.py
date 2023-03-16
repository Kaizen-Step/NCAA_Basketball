# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

# Theme
theme_plotly = None  # None or streamlit


# Layout
st.set_page_config(page_title='Data Collecting - NCAA_Basketball',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('🗃️ Data Collecting')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'Huston_data':
        return pd.read_csv('Data/2023_NCAA_Match/Houston_2023.csv')
    elif query == 'Barttorvik':
        return pd.read_csv('Data/barttorvik_2023.csv')
    elif query == 'kepnom':
        return pd.read_csv('Data/Kenpom_2023.csv')
    return None


Huston_data = get_data('Huston_data')
Barttorvik = get_data('Barttorvik')
kepnom = get_data('kepnom')

df = Huston_data
df2 = Barttorvik
df3 = kepnom

#################################################################################################
st.write(""" ### Data Gathering     """)

st.write(""" In order to create an effective NCAA match prediction application, it is important to collect and analyze relevant data on the teams and players involved in each game. There are several sources of data that can be used to inform match predictions, including statistics on team and player performance, historical data on past games, and real-time data on current games. In addition to statistics, historical data on past games can also be useful in predicting the outcome of a particular match-up. Historical data can reveal patterns and trends in team performance that can be used to make informed predictions about future games. This data can be collected from a variety of sources, including game archives, sports news websites, and other online databases. 
   

  """)


st.info(""" ##### In This Data Gathering Section you can find: ####

* NCAA Match played in 2023 with detailed result   
* Each team different Factors Data sets in barttorvick
* Further investigation in Kenpom ranking site

""")


#################################################################################################


st.write(""" ## NCAA Match played in 2023 with detailed result     """)

st.write(""" NCAA matches played data sets are collections of data that record various statistics and information related to NCAA matches, such as team scores, team performance, and game outcomes. As there was no appropriate data set that includes NCAA games in 2023 when we first started looking into the idea, we searched the internet for websites that might have the information.  The [barttorvick.com](https://barttorvik.com/gamestat.php?year=2023) listed all the matches played in 2023 in detail, but unfortunately the site just presents the 2500 match results out of the 1131 NCAA matches played in 2023.   So we start scraping the site for each individual team and generate a list for all 363 teams that are involved in the NCAA's different conferences individually, then gather up all the information in one table and publish it into Kaggle for public consumption under the name ["Kaggle-kaizen step-NCAA 2023 All Match Result"](https://www.kaggle.com/datasets/kaizenstep/ncaa-2023-all-games-results). An example table for 10 out of 31 Huston's  games is shown in the section below. The type of match refers to whether it is a conference or non-conference match, and the venue is the stadium where the matches are held based on first team. the rest of the tables is the statistics of teams played in the specefic match which will be explained throughly in the following sections.
 """)

st.table(df.head(10))


st.write(""" ##  Gathering Data of team statistics and Important Factors in barttorvick """)
st.write(""" There are lots of different statistics and features of teams and players that could influence the match result. In search of good parameters for our model, we use [barttorvick.com](https://barttorvik.com) 2023 annual ranking and features. At the following, you could see this statistics of the top 10 out of 363 teams. The statistics and factors were thoroughly explained in Effective Offensive and Defensive Section.
""")
st.table(df2.head(10))

##################################################################################
st.write(""" ##  Further investigation in Kenpom ranking site """)
st.write(""" We also used [Kenpom's](https://kenpom.com/) ranking and statistics, which are mostly the same as Battrovick's with a few differences, for further exploration and as in the bounty example suggested. These data were compiled into a single table data set and subjected to a sensibility analysis, which is covered in detail in the following two sections. .The following table lists the top 10 teams according to Kepnom. 
""")
st.table(df3.head(10))

##########################################################################

st.text(" \n")

st.info(""" #### Summary: ####


* 1131 match result which all held in 2022-2023 scraped from Battrovik site and put in kaggle for public usage
* all attribute and statistics of 363 teams and players invovled in NCAA devision scraped from Battrovik site and gathered in one table
* for further exploration features in Kenpom ranking site also scrape and added to data set



""")
