# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

# Theme
theme_plotly = None  # None or streamlit

# Layout
st.set_page_config(page_title=' Most Effective Factors - NCAA_Basketball',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('🔥 Most Effective Factors')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache_data()
def get_data(query):
    if query == 'Barttorvik_Team':
        return pd.read_csv('Data/barttorvik_2023.csv')
    elif query == 'sensetive_analyse':
        return pd.read_csv('Data/weights_O.csv')
    return None


Barttorvik_Team = get_data('Barttorvik_Team')
sensetive_analyse = get_data('sensetive_analyse')


df = Barttorvik_Team
df2 = sensetive_analyse

#################################################################################################
st.write(""" ### Most Effective Factors ##  """)

st.write("""
  there are many factors that can influence the outcome of these games, some of the most important include a team's overall talent level, their ability to execute on both offense and defense, their experience playing in high-pressure situations, and even the luck of the draw in terms of their tournament bracket placement. With so many variables at play, the NCAA tournament is always full of surprises, making it one of the most exciting events in all of sports.  

  """)


st.info(""" ##### In This Most Effective Offensive Factors you can find: ####   

* Adjusted Offensive Efficiency  
* Effective Field Goal Percentage Shot    
* Turnover Percentage Committed (Steal Rate)
* Offensive Rebound Rate  
* Free Throw Rate (How often the given team shoots Free Throws)  
* Two-Point Shooting Percentage   
* Three-Point Shooting Percentage    
* Wins Above Bubble
        """)

###################################################################

st.warning(" The Detailed explanation and multitude number of graphs might be over whelming to general audiance , visit the summary section at the end for brief informations")

st.write(""" ##  Offensive Factors ##  """)

st.write(""" In this section, we explained all the features and statistics of teams, with the top 10 teams being the best at each feature. We then used model sensitivity analysis to define which factor is more important than another. This section might be overwhelming to those who do not have intention to see the details; they can visit the summary section at the end for general ideas and rankings.
""")
#####################################################


st.write(""" ### Adjusted Offensive Efficiency [ADJOE] ##  """)

st.write(""" Adjusted Offensive Efficiency (AOE) is a basketball statistic that measures how effectively a team scores points per possession, while accounting for the strength of the opposing team's defense. AOE is typically calculated by taking a team's points scored per 100 possessions and adjusting that number based on the strength of the opposing team's defense, as well as the pace of the game.
One commonly used method for calculating AOE is to use the formula:      

  AOE = (Points Scored / Possessions) * (League Average Efficiency / Opponent's Defensive Efficiency)     
  
By adjusting for the strength of the opposing team's defense and the pace of the game, AOE provides a more accurate measure of a team's offensive performance than simply looking at their raw points scored per game.
   

  """)

# NCCA Team with Adjusted Offensive Efficiency
fig = px.area(df.sort_values(by=['ADJOE'], ascending=False), x="TEAM", y="ADJOE",
              title='NCCA Team with Adjusted Offensive Efficiency')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='ADJOE')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


c1, c2 = st.columns(2)

with c1:
    # Top 10 Team with Adjusted Offensive Efficiency [Log Value]
    fig = px.bar(df.sort_values(by=['ADJOE'], ascending=False).head(10), x="TEAM", y="ADJOE", color="TEAM",
                 title='Top 10 Team with Adjusted Offensive Efficiency [Log Value]', log_y=True)
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='ADJOE')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

with c2:
    fig = px.bar(df2, x="parameters", y="sensitivity",
                 title='Parameters Sensivity analysis', log_y=False)
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Sensitivity')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


##############################################################
st.write(""" ### Effective Field Goal Percentage Shot [EFG_O] ##  """)

st.write(""" Effective Field Goal Percentage (eFG%) is a basketball statistic that measures a player's shooting efficiency. It is a modification of the traditional Field Goal Percentage (FG%), which only takes into account two-point field goals and three-point field goals.
In contrast, eFG% takes into account the fact that three-point field goals are worth more than two-point field goals. The formula for eFG% is:  

eFG% = (FGM + 0.5 * 3PM) / FGA  

where FGM is the number of field goals made, 3PM is the number of three-point field goals made, and FGA is the number of field goal attempts.  
By adding 0.5 times the number of three-pointers made to the number of two-pointers made in the numerator, eFG% effectively weights three-pointers as if they were 1.5 two-pointers. This provides a more accurate picture of a player's shooting efficiency and helps to compare players who shoot a different mix of two-pointers and three-pointers.  
eFG% is particularly useful for evaluating players who are efficient at shooting three-pointers. For example, a player who shoots 50% on two-point field goals and 33% on three-point field goals would have a FG% of 43.3%, which is below average. However, their eFG% would be 51.7%, which is above average because their three-pointers are weighted more heavily.   
   

  """)

