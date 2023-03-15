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
    elif query == 'Weekly_2023':
        return pd.read_csv('https://raw.githubusercontent.com/Kaizen-Step/Hollywood_Box_Office_Tragedy/main/Data/Domestic/Y23/Y23-Weekly.csv')
    elif query == 'daily_table':
        return pd.read_csv('https://raw.githubusercontent.com/Kaizen-Step/Hollywood_Box_Office_Tragedy/main/Data/Domestic/Y23/Y23-Daily2.csv')
    return None


Huston_data = get_data('Huston_data')
Weekly_2023 = get_data('Weekly_2023')
daily_table = get_data('daily_table')

df = Huston_data
df2 = Weekly_2023
df3 = daily_table

#################################################################################################
st.write(""" ### Data Gathering     """)

st.write(""" In order to create an effective NCAA match prediction application, it is important to collect and analyze relevant data on the teams and players involved in each game. There are several sources of data that can be used to inform match predictions, including statistics on team and player performance, historical data on past games, and real-time data on current games. In addition to statistics, historical data on past games can also be useful in predicting the outcome of a particular match-up. Historical data can reveal patterns and trends in team performance that can be used to make informed predictions about future games. This data can be collected from a variety of sources, including game archives, sports news websites, and other online databases. 
   

  """)


st.info(""" ##### In This Data Gathering Section you can find: ####

* NCAA Match played in 2023 with detailed result   
* Each team different Factors Data sets in Kepnom
* Each team different Factors Data sets in barttorvick

""")


#################################################################################################


#####################################################

st.write(""" ## NCAA Match played in 2023 with detailed result     """)

st.write(""" NCAA matches played data sets are collections of data that record various statistics and information related to NCAA matches, such as team scores, team performance, and game outcomes. As there was no appropriate data set that includes NCAA games in 2023 when we first started looking into the idea, we searched the internet for websites that might have the information.  The [barttorvick.com](https://barttorvik.com/gamestat.php?year=2023) listed all the matches played in 2023 in detail, but unfortunately the site just presents the 2500 match results out of the 1131 NCAA matches played in 2023.   So we start scraping the site for each individual team and generate a list for all 363 teams that are involved in the NCAA's different conferences individually, then gather up all the information in one table and publish it into Kaggle for public consumption under the name ["Kaggle-kaizen step-NCAA 2023 All Match Result"](https://www.kaggle.com/datasets/kaizenstep/ncaa-2023-all-games-results). An example table for 10 out of 31 Huston's  games is shown in the section below. The type of match refers to whether it is a conference or non-conference match, and the venue is the stadium where the matches are held based on first team. the rest of the tables is the statistics of teams played in the specefic match which will be explained throughly in the following sections.
 """)

st.table(df.head(10))


st.write(""" ## Each team different Factors Data sets """)
st.write(""" The average number of daily movies released in 2019 (prior to the Covid-19 pandemic) was 54, but this figure dropped significantly to 32.4 in 2023, possibly due to an increase in the number of big production movies, as discussed in the previous section.
""")


##########################################################################

st.text(" \n")

st.info(""" #### Summary: ####


* The average daily top-ten movie gross for the first two months of 2023 was \$17.65 million
* On February 17, "Ant-Man and the Wasp: Quantumania" brought in \$46.5 million of the \$54.71 million total
* The market was easily influenced by a single big production movie
* In 2019, there were 54 average daily movie releases, however this number fell to 32.4 in 2023
* The market's weekly gross change increased by 135% with the release of "Ant-Man and the Wasp: Quantumania" on February 17

""")
