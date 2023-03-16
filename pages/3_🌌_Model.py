import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import pickle
from PIL import Image
# Theme
theme_plotly = None  # None or streamlit

# Layout
st.set_page_config(page_title='🌌 Model - NCAA_Basketball',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('🌌 Model')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache_data()
def get_data(query):
    if query == 'Total_Genre':
        return pd.read_csv('https://raw.githubusercontent.com/Kaizen-Step/Hollywood_Box_Office_Tragedy/main/Data/Geners/Genre-Total.csv')
    elif query == 'Number_of_Release':
        return pd.read_csv('https://raw.githubusercontent.com/Kaizen-Step/Hollywood_Box_Office_Tragedy/main/Data/Geners/Genre-Total2.csv')
    elif query == 'average_per_release':
        return pd.read_csv('https://raw.githubusercontent.com/Kaizen-Step/Hollywood_Box_Office_Tragedy/main/Data/Geners/Genre-Total3.csv')
    return None


Total_Genre = get_data('Total_Genre')
Number_of_Release = get_data('Number_of_Release')
average_per_release = get_data('average_per_release')


df = Total_Genre
df2 = Number_of_Release
df3 = average_per_release
##########################################################################
st.write(""" ### Machine Learning Model  ##  """)

st.write("""
  Machine learning can be used to predict the outcome of basketball matches by training a model on historical data of past games. The model can analyze various factors such as team rankings, player statistics, and game conditions to identify patterns that may influence the game's result.
The process of creating a basketball prediction model involves:     
* Collecting data: Gathering data on past basketball games, including team rankings, player statistics, and game conditions  
* Preprocessing data: Cleaning and preparing the data for analysis by handling missing values and converting it into a suitable format  
* Feature engineering: Identifying the relevant features that can be used to train the model and engineering new features based on domain knowledge  
* Model selection: Choosing an appropriate machine learning algorithm, such as decision trees, support vector machines, or neural networks, to train the model  
* Training: Feeding the data into the chosen model and adjusting its parameters to optimize its performance  
* Evaluation: Testing the model's performance on a separate set of data to assess its accuracy and generalization ability  
* Deployment: Integrating the trained model into a larger system or application, where it can be used to make predictions on new basketball matches  
  """)


st.info(""" ##### In This Model Section you can find: ####    

 
    * Model Demonstraion
    * Training the Model
    * Future Plan
    
    """)
#################################################################################################
st.write(""" ### Model Demonstraion ##  """)

st.write("""
The neural network used consists of five neurons with a 20 percent dropout rate. Since we have access to a limited amount of data, the model cannot be too deep in order to avoid overfitting. In the following plots, you can see accuracy and loss values during the training process. Both of the training and validation sets converge to satisfactory values. The prediction on the test dataset set showed approximately 75 percent, which sounds acceptable.
  """)

st.write(""" ### Training the Model ##  """)

st.write("""
The dataset extracted by scraping has been used for this project. There are 44 columns in total in the dataset. Through sensitivity analysis and some trials and errors, several columns that were not as effective as others were removed. The remaining columns (features) are: RK1, Win_Rate1, 2P%1, 2P%D1, 3P%1, 3P%D1, ADJT.1, WAB1, RK2, Win_Rate2, 2P%2, 2P%D2, 3P%2, 3P%D2, ADJT.2, WAB2, Venue_Home, Venue_Away, and Venue_Neutral
Win_Rate1 and Win_Rate2 are the number of wins divided by the total number of games of each team. The other features are extracted from the
barttorvik website.
  """)

# load
with open('Data/Prediction/Model History/trainHistoryDict', "rb") as file_pi:
    history = pickle.load(file_pi)


c1, c2 = st.columns(2)

with c1:
    # Plot accuracy
    st.write(" ### Accuracy")
    fig = go.Figure()

    for accuracy in [history['accuracy'], history['val_accuracy']]:
        fig = fig.add_trace(go.Scatter(y=accuracy))

    fig.update_layout(legend_title=None, xaxis_title='Epoch',
                      yaxis_title='Accuracy')

    st.plotly_chart(fig)

with c2:
    # Plot loss
    st.write(" ### Loss")
    fig = go.Figure()

    for loss in [history['loss'], history['val_loss']]:

        fig = fig.add_trace(go.Scatter(y=loss))

    fig.update_layout(legend_title=None, xaxis_title='Epoch',
                      yaxis_title='Loss')

    st.plotly_chart(fig)


st.write("""  The loss and accuracy plots of some deeper networks are displayed here. You can see that since there is only a limited amount of data, the model can easily overfit. These plots show the accuracy of the model with 128 neurons in the hidden layer. In the bottom one, a dropout layer with a 20 percent dropout rate has been added. Despite alleviating the overfitting a little bit, it is still overfitting, as there is a significant difference between the training and validation dataset results.In the following picture, you can see the summary of the model.	 """)

c1, c2 = st.columns(2)
with c1:
    st.image(Image.open('Images/128 neurons - 1 layer - no drop out.png'), )
with c2:

    st.image(Image.open(
        'Images/128 neurons - 1 layer - with 20 percent drop out.png'), )

#####################################################

st.write(""" ### Future Plan ##  """)


st.write("""  In the following picture, you can see the summary of the model. The model used to predict the 34 matches in March Madness 2023 In the future, one of the best choices might be to use the pretrained model from decades and then put new teams and data in the last layer to predict the match result with better performance. In our future work, we will use data from decades ago to build a model with higher accuracy. and try different approaches like decision trees and others. """)

c1, c2, c3 = st.columns(3)
with c2:
    st.image(Image.open('Images/model_plot.png'), )
