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
st.title('🛡️ Most Effective Factors')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'Barttorvik_Team':
        return pd.read_csv('Data/barttorvik_2023.csv')
    elif query == 'table':
        return pd.read_csv('https://raw.githubusercontent.com/Kaizen-Step/Hollywood_Box_Office_Tragedy/main/Data/Domestic/Domestic-Yearly2.csv')
    return None


Barttorvik_Team = get_data('Barttorvik_Team')
table = get_data('table')


df = Barttorvik_Team
df2 = table

#################################################################################################
st.write(""" ### Most Effective Defensive Factors ##  """)

st.write("""
  In NCAA basketball, there are several factors that can contribute to a team's defensive effectiveness. Some of the most effective defensive factors include:
Field Goal Percentage Defense: The ability to limit the opposing team's shooting percentage is a key factor in a team's defensive success.
Turnovers Forced: Teams that can force turnovers and convert them into points can have a significant impact on the outcome of a game.
Rebounding: Teams that can control the boards and limit second-chance opportunities for their opponents can be very effective on defense and so on.

In this sectin we name the most effective Defensive Factores that we used in our data sets and tried to evaluate each one of them with sensitivity analysis of model we created to show which one of the is more important and has bigger influenced on match result.

  """)


st.info(""" ##### In This Most Effective Deffensive Factors you can find: ####    

    * ADJ_T: Adjusted Tempo  
    * ADJDE: Adjusted Defensive Efficiency      
    * EFG_D: Effective Field Goal Percentage Allowed  
    * TOR: Turnover Percentage Allowed (Turnover Rate)  
    * DRB: Offensive Rebound Rate Allowed   
    * FTRD: Free Throw Rate Allowed   
    * 2P_D: Two-Point Shooting Percentage Allowed      
    * 3P_D: Three-Point Shooting Percentage Allowed  
    
    """)

###################################################################
st.write(""" ##  Defensive Factors ##  """)

#####################################################

st.write(""" ### Adjusted Tempo [ADJ_T]        """)

st.write(""" Offensive Rebound Rate (ORR) is a statistic used in basketball to measure the percentage of missed shots by a team that are rebounded by that same team. Specifically, it is the number of offensive rebounds divided by the total number of missed field goals and missed free throws by that team.

ORR is a useful statistic because offensive rebounds can lead to second-chance scoring opportunities, which can be critical in close games. A team with a high ORR is generally considered to be more effective at controlling the boards and generating additional scoring opportunities.

ORR can be calculated for individual players as well as for teams. The formula for ORR is:

ORR = Offensive rebounds / (Offensive rebounds + Opponents' defensive rebounds)
   
  """)
# Top 10 Team with Most Turnover Percentage Committed (Steal Rate)
fig = px.bar(df.sort_values(by=['ORB'], ascending=False).head(10), x="TEAM", y="ORB", color="TEAM",
             title='Top 10 Team with Most Offensive Rebound Rate [Log Value]', log_y=True)
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title=' Offensive Rebound Rate')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


c1, c2 = st.columns(2)

with c1:
    # NCCA Team with Adjusted Offensive Efficiency
    fig = px.area(df.sort_values(by=['ORB'], ascending=False), x="TEAM", y="ORB",
                  title='NCCA Team with Offensive Rebound Rate (Steal Rate)')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title=' Offensive Rebound Rate')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:
    # Hollywood Industry Gross Yearly change Rate[USD]
    fig = px.line(df2.tail(24), x="Year", y="%± LY",
                  title='Hollywood Industry Yearly Gross change Rate', log_y=False)
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Change Rate')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


#########################################################
st.write(""" ### Adjusted Defensive Efficiency     ##  """)

st.write(""" Adjusted Offensive Efficiency (AOE) is a basketball statistic that measures how effectively a team scores points per possession, while accounting for the strength of the opposing team's defense. AOE is typically calculated by taking a team's points scored per 100 possessions and adjusting that number based on the strength of the opposing team's defense, as well as the pace of the game.
One commonly used method for calculating AOE is to use the formula:      

  AOE = (Points Scored / Possessions) * (League Average Efficiency / Opponent's Defensive Efficiency)     
  
By adjusting for the strength of the opposing team's defense and the pace of the game, AOE provides a more accurate measure of a team's offensive performance than simply looking at their raw points scored per game.
   

  """)