# NCCA Team with Adjusted Offensive Efficiency
fig = px.area(df.sort_values(by=['EFG%'], ascending=False), x="TEAM", y="EFG%",
              title='NCCA Team with Adjusted Offensive Efficiency')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='EFG%')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


c1, c2 = st.columns(2)

with c1:
    # Top 10 Team with Adjusted Offensive Efficiency [Log Value]
    fig = px.bar(df.sort_values(by=['EFG%'], ascending=False).head(10), x="TEAM", y="EFG%", color="TEAM",
                 title='Top 10 Team with Most Effective Field Goal Percentage Shot [Log Value]', log_y=True)
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='EFG%')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

with c2:
    fig = px.bar(df2, x="parameters", y="sensitivity",
                 title='Parameters Sensivity analysis', log_y=False)
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Sensitivity')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

######################################################

st.write(""" ###  Turnover Percentage Committed (Steal Rate) [TORD] """)

st.write(""" Turnover Percentage Committed, also known as Steal Rate, is a basketball statistic that measures the percentage of possessions in which a player commits a steal. It is calculated as follows:

Steal Rate = (Steals x (Team Minutes / 5)) / Minutes Played

Where "Team Minutes" refers to the total number of minutes played by the player's team, and "Minutes Played" refers to the total number of minutes played by the player.
Steal Rate is used to evaluate a player's defensive ability and effectiveness in causing turnovers. A high Steal Rate indicates that a player is skilled at anticipating and disrupting passing lanes, and is successful at stealing the ball from opposing players.   
   
  """)

# NCCA Team with Adjusted Offensive Efficiency
fig = px.area(df.sort_values(by=['TOR'], ascending=False), x="TEAM", y="TOR",
              title='NCCA Team with Turnover Percentage Committed (Steal Rate)')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title=' Turnover Percentage')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


c1, c2 = st.columns(2)

with c1:
    # Top 10 Team with Most Turnover Percentage Committed (Steal Rate)
    fig = px.bar(df.sort_values(by=['TOR'], ascending=False).head(10), x="TEAM", y="TOR", color="TEAM",
                 title='Top 10 Team with Most Turnover Percentage Committed (Steal Rate) [Log Value]', log_y=True)
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title=' Turnover Percentage')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


with c2:
    fig = px.bar(df2, x="parameters", y="sensitivity",
                 title='Parameters Sensivity analysis', log_y=False)
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Sensitivity')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


############################################################
st.write(""" ### Effective Field Goal Percentage Shot [EFG_O] ##  """)

st.write(""" Effective Field Goal Percentage (eFG%) is a basketball statistic that measures a player's shooting efficiency. It is a modification of the traditional Field Goal Percentage (FG%), which only takes into account two-point field goals and three-point field goals.
In contrast, eFG% takes into account the fact that three-point field goals are worth more than two-point field goals. The formula for eFG% is:  

eFG% = (FGM + 0.5 * 3PM) / FGA  

where FGM is the number of field goals made, 3PM is the number of three-point field goals made, and FGA is the number of field goal attempts.  
By adding 0.5 times the number of three-pointers made to the number of two-pointers made in the numerator, eFG% effectively weights three-pointers as if they were 1.5 two-pointers. This provides a more accurate picture of a player's shooting efficiency and helps to compare players who shoot a different mix of two-pointers and three-pointers.  
eFG% is particularly useful for evaluating players who are efficient at shooting three-pointers. For example, a player who shoots 50% on two-point field goals and 33% on three-point field goals would have a FG% of 43.3%, which is below average. However, their eFG% would be 51.7%, which is above average because their three-pointers are weighted more heavily.   
   

  """)

# NCCA Team with Adjusted Offensive Efficiency
fig = px.area(df.sort_values(by=['EFG%'], ascending=False), x="TEAM", y="EFG%",
              title='NCCA Team with Adjusted Offensive Efficiency')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='EFG%')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


c1, c2 = st.columns(2)

