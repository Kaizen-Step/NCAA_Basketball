import tensorflow as tf
import pandas as pd
import pickle


# Helper functions
def normalize_data(df, df_mean, df_std):


    normalized_df= (df-df_mean) / df_std

    return normalized_df


def convert_team_names_proper_input_x(team1_name, team2_name, venue='Home'):

    team_stats_2023 = pd.read_csv('existing_data/team_stats_2023.csv')

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
    x_input_df['RK1'] = x_input_df['RK1'].replace([team_name for team_name in team_stats_2023['TEAM']], [rk for rk in team_stats_2023['RK']])

    x_input_df['Win_Rate1'] = x_input_df['Win_Rate1'].replace([team_name for team_name in team_stats_2023['TEAM']], [win_rate for win_rate in team_stats_2023['REC']])

    # Modfiy win rate
    x_input_df['Win_Rate1'] = (x_input_df['Win_Rate1'].str.split(
    '-').str[0].astype(float))/(x_input_df['Win_Rate1'].str.split('-').str[1].astype(float) + x_input_df['Win_Rate1'].str.split('-').str[0].astype(float))

    x_input_df['ADJOE1'] = x_input_df['ADJOE1'].replace([team_name for team_name in team_stats_2023['TEAM']], [adjoe for adjoe in team_stats_2023['ADJOE']])

    x_input_df['ADJDE1'] = x_input_df['ADJDE1'].replace([team_name for team_name in team_stats_2023['TEAM']], [adjde for adjde in team_stats_2023['ADJDE']])

    x_input_df['BARTHAG1'] = x_input_df['BARTHAG1'].replace([team_name for team_name in team_stats_2023['TEAM']], [barthag for barthag in team_stats_2023['BARTHAG']])

    x_input_df['BARTHAG1'] = x_input_df['BARTHAG1'].replace([team_name for team_name in team_stats_2023['TEAM']], [barthag for barthag in team_stats_2023['BARTHAG']])

    x_input_df['EFG%1'] = x_input_df['EFG%1'].replace([team_name for team_name in team_stats_2023['TEAM']], [efg for efg in team_stats_2023['EFG%']])

    x_input_df['EFGD%1'] = x_input_df['EFGD%1'].replace([team_name for team_name in team_stats_2023['TEAM']], [efgd for efgd in team_stats_2023['EFGD%']])

    x_input_df['TOR1'] = x_input_df['TOR1'].replace([team_name for team_name in team_stats_2023['TEAM']], [tor for tor in team_stats_2023['TOR']])

    x_input_df['TORD1'] = x_input_df['TORD1'].replace([team_name for team_name in team_stats_2023['TEAM']], [tord for tord in team_stats_2023['TORD']])

    x_input_df['ORB1'] = x_input_df['ORB1'].replace([team_name for team_name in team_stats_2023['TEAM']], [orb for orb in team_stats_2023['ORB']])

    x_input_df['DRB1'] = x_input_df['DRB1'].replace([team_name for team_name in team_stats_2023['TEAM']], [drb for drb in team_stats_2023['DRB']])

    x_input_df['FTR1'] = x_input_df['FTR1'].replace([team_name for team_name in team_stats_2023['TEAM']], [ftr for ftr in team_stats_2023['FTR']])

    x_input_df['FTRD1'] = x_input_df['FTRD1'].replace([team_name for team_name in team_stats_2023['TEAM']], [ftrd for ftrd in team_stats_2023['FTRD']])

    x_input_df['2P%1'] = x_input_df['2P%1'].replace([team_name for team_name in team_stats_2023['TEAM']], [two_p for two_p in team_stats_2023['2P%']])

    x_input_df['2P%D1'] = x_input_df['2P%D1'].replace([team_name for team_name in team_stats_2023['TEAM']], [two_pd for two_pd in team_stats_2023['2P%D']])

    x_input_df['2P%1'] = x_input_df['2P%1'].replace([team_name for team_name in team_stats_2023['TEAM']], [drb for drb in team_stats_2023['2P%']])

    x_input_df['3P%1'] = x_input_df['3P%1'].replace([team_name for team_name in team_stats_2023['TEAM']], [three_p for three_p in team_stats_2023['3P%']])

    x_input_df['3P%D1'] = x_input_df['3P%D1'].replace([team_name for team_name in team_stats_2023['TEAM']], [three_pd for three_pd in team_stats_2023['3P%D']])

    x_input_df['ADJ T.1'] = x_input_df['ADJ T.1'].replace([team_name for team_name in team_stats_2023['TEAM']], [adj for adj in team_stats_2023['ADJ T.']])

    x_input_df['WAB1'] = x_input_df['WAB1'].replace([team_name for team_name in team_stats_2023['TEAM']], [wab for wab in team_stats_2023['WAB']])

    # Team 2
    x_input_df['RK2'] = x_input_df['RK2'].replace([team_name for team_name in team_stats_2023['TEAM']], [rk for rk in team_stats_2023['RK']])

    x_input_df['Win_Rate2'] = x_input_df['Win_Rate2'].replace([team_name for team_name in team_stats_2023['TEAM']], [win_rate for win_rate in team_stats_2023['REC']])

    # Modfiy win rate
    x_input_df['Win_Rate2'] = (x_input_df['Win_Rate2'].str.split(
    '-').str[0].astype(float))/(x_input_df['Win_Rate2'].str.split('-').str[1].astype(float) + x_input_df['Win_Rate2'].str.split('-').str[0].astype(float))

    x_input_df['ADJOE2'] = x_input_df['ADJOE2'].replace([team_name for team_name in team_stats_2023['TEAM']], [adjoe for adjoe in team_stats_2023['ADJOE']])

    x_input_df['ADJDE2'] = x_input_df['ADJDE2'].replace([team_name for team_name in team_stats_2023['TEAM']], [adjde for adjde in team_stats_2023['ADJDE']])

    x_input_df['BARTHAG2'] = x_input_df['BARTHAG2'].replace([team_name for team_name in team_stats_2023['TEAM']], [barthag for barthag in team_stats_2023['BARTHAG']])

    x_input_df['EFG%2'] = x_input_df['EFG%2'].replace([team_name for team_name in team_stats_2023['TEAM']], [efg for efg in team_stats_2023['EFG%']])

    x_input_df['EFGD%2'] = x_input_df['EFGD%2'].replace([team_name for team_name in team_stats_2023['TEAM']], [efgd for efgd in team_stats_2023['EFGD%']])

    x_input_df['TOR2'] = x_input_df['TOR2'].replace([team_name for team_name in team_stats_2023['TEAM']], [tor for tor in team_stats_2023['TOR']])

    x_input_df['TORD2'] = x_input_df['TORD2'].replace([team_name for team_name in team_stats_2023['TEAM']], [tord for tord in team_stats_2023['TORD']])

    x_input_df['ORB2'] = x_input_df['ORB2'].replace([team_name for team_name in team_stats_2023['TEAM']], [orb for orb in team_stats_2023['ORB']])

    x_input_df['DRB2'] = x_input_df['DRB2'].replace([team_name for team_name in team_stats_2023['TEAM']], [drb for drb in team_stats_2023['DRB']])

    x_input_df['FTR2'] = x_input_df['FTR2'].replace([team_name for team_name in team_stats_2023['TEAM']], [ftr for ftr in team_stats_2023['FTR']])

    x_input_df['FTRD2'] = x_input_df['FTRD2'].replace([team_name for team_name in team_stats_2023['TEAM']], [ftrd for ftrd in team_stats_2023['FTRD']])

    x_input_df['2P%2'] = x_input_df['2P%2'].replace([team_name for team_name in team_stats_2023['TEAM']], [two_p for two_p in team_stats_2023['2P%']])

    x_input_df['2P%D2'] = x_input_df['2P%D2'].replace([team_name for team_name in team_stats_2023['TEAM']], [two_pd for two_pd in team_stats_2023['2P%D']])

    x_input_df['2P%2'] = x_input_df['2P%2'].replace([team_name for team_name in team_stats_2023['TEAM']], [drb for drb in team_stats_2023['2P%']])

    x_input_df['3P%2'] = x_input_df['3P%2'].replace([team_name for team_name in team_stats_2023['TEAM']], [three_p for three_p in team_stats_2023['3P%']])

    x_input_df['3P%D2'] = x_input_df['3P%D2'].replace([team_name for team_name in team_stats_2023['TEAM']], [three_pd for three_pd in team_stats_2023['3P%D']])

    x_input_df['ADJ T.2'] = x_input_df['ADJ T.2'].replace([team_name for team_name in team_stats_2023['TEAM']], [adj for adj in team_stats_2023['ADJ T.']])

    x_input_df['WAB2'] = x_input_df['WAB2'].replace([team_name for team_name in team_stats_2023['TEAM']], [wab for wab in team_stats_2023['WAB']])

    # Add venue column
    x_input_df['Venue_Home'] = [int(venue=='Home')]
    x_input_df['Venue_Away'] = [int(venue=='Away')]
    x_input_df['Venue_Neutral'] = [int(venue=='Neutral')]

    # Team Names Must Be Removed
    x_input_df = x_input_df.drop(['TEAM1', 'TEAM2'], axis=1)

    # Load mean and std values for prediction purposes
    with open('Model History/mean_std_vals', 'rb') as file_stat:
        dataset_stats = pickle.load(file_stat)
    
    # Normalize
    x_input_df = normalize_data(x_input_df, dataset_stats['df_mean'], dataset_stats['df_std'])

    return x_input_df


