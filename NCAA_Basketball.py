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
    st.image(Image.open('Images/march2.jpg'))


st.write("""
### NCAA March Madness tournament ###
The NCAA Division I men's basketball tournament, branded as NCAA March Madness and commonly called March Madness, is a single-elimination tournament played each spring in the United States, currently featuring 68 college basketball teams from the Division I level of the National Collegiate Athletic Association (NCAA), to determine the national champion. The tournament was created in 1939 by the National Association of Basketball Coaches, and was the idea of Ohio State coach Harold Olsen. Played mostly during March, it has become one of the most popular annual sporting events in the United States.   
The tournament teams include champions from 32 Division I conferences (which receive automatic bids), and 36 teams which are awarded at-large berths. These "at-large" teams are chosen by an NCAA selection committee, then announced in a nationally televised event dubbed Selection Sunday. The 68 teams are divided into four regions and organized into a single-elimination "bracket", which pre-determines – when a team wins a game – which team it will face next. Each team is "seeded", or ranked, within its region from 1 to 16. After the First Four round, the remainder of the tournament begins the third Thursday of March, and is played over the course of three weekends, at pre-selected neutral sites across the United States. Teams, seeded by rank, proceed through a single-game elimination bracket beginning with the First Four round, a first round consisting of 64 teams playing in 32 games over the course of two days, the second round consisting of the 32 remaining teams playing in 16 games that weekend, the "Sweet Sixteen" and "Elite Eight" rounds the next week and weekend, respectively, and – for the last weekend of the tournament – the "Final Four" round. The two Final Four games are played the Saturday preceding the first Sunday in April, with the championship game on Monday. These four teams, one from each region (East, South, Midwest, and West), compete in a preselected location for the national championship.[[1]](https://en.wikipedia.org/wiki/NCAA_Division_I_men%27s_basketball_tournament) """)


st.write("""
## Methodology ##   
Even among non-sports fans, it has become quite prevalent in popular culture to predict the results of each game; it is estimated that tens of millions of Americans take part in a bracket pool contest each year. Have you ever wondered if it's possible to predict the outcome of NCAA basketball matches with the help of machine learning? Well, wonder no more!  We tried to gather the immense amount of data on NCAA basketball games, and trained machine learning algorithms to analyze team statistics, past Offenisve and Defensive performance and other factors  the outcome of future matches. In this dashboard after explainig dataset gathering and cleansing procedure we discuss about most effective teams factors that could impact on match result and explained them in details and by usinig sensivity anlaysis of model define which one is more effective than another. in model section we discuss about number of layers and nerouns different activation functions and different optimal features of network.then investigate any cinderal stories possibility during 34 march madness 2023 comparing model prediction with teams official ranking. By using machine learning to predict the results of NCAA basketball matches, you can increase your chances of making accurate predictions and enhance your overall enjoyment of the sport.
""")


st.text(" \n")
st.write("""   
#### Sources ####  """)
st.write("""    1.https://www.ncaa.org/news/2022/3/10/media-center-from-authorized-sources.aspx   
        2.https://www.bannersontheparkway.com/2023/2/13/23598002/rule-15-2-a-and-the-state-of-officials-in-college-basketball-big-east  
        3.https://www.boxofficemojo.com/
            """)


st.text(" \n")
c1, c2 = st.columns(2)
with c1:
    st.info(
        '**Twitter:  [Ludwig.1989](https://flipsidecrypto.xyz/)**', icon="🕊️")
    st.info(
        '**Data Set (1):  [IMDB Box office Mojo (Kaggle)](https://www.kaggle.com/code/jonbown/box-office-mojo-web-scraping-with-python)**', icon="🧠")

with c2:
    st.info(
        '**Project Github:  [Hollywood Box Office](https://github.com/Kaizen-Step/Hollywood_Box_Office_Tragedy)**', icon="💻")
    st.info(
        '**Data Set (2):  [IMDB Box office Mojo (Kaggle)](https://www.kaggle.com/datasets/thedevastator/hollywood-movies-domestic-lifetime-gross-and-ran?resource=download)**', icon="🧠")