with c1:
    # Top 10 Team with Adjusted Offensive Efficiency [Log Value]
    fig = px.bar(df.sort_values(by=['EFG%'], ascending=False).head(10), x="TEAM", y="EFG%", color="TEAM",
                 title='Top 10 Team with Most Effective Field Goal Percentage Shot [Log Value]', log_y=True)
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='EFG%')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

with c2:
    fig = px.bar(df2, x="parameters", y="sensitivity",
                 title='Parameters Sensivity analysis', log_y=False)
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Sensitivity')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

######################################################

st.write(""" ### Offensive Rebound Rate [ORB] """)

st.write(""" Offensive Rebound Rate (ORR) is a statistic used in basketball to measure the percentage of missed shots by a team that are rebounded by that same team. Specifically, it is the number of offensive rebounds divided by the total number of missed field goals and missed free throws by that team.

ORR is a useful statistic because offensive rebounds can lead to second-chance scoring opportunities, which can be critical in close games. A team with a high ORR is generally considered to be more effective at controlling the boards and generating additional scoring opportunities.

ORR can be calculated for individual players as well as for teams. The formula for ORR is:

ORR = Offensive rebounds / (Offensive rebounds + Opponents' defensive rebounds)
   
  """)

# NCCA Team with Adjusted Offensive Efficiency
fig = px.area(df.sort_values(by=['ORB'], ascending=False), x="TEAM", y="ORB",
              title='NCCA Team with Offensive Rebound Rate (Steal Rate)')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title=' Offensive Rebound Rate')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


c1, c2 = st.columns(2)

with c1:
    # Top 10 Team with Most Turnover Percentage Committed (Steal Rate)
    fig = px.bar(df.sort_values(by=['ORB'], ascending=False).head(10), x="TEAM", y="ORB", color="TEAM",
                 title='Top 10 Team with Most Offensive Rebound Rate [Log Value]', log_y=True)
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title=' Offensive Rebound Rate')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

with c2:
    fig = px.bar(df2, x="parameters", y="sensitivity",
                 title='Parameters Sensivity analysis', log_y=False)
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Sensitivity')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
####################################################################################################
st.write(
    """ ### Free Throw Rate (How often the given team shoots Free Throws)  [FTR] """)

st.write(""" Free Throw Rate (FTR) is a basketball statistic that measures how often a team attempts free throws in relation to their field goal attempts. It is calculated by dividing the number of free throw attempts by the number of field goal attempts.

The formula for Free Throw Rate is:

FTR = Free Throw Attempts / Field Goal Attempts

The resulting FTR value is a ratio, expressed as a decimal or a percentage. A higher FTR indicates that a team is more aggressive in attacking the basket and drawing fouls, which can be advantageous since free throws are uncontested shots that can lead to points without using the clock.
Free throw rate can be used to analyze a team's offensive strategy and the effectiveness of individual players in drawing fouls and getting to the free-throw line.
   
  """)

# NCCA Team with Adjusted Offensive Efficiency
fig = px.area(df.sort_values(by=['FTR'], ascending=False), x="TEAM", y="FTR",
              title='NCCA Team with Free Throw Rate')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title=' Free Throw Rate ')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


c1, c2 = st.columns(2)

with c1:
    # Top 10 Team with Most Turnover Percentage Committed (Steal Rate)
    fig = px.bar(df.sort_values(by=['FTR'], ascending=False).head(10), x="TEAM", y="FTR", color="TEAM",
                 title='Top 10 Team with Most Free Throw Rate [Log Value]', log_y=True)
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title=' Free Throw Rate ')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


with c2:
    fig = px.bar(df2, x="parameters", y="sensitivity",
                 title='Parameters Sensivity analysis', log_y=False)
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Sensitivity')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
############################################################################################################
st.write(
    """ ### Two-Point Shooting Percentage """)

st.write(""" Free Throw Rate (FTR) is a basketball statistic that measures how often a team attempts free throws in relation to their field goal attempts. It is calculated by dividing the number of free throw attempts by the number of field goal attempts.

The formula for Free Throw Rate is:

FTR = Free Throw Attempts / Field Goal Attempts

The resulting FTR value is a ratio, expressed as a decimal or a percentage. A higher FTR indicates that a team is more aggressive in attacking the basket and drawing fouls, which can be advantageous since free throws are uncontested shots that can lead to points without using the clock.
Free throw rate can be used to analyze a team's offensive strategy and the effectiveness of individual players in drawing fouls and getting to the free-throw line.
   
  """)

