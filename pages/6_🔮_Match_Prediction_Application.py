# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import tensorflow as tf
import pandas as pd
import pickle

# Theme
theme_plotly = None  # None or streamlit


# Layout
st.set_page_config(page_title=' Match Prediction Application -  NCAA_Basketball',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('🔮 Match Prediction Application')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'Daily_2022':
        return pd.read_csv('Data/March_Madness2023_Team/2023_Teams.csv')
    elif query == 'Teams_2023':
        return pd.read_csv('Data/2023_NCAA_Match/team_names.csv')
    elif query == 'table':
        return pd.read_csv('https://raw.githubusercontent.com/Kaizen-Step/Hollywood_Box_Office_Tragedy/main/Data/Domestic/Y22/Y22-Weekly2.csv')
    return None


Daily_2022 = get_data('Daily_2022')
Teams_2023 = get_data('Teams_2023')
table = get_data('table')

df = Daily_2022
df2 = Teams_2023
df3 = table


#################################################################################################
st.write(""" ### March Madness 2023 Match Prediction Appication ##  """)

st.write(""" Welcome to our NCAA match prediction application, powered by machine learning! Our application uses sophisticated algorithms to analyze vast amounts of historical data on NCAA teams, players, and games to provide accurate predictions for upcoming matches. By training our models on a variety of factors such as team statistics, player performance, and home court advantage, we are able to provide valuable insights into which teams are most likely to win a given match.




  """)


st.info(""" ##### In This Review 2022 Section you can find: ####

* Daily Top 10 Movie Grosss in 2022 [USD]
* Daily Number of Movie Released
* 2022 Weekly Figures
* Top First Sold Movie each Week [Detailed Table]



""")


#################################################################################################


# User Interface

c1, c2 = st.columns(2)

with c1:
    st.write(""" ### Please Choose the Team Number One   
         """)
    team1 = st.selectbox(
        ' Team 1', options=df2["team_name"], index=4)


with c2:
    st.write(""" ### Please Choose the Team Number Two     
              """)
    team2 = st.selectbox(
        'Team 2', options=df2["team_name"], index=25)


c1, c2, c3 = st.columns(3)

with c2:
    st.write(" ### Please Choose Team One Venue  ")
    venue = st.selectbox('Venue', options=[
        'Home', 'Away', 'Neutral'])


#####################################################################################


#################################################################################################

# Predict Function


############################################################################################################
c1, c2, c3 = st.columns(3)


# with c1:
# if Apartment == 0:
#     if round_predction > 500000:
#         st.image(Image.open('Images/apartmentluxury.jpg'), width=500)
#     elif round_predction > 400000:
#         st.image(Image.open('Images/apartment2.jpg'), width=500)
#     elif round_predction > 300000:
#         st.image(Image.open('Images/apartment3.jpg'), width=500)
#     elif round_predction > 200000:
#         st.image(Image.open('Images/apartment4.jpg'), width=500)
#     elif round_predction > 10000:
#         st.image(Image.open('Images/apartment5.jpg'), width=500)
# elif Apartment == 1:
#     if round_predction > 500000:
#         st.image(Image.open('Images/houseluxury.jpg'), width=500)
#     elif round_predction > 400000:
#         st.image(Image.open('Images/h2.jpg'), width=500)
#     elif round_predction > 300000:
#         st.image(Image.open('Images/h3.jpg'), width=500)
#     elif round_predction > 200000:
#         st.image(Image.open('Images/h4.jpg'), width=500)
#     elif round_predction > 10000:
#         st.image(Image.open('Images/h5.jpg'), width=500)

with c2:

    st.write(" # VS")

# with c3:
#     st.info(
#         f""" ###       {round_predction}\$   """)

    # if Apartment == 0:
    #     if round_predction > 500000:
    #         st.image(Image.open('Images/apartmentluxury.jpg'), width=500)
    #     elif round_predction > 400000:
    #         st.image(Image.open('Images/apartment2.jpg'), width=500)
    #     elif round_predction > 300000:
    #         st.image(Image.open('Images/apartment3.jpg'), width=500)
    #     elif round_predction > 200000:
    #         st.image(Image.open('Images/apartment4.jpg'), width=500)
    #     elif round_predction > 10000:
    #         st.image(Image.open('Images/apartment5.jpg'), width=500)
    # elif Apartment == 1:
    #     if round_predction > 500000:
    #         st.image(Image.open('Images/houseluxury.jpg'), width=500)
    #     elif round_predction > 400000:
    #         st.image(Image.open('Images/h2.jpg'), width=500)
    #     elif round_predction > 300000:
    #         st.image(Image.open('Images/h3.jpg'), width=500)
    #     elif round_predction > 200000:
    #         st.image(Image.open('Images/h4.jpg'), width=500)
    #     elif round_predction > 10000:
    #         st.image(Image.open('Images/h5.jpg'), width=500)