# Top 10 Team with Adjusted Offensive Efficiency [Log Value]
fig = px.bar(df.sort_values(by=['ADJOE'], ascending=False).head(10), x="TEAM", y="ADJOE", color="TEAM",
             title='Top 10 Team with Adjusted Offensive Efficiency [Log Value]', log_y=True)
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='ADJOE')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


c1, c2 = st.columns(2)

with c1:
    # NCCA Team with Adjusted Offensive Efficiency
    fig = px.area(df.sort_values(by=['ADJOE'], ascending=False), x="TEAM", y="ADJOE",
                  title='NCCA Team with Adjusted Offensive Efficiency')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='ADJOE')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:
    # Hollywood Industry Gross Yearly change Rate[USD]
    fig = px.line(df2.tail(24), x="Year", y="%± LY",
                  title='Hollywood Industry Yearly Gross change Rate', log_y=False)
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Change Rate')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


##############################################################
st.write(""" ### Effective Field Goal Percentage Allowed  ##  """)

st.write(""" Effective Field Goal Percentage (eFG%) is a basketball statistic that measures a player's shooting efficiency. It is a modification of the traditional Field Goal Percentage (FG%), which only takes into account two-point field goals and three-point field goals.
In contrast, eFG% takes into account the fact that three-point field goals are worth more than two-point field goals. The formula for eFG% is:  

eFG% = (FGM + 0.5 * 3PM) / FGA  

where FGM is the number of field goals made, 3PM is the number of three-point field goals made, and FGA is the number of field goal attempts.  
By adding 0.5 times the number of three-pointers made to the number of two-pointers made in the numerator, eFG% effectively weights three-pointers as if they were 1.5 two-pointers. This provides a more accurate picture of a player's shooting efficiency and helps to compare players who shoot a different mix of two-pointers and three-pointers.  
eFG% is particularly useful for evaluating players who are efficient at shooting three-pointers. For example, a player who shoots 50% on two-point field goals and 33% on three-point field goals would have a FG% of 43.3%, which is below average. However, their eFG% would be 51.7%, which is above average because their three-pointers are weighted more heavily.   
   

  """)
# Top 10 Team with Adjusted Offensive Efficiency [Log Value]
fig = px.bar(df.sort_values(by=['EFG%'], ascending=False).head(10), x="TEAM", y="EFG%", color="TEAM",
             title='Top 10 Team with Most Effective Field Goal Percentage Shot [Log Value]', log_y=True)
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='EFG%')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


c1, c2 = st.columns(2)

with c1:
    # NCCA Team with Adjusted Offensive Efficiency
    fig = px.area(df.sort_values(by=['EFG%'], ascending=False), x="TEAM", y="EFG%",
                  title='NCCA Team with Adjusted Offensive Efficiency')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='EFG%')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:
    # Hollywood Industry Gross Yearly change Rate[USD]
    fig = px.line(df2.tail(24), x="Year", y="%± LY",
                  title='Hollywood Industry Yearly Gross change Rate', log_y=False)
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Change Rate')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

######################################################

st.write(""" ###  Turnover Percentage Allowed (Turnover Rate)  """)

st.write(""" Turnover Percentage Committed, also known as Steal Rate, is a basketball statistic that measures the percentage of possessions in which a player commits a steal. It is calculated as follows:

Steal Rate = (Steals x (Team Minutes / 5)) / Minutes Played

Where "Team Minutes" refers to the total number of minutes played by the player's team, and "Minutes Played" refers to the total number of minutes played by the player.
Steal Rate is used to evaluate a player's defensive ability and effectiveness in causing turnovers. A high Steal Rate indicates that a player is skilled at anticipating and disrupting passing lanes, and is successful at stealing the ball from opposing players.   
   
  """)
# Top 10 Team with Most Turnover Percentage Committed (Steal Rate)
fig = px.bar(df.sort_values(by=['TOR'], ascending=False).head(10), x="TEAM", y="TOR", color="TEAM",
             title='Top 10 Team with Most Turnover Percentage Committed (Steal Rate) [Log Value]', log_y=True)
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title=' Turnover Percentage')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


c1, c2 = st.columns(2)

with c1:
    # NCCA Team with Adjusted Offensive Efficiency
    fig = px.area(df.sort_values(by=['TOR'], ascending=False), x="TEAM", y="TOR",
                  title='NCCA Team with Turnover Percentage Committed (Steal Rate)')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title=' Turnover Percentage')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:
    # Hollywood Industry Gross Yearly change Rate[USD]
    fig = px.line(df2.tail(24), x="Year", y="%± LY",
                  title='Hollywood Industry Yearly Gross change Rate', log_y=False)
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Change Rate')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