# NCCA Team with Adjusted Offensive Efficiency
fig = px.area(df.sort_values(by=['2P%'], ascending=False), x="TEAM", y="2P%",
              title='NCCA Team with Free Throw Rate')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title=' Free Throw Rate ')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


c1, c2 = st.columns(2)

with c1:
    # Top 10 Team with Most Turnover Percentage Committed (Steal Rate)
    fig = px.bar(df.sort_values(by=['2P%'], ascending=False).head(10), x="TEAM", y="2P%", color="TEAM",
                 title='Top 10 Team with Most Two-Point Shooting Percentage [Log Value]', log_y=True)
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title=' Two-Point Shooting Percentage ')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


with c2:
    fig = px.bar(df2, x="parameters", y="sensitivity",
                 title='Parameters Sensivity analysis', log_y=False)
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Sensitivity')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

######################################################################################################
st.write(
    """ ### Three-Point Shooting Percentage  """)

st.write(""" Free Throw Rate (FTR) is a basketball statistic that measures how often a team attempts free throws in relation to their field goal attempts. It is calculated by dividing the number of free throw attempts by the number of field goal attempts.

The formula for Free Throw Rate is:

FTR = Free Throw Attempts / Field Goal Attempts

The resulting FTR value is a ratio, expressed as a decimal or a percentage. A higher FTR indicates that a team is more aggressive in attacking the basket and drawing fouls, which can be advantageous since free throws are uncontested shots that can lead to points without using the clock.
Free throw rate can be used to analyze a team's offensive strategy and the effectiveness of individual players in drawing fouls and getting to the free-throw line.
   
  """)

# NCCA Team with Adjusted Offensive Efficiency
fig = px.area(df.sort_values(by=['3P%'], ascending=False), x="TEAM", y="3P%",
              title='NCCA Team with Three-Point Shooting Percentage')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title=' Three-Point Shooting Percentage')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


c1, c2 = st.columns(2)

with c1:
    # Top 10 Team with Most Turnover Percentage Committed (Steal Rate)
    fig = px.bar(df.sort_values(by=['3P%'], ascending=False).head(10), x="TEAM", y="3P%", color="TEAM",
                 title='Top 10 Team with Most Three-Point Shooting Percentage [Log Value]', log_y=True)
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title=' Three-Point Shooting Percentage ')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


with c2:
    fig = px.bar(df2, x="parameters", y="sensitivity",
                 title='Parameters Sensivity analysis', log_y=False)
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Sensitivity')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
###########################################################################################
st.write(
    """ ### Wins Above Bubble  """)

st.write(""" Free Throw Rate (FTR) is a basketball statistic that measures how often a team attempts free throws in relation to their field goal attempts. It is calculated by dividing the number of free throw attempts by the number of field goal attempts.

The formula for Free Throw Rate is:

FTR = Free Throw Attempts / Field Goal Attempts

The resulting FTR value is a ratio, expressed as a decimal or a percentage. A higher FTR indicates that a team is more aggressive in attacking the basket and drawing fouls, which can be advantageous since free throws are uncontested shots that can lead to points without using the clock.
Free throw rate can be used to analyze a team's offensive strategy and the effectiveness of individual players in drawing fouls and getting to the free-throw line.
   
  """)

# NCCA Team with Adjusted Offensive Efficiency
fig = px.area(df.sort_values(by=['WAB'], ascending=False), x="TEAM", y="WAB",
              title='NCCA Team with Wins Above Bubble')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title=' Wins Above Bubble ')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


c1, c2 = st.columns(2)

with c1:
    # Top 10 Team with Most Turnover Percentage Committed (Steal Rate)
    fig = px.bar(df.sort_values(by=['WAB'], ascending=False).head(10), x="TEAM", y="WAB", color="TEAM",
                 title='Top 10 Team with Most Wins Above Bubble [Log Value]', log_y=True)
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title=' Wins Above Bubble ')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


with c2:
    fig = px.bar(df2, x="parameters", y="sensitivity",
                 title='Parameters Sensivity analysis', log_y=False)
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Sensitivity')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
#############################################################################################################

st.text(" \n")

st.info(""" #### Summary: ####


* Collgate was the team with best offensive record wich ranked first in 3 category
* Gongoza also showed aggresive performance and ranked first in 2 factors
* Huston and Alabama which ranked first in battrovick ranking were not in single top five in different factores
* UCLA showed good statistics in offensive features among top ranking teams

""")