def load_model(input_shape):

    # Create the TensorFlow model (Should be compatible with the weights that will be loaded)
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(1, activation='relu',
                            input_shape=input_shape),
        # tf.keras.layers.Dense(256, activation='relu'),
        # tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    try:
        # Save the weights using the `checkpoint_path` format
        checkpoint_path = "Model History/cp.ckpt"

        # How to load
        # Loads the weights
        model.load_weights(checkpoint_path)

    except:
        raise Exception("Unable to load weights from this address: '{}' \n Or maybe the weights are not compatible with the model ...".format(checkpoint_path))
       
    return model



def predict(team1, team2, venue='Home'):
    # Preprocess the data
    # Load the basketball dataset
    basketball_data = pd.read_csv('Data/generated_df.csv')

    X = basketball_data.drop(['Match_Result', 'TEAM1', 'TEAM2'], axis=1)

    model = load_model(input_shape=(X.shape[1], ))
    # print(abs(model.weights[0][:, 0]))

    # Create x input (Venue should be one of these: 'Home', 'Away', 'Neutral')
    x_input_df = convert_team_names_proper_input_x(team1, team2, venue)

    prediction = model.predict(x_input_df)

    prediction = prediction[0][0]

    return prediction


prediction = predict('Houston', 'Alabama', venue='Away')

# print('Prediction: {}'.format(prediction))