# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import tensorflow as tf
import pandas as pd
import pickle
from PIL import Image


# Theme
theme_plotly = None  # None or streamlit


# Layout
st.set_page_config(page_title=' Match Prediction Application -  Who Will Win 2023 March Madness',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('🔮 Match Prediction Application')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache_data()
def get_data(query):
    if query == 'March2023_Team':
        return pd.read_csv('Data/March_Madness2023_Team/2023_Teams.csv')
    elif query == 'Teams_2023':
        return pd.read_csv('Data/2023_NCAA_Match/team_names.csv')

    return None


March2023_Team = get_data('March2023_Team')
Teams_2023 = get_data('Teams_2023')
table = get_data('table')

df11 = March2023_Team
df12 = Teams_2023
df13 = table


#################################################################################################
st.write(""" ### March Madness 2023 Match Prediction Appication ##  """)

st.write(""" Welcome to our NCAA match prediction application, powered by machine learning! Our application uses sophisticated algorithms to analyze vast amounts of historical data on NCAA teams, players, and games to provide accurate predictions for upcoming matches. By training our models on a variety of factors such as team statistics, player performance, and home court advantage, we are able to provide valuable insights into which teams are most likely to win a given match.




  """)


#################################################################################################


# User Interface


c1, c2 = st.columns(2)

with c1:
    st.write(""" ### Please Choose the Team Number One   
         """)
    team1 = st.selectbox(
        ' Team 1', options=df12["team_name"], index=9)


with c2:
    st.write(""" ### Please Choose the Team Number Two     
              """)
    team2 = st.selectbox(
        'Team 2', options=df12["team_name"], index=0)

c1, c2, c3 = st.columns(3)
with c2:
    st.write(" ### Please Choose Team One Venue  ")
    venue = st.selectbox('Venue', options=[
        'Home', 'Away', 'Neutral'])


#####################################################################################

st.text(" \n")

# Team in Highlight

c1, c2, c3 = st.columns(3)

with c1:
    if team1 == "Houston":
        st.image(Image.open("Logos/Houston Cougars.png"), width=500)
    elif team1 == "Alabama":
        st.image(Image.open("Logos/Alabama A&M Bulldogs.png"), width=500)
    elif team1 == "UCLA":
        st.image(Image.open("Logos/UCLA Bruins.png"), width=500)
    elif team1 == "Tennessee":
        st.image(Image.open("Logos/Tennessee State Tigers.png"), width=500)
    elif team1 == "Connecticut":
        st.image(Image.open("Logos/Colgate Raiders.png"), width=500)
    elif team1 == "Purdue":
        st.image(Image.open("Logos/Purdue Boilermakers.png"), width=500)
    elif team1 == "Gonzaga":
        st.image(Image.open("Logos/Gonzaga Bulldogs.png"), width=500)
    elif team1 == "Saint Mary's":
        st.image(Image.open("Logos/Syracuse Orange.png"), width=500)
    elif team1 == "San Diego St.":
        st.image(Image.open("Logos/San Diego State Aztecs.png"), width=500)
    elif team1 == "Arizona":
        st.image(Image.open("Logos/Arizona Wildcats.png"), width=500)
    elif team1 == "Texas":
        st.image(Image.open("Logos/Texas Longhorns.png"), width=500)
    elif team1 == "Kansas":
        st.image(Image.open("Logos/Kansas City Roos.png"), width=500)
    elif team1 == "Baylor":
        st.image(Image.open("Logos/Baylor Bears.png"), width=500)
    elif team1 == "Creighton":
        st.image(Image.open("Logos/Cal State Northridge Matadors.png"), width=500)
    elif team1 == "Marquette":
        st.image(Image.open("Logos/Maryland Terrapins.png"), width=500)
    elif team1 == "Texas A&M":
        st.image(Image.open("Logos/Texas A&M Aggies.png"), width=500)
    elif team1 == "Xavier":
        st.image(Image.open("Logos/Xavier Musketeers.png"), width=500)
    elif team1 == "Arkansas":
        st.image(Image.open("Logos/Arkansas Razorbacks.png"), width=500)
    elif team1 == "West Virginia":
        st.image(Image.open("Logos/West Virginia Mountaineers.png"), width=500)
    elif team1 == "Iowa St.":
        st.image(Image.open("Logos/Iowa State Cyclones.png"), width=500)
    elif team1 == "Auburn":
        st.image(Image.open("Logos/Auburn Tigers.png"), width=500)
    elif team1 == "Kansas St.":
        st.image(Image.open("Logos/Kansas State Wildcats.png"), width=500)
    elif team1 == "Duke":
        st.image(Image.open("Logos/Duquesne Dukes.png"), width=500)
    elif team1 == "Utah St.":
        st.image(Image.open("Logos/Utah State Aggies.png"), width=500)
    elif team1 == "Memphis":
        st.image(Image.open("Logos/Memphis Tigers.png"), width=500)
    elif team1 == "TCU":
        st.image(Image.open("Logos/TCU Horned Frogs.png"), width=500)
    elif team1 == "Kentucky":
        st.image(Image.open("Logos/Northern Kentucky Norse.png"), width=500)
    elif team1 == "Virginia":
        st.image(Image.open("Logos/Virginia Commonwealth Rams.png"), width=500)
    elif team1 == "Maryland":
        st.image(Image.open("Logos/Maryland Terrapins.png"), width=500)


with c2:

    st.image(Image.open('Images/VS6.png'))

with c3:
    if team2 == "Houston":
        st.image(Image.open("Logos/Houston Cougars.png"), width=500)
    elif team2 == "Alabama":
        st.image(Image.open("Logos/Alabama A&M Bulldogs.png"), width=500)
    elif team2 == "UCLA":
        st.image(Image.open("Logos/UCLA Bruins.png"), width=500)
    elif team2 == "Tennessee":
        st.image(Image.open("Logos/Tennessee State Tigers.png"), width=500)
    elif team2 == "Connecticut":
        st.image(Image.open("Logos/Colgate Raiders.png"), width=500)
    elif team2 == "Purdue":
        st.image(Image.open("Logos/Purdue Boilermakers.png"), width=500)
    elif team2 == "Gonzaga":
        st.image(Image.open("Logos/Gonzaga Bulldogs.png"), width=500)
    elif team2 == "Saint Mary's":
        st.image(Image.open("Logos/Syracuse Orange.png"), width=500)
    elif team2 == "San Diego St.":
        st.image(Image.open("Logos/San Diego State Aztecs.png"), width=500)
    elif team2 == "Arizona":
        st.image(Image.open("Logos/Arizona Wildcats.png"), width=500)
    elif team2 == "Texas":
        st.image(Image.open("Logos/Texas Longhorns.png"), width=500)
    elif team2 == "Kansas":
        st.image(Image.open("Logos/Kansas City Roos.png"), width=500)
    elif team2 == "Baylor":
        st.image(Image.open("Logos/Baylor Bears.png"), width=500)
    elif team2 == "Creighton":
        st.image(Image.open("Logos/Cal State Northridge Matadors.png"), width=500)
    elif team2 == "Marquette":
        st.image(Image.open("Logos/Maryland Terrapins.png"), width=500)
    elif team2 == "Texas A&M":
        st.image(Image.open("Logos/Texas A&M Aggies.png"), width=500)
    elif team2 == "Xavier":
        st.image(Image.open("Logos/Xavier Musketeers.png"), width=500)
    elif team2 == "Arkansas":
        st.image(Image.open("Logos/Arkansas Razorbacks.png"), width=500)
    elif team2 == "West Virginia":
        st.image(Image.open("Logos/West Virginia Mountaineers.png"), width=500)
    elif team2 == "Iowa St.":
        st.image(Image.open("Logos/Iowa State Cyclones.png"), width=500)
    elif team2 == "Auburn":
        st.image(Image.open("Logos/Auburn Tigers.png"), width=500)
    elif team2 == "Kansas St.":
        st.image(Image.open("Logos/Kansas State Wildcats.png"), width=500)
    elif team2 == "Duke":
        st.image(Image.open("Logos/Duquesne Dukes.png"), width=500)
    elif team2 == "Utah St.":
        st.image(Image.open("Logos/Utah State Aggies.png"), width=500)
    elif team2 == "Memphis":
        st.image(Image.open("Logos/Memphis Tigers.png"), width=500)
    elif team2 == "TCU":
        st.image(Image.open("Logos/TCU Horned Frogs.png"), width=500)
    elif team2 == "Kentucky":
        st.image(Image.open("Logos/Northern Kentucky Norse.png"), width=500)
    elif team2 == "Virginia":
        st.image(Image.open("Logos/Virginia Commonwealth Rams.png"), width=500)
    elif team2 == "Maryland":
        st.image(Image.open("Logos/Maryland Terrapins.png"), width=500)


c1, c2, c3 = st.columns(3)

with c1:
    st.write(f" # {team1} ")
    st.text(" \n")

with c3:
    st.write(f" # {team2} ")
    st.text(" \n")

################################################

# Prediction Result

# Helper functions


def normalize_data(df, df_mean, df_std):

    normalized_df = (df-df_mean) / df_std

    return normalized_df


def convert_team_names_proper_input_x(team1_name, team2_name, venue='Home'):

    team_stats_2023 = pd.read_csv(
        'Data/Prediction/existing_data/team_stats_2023.csv')

    # The columns of x input (template)
    x_input_col_names = [
        'RK1', 'TEAM1', 'Win_Rate1', 'ADJOE1', 'ADJDE1', 'BARTHAG1', 'EFG%1', 'EFGD%1', 'TOR1', 'TORD1',
        'ORB1', 'DRB1', 'FTR1', 'FTRD1', '2P%1', '2P%D1', '3P%1', '3P%D1', 'ADJ T.1', 'WAB1',
        'RK2', 'TEAM2', 'Win_Rate2', 'ADJOE2', 'ADJDE2', 'BARTHAG2', 'EFG%2', 'EFGD%2', 'TOR2', 'TORD2',
        'ORB2', 'DRB2', 'FTR2', 'FTRD2', '2P%2', '2P%D2', '3P%2', '3P%D2', 'ADJ T.2', 'WAB2',
        'Venue_Home', 'Venue_Away', 'Venue_Neutral',
    ]

    x_input_df = pd.DataFrame(columns=x_input_col_names)

    # Adding the corresponding values of each column (using the total games dataset)
    # x_input_df['RK1'] = all_games_df['RK']
    x_input_df['TEAM1'] = [team1_name]
    x_input_df['TEAM2'] = [team2_name]

    # Use team_stats table to add team stats of both home and away teams. First we put the team name in each column of home and away team
    # Then replace it with the corresponding value from team stats dataset
    # Not that two tables are being mapped here (all games table and stats table)

    # Team 1
    x_input_df['RK1'] = [team1_name]
    x_input_df['Win_Rate1'] = [team1_name]
    x_input_df['ADJOE1'] = [team1_name]
    x_input_df['ADJDE1'] = [team1_name]
    x_input_df['BARTHAG1'] = [team1_name]
    x_input_df['EFG%1'] = [team1_name]
    x_input_df['EFGD%1'] = [team1_name]
    x_input_df['TOR1'] = [team1_name]
    x_input_df['TORD1'] = [team1_name]
    x_input_df['ORB1'] = [team1_name]
    x_input_df['DRB1'] = [team1_name]
    x_input_df['FTR1'] = [team1_name]
    x_input_df['FTRD1'] = [team1_name]
    x_input_df['2P%1'] = [team1_name]
    x_input_df['2P%D1'] = [team1_name]
    x_input_df['3P%1'] = [team1_name]
    x_input_df['3P%D1'] = [team1_name]
    x_input_df['ADJ T.1'] = [team1_name]
    x_input_df['WAB1'] = [team1_name]

    # Team 2
    x_input_df['RK2'] = [team2_name]
    x_input_df['Win_Rate2'] = [team2_name]
    x_input_df['ADJOE2'] = [team2_name]
    x_input_df['ADJDE2'] = [team2_name]
    x_input_df['BARTHAG2'] = [team2_name]
    x_input_df['EFG%2'] = [team2_name]
    x_input_df['EFGD%2'] = [team2_name]
    x_input_df['TOR2'] = [team2_name]
    x_input_df['TORD2'] = [team2_name]
    x_input_df['ORB2'] = [team2_name]
    x_input_df['DRB2'] = [team2_name]
    x_input_df['FTR2'] = [team2_name]
    x_input_df['FTRD2'] = [team2_name]
    x_input_df['2P%2'] = [team2_name]
    x_input_df['2P%D2'] = [team2_name]
    x_input_df['3P%2'] = [team2_name]
    x_input_df['3P%D2'] = [team2_name]
    x_input_df['ADJ T.2'] = [team2_name]
    x_input_df['WAB2'] = [team2_name]

    # Replacing the values from stats column
    # Team 1
    x_input_df['RK1'] = x_input_df['RK1'].replace(
        [team_name for team_name in team_stats_2023['TEAM']], [rk for rk in team_stats_2023['RK']])

    x_input_df['Win_Rate1'] = x_input_df['Win_Rate1'].replace(
        [team_name for team_name in team_stats_2023['TEAM']], [win_rate for win_rate in team_stats_2023['REC']])

    # Modfiy win rate
    x_input_df['Win_Rate1'] = (x_input_df['Win_Rate1'].str.split(
        '-').str[0].astype(float))/(x_input_df['Win_Rate1'].str.split('-').str[1].astype(float) + x_input_df['Win_Rate1'].str.split('-').str[0].astype(float))

    x_input_df['ADJOE1'] = x_input_df['ADJOE1'].replace(
        [team_name for team_name in team_stats_2023['TEAM']], [adjoe for adjoe in team_stats_2023['ADJOE']])

    x_input_df['ADJDE1'] = x_input_df['ADJDE1'].replace(
        [team_name for team_name in team_stats_2023['TEAM']], [adjde for adjde in team_stats_2023['ADJDE']])

    x_input_df['BARTHAG1'] = x_input_df['BARTHAG1'].replace([team_name for team_name in team_stats_2023['TEAM']], [
                                                            barthag for barthag in team_stats_2023['BARTHAG']])

    x_input_df['EFG%1'] = x_input_df['EFG%1'].replace(
        [team_name for team_name in team_stats_2023['TEAM']], [efg for efg in team_stats_2023['EFG%']])

    x_input_df['EFGD%1'] = x_input_df['EFGD%1'].replace(
        [team_name for team_name in team_stats_2023['TEAM']], [efgd for efgd in team_stats_2023['EFGD%']])

    x_input_df['TOR1'] = x_input_df['TOR1'].replace(
        [team_name for team_name in team_stats_2023['TEAM']], [tor for tor in team_stats_2023['TOR']])

    x_input_df['TORD1'] = x_input_df['TORD1'].replace(
        [team_name for team_name in team_stats_2023['TEAM']], [tord for tord in team_stats_2023['TORD']])

    x_input_df['ORB1'] = x_input_df['ORB1'].replace(
        [team_name for team_name in team_stats_2023['TEAM']], [orb for orb in team_stats_2023['ORB']])

    x_input_df['DRB1'] = x_input_df['DRB1'].replace(
        [team_name for team_name in team_stats_2023['TEAM']], [drb for drb in team_stats_2023['DRB']])

    x_input_df['FTR1'] = x_input_df['FTR1'].replace(
        [team_name for team_name in team_stats_2023['TEAM']], [ftr for ftr in team_stats_2023['FTR']])

    x_input_df['FTRD1'] = x_input_df['FTRD1'].replace(
        [team_name for team_name in team_stats_2023['TEAM']], [ftrd for ftrd in team_stats_2023['FTRD']])

    x_input_df['2P%1'] = x_input_df['2P%1'].replace([team_name for team_name in team_stats_2023['TEAM']], [
                                                    two_p for two_p in team_stats_2023['2P%']])

    x_input_df['2P%D1'] = x_input_df['2P%D1'].replace([team_name for team_name in team_stats_2023['TEAM']], [
                                                      two_pd for two_pd in team_stats_2023['2P%D']])

    x_input_df['3P%1'] = x_input_df['3P%1'].replace([team_name for team_name in team_stats_2023['TEAM']], [
                                                    three_p for three_p in team_stats_2023['3P%']])

    x_input_df['3P%D1'] = x_input_df['3P%D1'].replace([team_name for team_name in team_stats_2023['TEAM']], [
                                                      three_pd for three_pd in team_stats_2023['3P%D']])

    x_input_df['ADJ T.1'] = x_input_df['ADJ T.1'].replace(
        [team_name for team_name in team_stats_2023['TEAM']], [adj for adj in team_stats_2023['ADJ T.']])

    x_input_df['WAB1'] = x_input_df['WAB1'].replace(
        [team_name for team_name in team_stats_2023['TEAM']], [wab for wab in team_stats_2023['WAB']])

    # Team 2
    x_input_df['RK2'] = x_input_df['RK2'].replace(
        [team_name for team_name in team_stats_2023['TEAM']], [rk for rk in team_stats_2023['RK']])

    x_input_df['Win_Rate2'] = x_input_df['Win_Rate2'].replace(
        [team_name for team_name in team_stats_2023['TEAM']], [win_rate for win_rate in team_stats_2023['REC']])

    # Modfiy win rate
    x_input_df['Win_Rate2'] = (x_input_df['Win_Rate2'].str.split(
        '-').str[0].astype(float))/(x_input_df['Win_Rate2'].str.split('-').str[1].astype(float) + x_input_df['Win_Rate2'].str.split('-').str[0].astype(float))

    x_input_df['ADJOE2'] = x_input_df['ADJOE2'].replace(
        [team_name for team_name in team_stats_2023['TEAM']], [adjoe for adjoe in team_stats_2023['ADJOE']])

    x_input_df['ADJDE2'] = x_input_df['ADJDE2'].replace(
        [team_name for team_name in team_stats_2023['TEAM']], [adjde for adjde in team_stats_2023['ADJDE']])

    x_input_df['BARTHAG2'] = x_input_df['BARTHAG2'].replace([team_name for team_name in team_stats_2023['TEAM']], [
                                                            barthag for barthag in team_stats_2023['BARTHAG']])

    x_input_df['EFG%2'] = x_input_df['EFG%2'].replace(
        [team_name for team_name in team_stats_2023['TEAM']], [efg for efg in team_stats_2023['EFG%']])

    x_input_df['EFGD%2'] = x_input_df['EFGD%2'].replace(
        [team_name for team_name in team_stats_2023['TEAM']], [efgd for efgd in team_stats_2023['EFGD%']])

    x_input_df['TOR2'] = x_input_df['TOR2'].replace(
        [team_name for team_name in team_stats_2023['TEAM']], [tor for tor in team_stats_2023['TOR']])

    x_input_df['TORD2'] = x_input_df['TORD2'].replace(
        [team_name for team_name in team_stats_2023['TEAM']], [tord for tord in team_stats_2023['TORD']])

    x_input_df['ORB2'] = x_input_df['ORB2'].replace(
        [team_name for team_name in team_stats_2023['TEAM']], [orb for orb in team_stats_2023['ORB']])

    x_input_df['DRB2'] = x_input_df['DRB2'].replace(
        [team_name for team_name in team_stats_2023['TEAM']], [drb for drb in team_stats_2023['DRB']])

    x_input_df['FTR2'] = x_input_df['FTR2'].replace(
        [team_name for team_name in team_stats_2023['TEAM']], [ftr for ftr in team_stats_2023['FTR']])

    x_input_df['FTRD2'] = x_input_df['FTRD2'].replace(
        [team_name for team_name in team_stats_2023['TEAM']], [ftrd for ftrd in team_stats_2023['FTRD']])

    x_input_df['2P%2'] = x_input_df['2P%2'].replace([team_name for team_name in team_stats_2023['TEAM']], [
                                                    two_p for two_p in team_stats_2023['2P%']])

    x_input_df['2P%D2'] = x_input_df['2P%D2'].replace([team_name for team_name in team_stats_2023['TEAM']], [
                                                      two_pd for two_pd in team_stats_2023['2P%D']])

    x_input_df['3P%2'] = x_input_df['3P%2'].replace([team_name for team_name in team_stats_2023['TEAM']], [
                                                    three_p for three_p in team_stats_2023['3P%']])

    x_input_df['3P%D2'] = x_input_df['3P%D2'].replace([team_name for team_name in team_stats_2023['TEAM']], [
                                                      three_pd for three_pd in team_stats_2023['3P%D']])

    x_input_df['ADJ T.2'] = x_input_df['ADJ T.2'].replace(
        [team_name for team_name in team_stats_2023['TEAM']], [adj for adj in team_stats_2023['ADJ T.']])

    x_input_df['WAB2'] = x_input_df['WAB2'].replace(
        [team_name for team_name in team_stats_2023['TEAM']], [wab for wab in team_stats_2023['WAB']])

    # Add venue column
    x_input_df['Venue_Home'] = [int(venue == 'Home')]
    x_input_df['Venue_Away'] = [int(venue == 'Away')]
    x_input_df['Venue_Neutral'] = [int(venue == 'Neutral')]

    # Team Names Must Be Removed

    # x_input_df = x_input_df.drop(['TEAM1', 'TEAM2'], axis=1)

    # x_input_df = x_input_df.drop(['TEAM1', 'TEAM2',
    #                               'ADJOE1', 'ADJDE1', 'BARTHAG1', 'EFG%1', 'EFGD%1', 'TOR1', 'TORD1', 'ORB1', 'DRB1', 'FTR1', 'FTRD1',
    #                               'ADJOE2', 'ADJDE2', 'BARTHAG2', 'EFG%2', 'EFGD%2', 'TOR2', 'TORD2', 'ORB2', 'DRB2', 'FTR2', 'FTRD2',
    #                               ], axis=1)

    x_input_df = x_input_df[
        ['Win_Rate1', 'ORB1', 'ADJOE1', 'BARTHAG1', 'TOR1', 'ADJDE1',
         'Win_Rate2', 'ORB2', 'ADJOE2', 'BARTHAG2', 'TOR2', 'ADJDE2',
         'Venue_Home', 'Venue_Away', 'Venue_Neutral']
    ]

    # Load mean and std values for prediction purposes
    with open('Data/Prediction/Model History_concat_data/mean_std_vals', 'rb') as file_stat:
        dataset_stats = pickle.load(file_stat)

    # Normalize
    x_input_df = normalize_data(
        x_input_df, dataset_stats['df_mean'], dataset_stats['df_std'])

    return x_input_df


def load_model(input_shape):

    # Create the TensorFlow model (Should be compatible with the weights that will be loaded)
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(5, activation='relu',
                              input_shape=input_shape),
        # tf.keras.layers.Dense(256, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    model.summary()

    checkpoint_path = "Data/Prediction/Model History_concat_data/cp.ckpt"

    model.load_weights(checkpoint_path)

    try:
        # Save the weights using the `checkpoint_path` format

        # How to load
        # Loads the weights
        model.load_weights(checkpoint_path)

    except:
        raise Exception(
            "Unable to load weights from this address: '{}' \n Or maybe the weights are not compatible with the model ...".format(checkpoint_path))

    return model


def predict(team1, team2, venue='Home'):
    # Preprocess the data
    # Load the basketball dataset
    basketball_data = pd.read_csv('Data/Prediction/generated_df.csv')

    # X = basketball_data.drop(['Match_Result', 'TEAM1', 'TEAM2'], axis=1)

    # X = basketball_data.drop(['Match_Result', 'TEAM1', 'TEAM2',
    #                           'ADJOE1', 'ADJDE1', 'BARTHAG1', 'EFG%1', 'EFGD%1', 'TOR1', 'TORD1', 'ORB1', 'DRB1', 'FTR1', 'FTRD1',
    #                           'ADJOE2', 'ADJDE2', 'BARTHAG2', 'EFG%2', 'EFGD%2', 'TOR2', 'TORD2', 'ORB2', 'DRB2', 'FTR2', 'FTRD2',
    #                           ], axis=1)

    X = basketball_data[
        ['Win_Rate1', 'ORB1', 'ADJOE1', 'BARTHAG1', 'TOR1', 'ADJDE1',
         'Win_Rate2', 'ORB2', 'ADJOE2', 'BARTHAG2', 'TOR2', 'ADJDE2',
         'Venue_Home', 'Venue_Away', 'Venue_Neutral']
    ]

    model = load_model(input_shape=(X.shape[1], ))
    # print(abs(model.weights[0][:, 0]))

    # Create x input (Venue should be one of these: 'Home', 'Away', 'Neutral')
    x_input_df = convert_team_names_proper_input_x(team1, team2, venue)

    print(x_input_df)

    prediction = model.predict(x_input_df)

    prediction = prediction[0][0]

    return prediction


new_prediction = predict(team1=team1, team2=team2, venue=venue)


st.write(" ## Wining {} Probability:       {:.3f}".format(
    team1, new_prediction))