############################################################
st.write(""" ### Free Throw Rate Allowed     ##  """)

st.write(""" Effective Field Goal Percentage (eFG%) is a basketball statistic that measures a player's shooting efficiency. It is a modification of the traditional Field Goal Percentage (FG%), which only takes into account two-point field goals and three-point field goals.
In contrast, eFG% takes into account the fact that three-point field goals are worth more than two-point field goals. The formula for eFG% is:  

eFG% = (FGM + 0.5 * 3PM) / FGA  

where FGM is the number of field goals made, 3PM is the number of three-point field goals made, and FGA is the number of field goal attempts.  
By adding 0.5 times the number of three-pointers made to the number of two-pointers made in the numerator, eFG% effectively weights three-pointers as if they were 1.5 two-pointers. This provides a more accurate picture of a player's shooting efficiency and helps to compare players who shoot a different mix of two-pointers and three-pointers.  
eFG% is particularly useful for evaluating players who are efficient at shooting three-pointers. For example, a player who shoots 50% on two-point field goals and 33% on three-point field goals would have a FG% of 43.3%, which is below average. However, their eFG% would be 51.7%, which is above average because their three-pointers are weighted more heavily.   
   

  """)
# Top 10 Team with Adjusted Offensive Efficiency [Log Value]
fig = px.bar(df.sort_values(by=['EFG%'], ascending=False).head(10), x="TEAM", y="EFG%", color="TEAM",
             title='Top 10 Team with Most Effective Field Goal Percentage Shot [Log Value]', log_y=True)
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='EFG%')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


c1, c2 = st.columns(2)

with c1:
    # NCCA Team with Adjusted Offensive Efficiency
    fig = px.area(df.sort_values(by=['EFG%'], ascending=False), x="TEAM", y="EFG%",
                  title='NCCA Team with Adjusted Offensive Efficiency')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='EFG%')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:
    # Hollywood Industry Gross Yearly change Rate[USD]
    fig = px.line(df2.tail(24), x="Year", y="%± LY",
                  title='Hollywood Industry Yearly Gross change Rate', log_y=False)
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Change Rate')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

######################################################

st.write(""" ###  Two-Point Shooting Percentage Allowed       """)

st.write(""" Offensive Rebound Rate (ORR) is a statistic used in basketball to measure the percentage of missed shots by a team that are rebounded by that same team. Specifically, it is the number of offensive rebounds divided by the total number of missed field goals and missed free throws by that team.

ORR is a useful statistic because offensive rebounds can lead to second-chance scoring opportunities, which can be critical in close games. A team with a high ORR is generally considered to be more effective at controlling the boards and generating additional scoring opportunities.

ORR can be calculated for individual players as well as for teams. The formula for ORR is:

ORR = Offensive rebounds / (Offensive rebounds + Opponents' defensive rebounds)
   
  """)
# Top 10 Team with Most Turnover Percentage Committed (Steal Rate)
fig = px.bar(df.sort_values(by=['ORB'], ascending=False).head(10), x="TEAM", y="ORB", color="TEAM",
             title='Top 10 Team with Most Offensive Rebound Rate [Log Value]', log_y=True)
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title=' Offensive Rebound Rate')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


c1, c2 = st.columns(2)

with c1:
    # NCCA Team with Adjusted Offensive Efficiency
    fig = px.area(df.sort_values(by=['ORB'], ascending=False), x="TEAM", y="ORB",
                  title='NCCA Team with Offensive Rebound Rate (Steal Rate)')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title=' Offensive Rebound Rate')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:
    # Hollywood Industry Gross Yearly change Rate[USD]
    fig = px.line(df2.tail(24), x="Year", y="%± LY",
                  title='Hollywood Industry Yearly Gross change Rate', log_y=False)
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Change Rate')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
##########################################################################

st.text(" \n")

st.info(""" #### Summary: ####


* As a result of the COVID-19 pandemic, the Hollywood annual gross dropped from \$11.36 billion in 2019 to \$2.11 billion in 2020
* Annual gross has steadily increased, reaching nearly \$7.36 billion in 2022—a more than 112% increase in a single year.
* Since 2000, the number of movies released has continuously risen, with 2018 seeing a record-breaking 993 movies released in a single year
* The total gross fell by 82% in 2020 while the number of movies released fell by 44%.
* Each movie's average gross revenue rose from \$12 million in 2019 to \$14.84 million in 2022.

""")
