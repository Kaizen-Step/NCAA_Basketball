# Libraries
import streamlit as st
from PIL import Image

# Layout
st.set_page_config(page_title=' NCAA Basketball',
                   page_icon=':bar_chart:📈', layout='wide')
st.title(' NCAA Basketball 🏀')
st.text(" \n")
# Content
c1, c2, c3 = st.columns(3)


with c1:
    st.text(" \n")
    st.text(" \n")
    st.image(Image.open('Images/march1.jpg'))

with c2:
    st.text(" \n")
    st.text(" \n")
    st.image(Image.open('Images/March5.jpg'))
with c3:
    st.text(" \n")
    st.text(" \n")
    st.image(Image.open('Images/Basketball.jpg'))


st.write("""
### NCAA March Madness tournament ###
The NCAA Division I men's basketball tournament, branded as NCAA March Madness and commonly called March Madness, is a single-elimination tournament played each spring in the United States, currently featuring 68 college basketball teams from the Division I level of the National Collegiate Athletic Association (NCAA), to determine the national champion. The tournament was created in 1939 by the National Association of Basketball Coaches, and was the idea of Ohio State coach Harold Olsen. Played mostly during March, it has become one of the most popular annual sporting events in the United States.   
The tournament teams include champions from 32 Division I conferences (which receive automatic bids), and 36 teams which are awarded at-large berths. These "at-large" teams are chosen by an NCAA selection committee, then announced in a nationally televised event dubbed Selection Sunday. The 68 teams are divided into four regions and organized into a single-elimination "bracket", which pre-determines – when a team wins a game – which team it will face next. Each team is "seeded", or ranked, within its region from 1 to 16. After the First Four round, the remainder of the tournament begins the third Thursday of March, and is played over the course of three weekends, at pre-selected neutral sites across the United States. Teams, seeded by rank, proceed through a single-game elimination bracket beginning with the First Four round, a first round consisting of 64 teams playing in 32 games over the course of two days, the second round consisting of the 32 remaining teams playing in 16 games that weekend, the "Sweet Sixteen" and "Elite Eight" rounds the next week and weekend, respectively, and – for the last weekend of the tournament – the "Final Four" round. The two Final Four games are played the Saturday preceding the first Sunday in April, with the championship game on Monday. These four teams, one from each region (East, South, Midwest, and West), compete in a preselected location for the national championship.[[1]](https://en.wikipedia.org/wiki/NCAA_Division_I_men%27s_basketball_tournament) """)

st.write("""
### Machine Learning Prediction Algorithms ###
The term ‘machine learning’ is often, incorrectly, interchanged with Artificial Intelligence, but machine learning is actually a sub
field/type of AI. Machine learning is also often referred to as predictive analytics, or predictive modelling.
Coined by American computer scientist Arthur Samuel in 1959, the term ‘machine learning’ is defined as a “computer’s ability to learn without being explicitly programmed”.
At its most basic, machine learning uses programmed algorithms that receive and analyse input data to predict output values within an acceptable range. As new data is fed to these algorithms, they learn and optimise their operations to improve performance, developing ‘intelligence’ over time.
There are four types of machine learning algorithms: supervised, semi-supervised, unsupervised and reinforcement.  
n supervised learning, the machine is taught by example. The operator provides the machine learning algorithm with a known dataset that includes desired inputs and outputs, and the algorithm must find a method to determine how to arrive at those inputs and outputs. While the operator knows the correct answers to the problem, the algorithm identifies patterns in data, learns from observations and makes predictions. The algorithm makes predictions and is corrected by the operator – and this process continues until the algorithm achieves a high level of accuracy/performance.[[2]](https://www.sas.com/en_gb/insights/articles/analytics/machine-learning-algorithms.html#:~:text=At%20its%20most%20basic%2C%20machine,developing%20'intelligence'%20over%20time.  ) """)


st.write("""
## Methodology ##   
Even among non-sports fans, it has become quite prevalent in popular culture to predict the results of each game; it is estimated that tens of millions of Americans take part in a bracket pool contest each year. Have you ever wondered if it's possible to predict the outcome of NCAA basketball matches with the help of machine learning? Well, wonder no more! We tried to gather the immense amount of data on NCAA basketball games and trained machine learning algorithms to analyze team statistics, past offensive and defensive performance, and other factors that might affect the outcome of future matches. In this dashboard, After explaining the dataset gathering and cleansing procedure, we discuss the most effective teams' factors that could impact match results and explain them in detail, then we use sensitivity analysis of the model to determine which one is more effective than another. In the model section, we discuss the number of layers and nodes, different activation functions, and different optimal features of networks and how to avoid overfitting. then investigate any cinderella story possibility during March Madness 2023 by comparing model prediction with teams official rankings. At last, you can find a match prediction application that uses machine learning to predict the results of NCAA basketball matches, increasing your chances of making accurate predictions and enhancing your overall enjoyment of the sport.
""")


st.text(" \n")
st.write("""   
#### Sources ####  """)
st.write("""    1.https://www.ncaa.org/news/2022/3/10/media-center-from-authorized-sources.aspx     
                2.https://www.sas.com/en_gb/insights/articles/analytics/machine-learning-algorithms.html#:~:text=At%20its%20most%20basic%2C%20machine,developing%20'intelligence'%20over%20time.  
        3.https://www.bannersontheparkway.com/2023/2/13/23598002/rule-15-2-a-and-the-state-of-officials-in-college-basketball-big-east    
        4.https://kenpom.com/    
        5.https://barttorvik.com/trank.php#  
            """)


st.text(" \n")
c1, c2 = st.columns(2)
with c1:
    st.info(
        '**Twitter:  [Ludwig.1989](https://flipsidecrypto.xyz/)**', icon="🕊️")
    st.info(
        '**Data Set (1):  [Our own upploaded Data Set Match Results (Kaggle)](https://www.kaggle.com/datasets/kaizenstep/ncaa-2023-all-games-results)**', icon="🧠")

with c2:
    st.info(
        '**Project Github:  [NCAA Basketball](https://github.com/Kaizen-Step/NCAA_Basketball)**', icon="💻")
    st.info(
        '**Data Set (2):  [Barttorvik](https://barttorvik.com/trank.php#)**', icon="🧠")
