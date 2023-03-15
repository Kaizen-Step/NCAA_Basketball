# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

# Theme
theme_plotly = None  # None or streamlit


# Layout
st.set_page_config(page_title=' Cinderella stories - NCAA_Basketball',
                   page_icon=':bar_chart:📈', layout='wide')
st.title(' 🏆 Cinderella stories')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'Daily_2022':
        return pd.read_csv('https://raw.githubusercontent.com/Kaizen-Step/Hollywood_Box_Office_Tragedy/main/Data/Domestic/Y22/Y22-Daily.csv')
    elif query == 'Weekly_2022':
        return pd.read_csv('https://raw.githubusercontent.com/Kaizen-Step/Hollywood_Box_Office_Tragedy/main/Data/Domestic/Y22/Y22-Weekly.csv')
    elif query == 'table':
        return pd.read_csv('https://raw.githubusercontent.com/Kaizen-Step/Hollywood_Box_Office_Tragedy/main/Data/Domestic/Y22/Y22-Weekly2.csv')
    return None


Daily_2022 = get_data('Daily_2022')
Weekly_2022 = get_data('Weekly_2022')
table = get_data('table')

df = Daily_2022
df2 = Weekly_2022
df3 = table


#################################################################################################
st.write(""" ### Hollywood Box Office in 2022 ##  """)

st.write(""" Hollywood movie theater box office revenue reached in at $7.36 billion in 2022, a respectable 64% increase from 2021 but still far below pre-pandemic levels. The 2022 figure is 35% lower than the average for 2017–19, the three years prior to COVID–19, which completely changed the worldwide film industry.
    

   

  """)


st.info(""" ##### In This Review 2022 Section you can find: ####

* Daily Top 10 Movie Grosss in 2022 [USD]     
* Daily Number of Movie Released    
* 2022 Weekly Figures
* Top First Sold Movie each Week [Detailed Table]



""")


#################################################################################################


#####################################################

st.write(""" ## Hollywood Box Office 2022 Daily Figures""")

st.write(""" The highest top-10 grossing day in 2019 was 169 million, which fell to 57 million in 2020 and then rose to 128 million in 2021. This trend was expected to continue, and the record should have been broken in 2022. However, as you can see, there were days with a maximum of 99 million top ten grossings, and none of them were able to break "Spider-Man: No Way Home's" record in 2021. In 2022, there were seven days with more than 50 million top ten grossings, with other days tolerated between 20m and 45m on weekends and 2m to 14m on weekdays.
""")
# Hollywood Industry total gross over course of years [USD]
fig = px.area(df, x="Date", y="Top 10 Gross",
              title='Daily Top 10 Grosss in 2022 [USD]')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Daily top 10 Gross [USD]')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Daily Number of Release in 2022
fig = px.line(df, x="Date", y="%± YD",
              title='Daily Top 10 Grosss Change Rate [Yesterday]', log_y=False)
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Daily Change Rate')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.write(""" ### Daily Number of Movie Released   """)

st.write(""" The daily number of movies released increased steadily from 23 in the first week of January to 52 on September 17, before dropping to 24 on November 30. The Qatar 2022 World Cup might be a reason for this fall. Even though the number of movies that came out during this time period went down, the total gross didn't change much. Maybe theaters showing soccer matches were the reason for this.
""")

# Hollywood Industry total gross over course of years [USD]
fig = px.area(df, x="Date", y="Releases",
              title=' Daily Number of Release in 2022')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title=' Daily Release')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


##############################################################

st.write(""" ## Weekly Figures """)
st.write("""  The weekly figure, which shows a high of 334 million on July 8–14 and a low of 58.7 million on September 9–15, makes it more obvious that overall gross decreased dramatically after the summer. This number increased considerably once again in the winter, and there were weeks with a gross of 200 million.
""")
# Hollywood Industry total gross over course of years [USD]
fig = px.area(df2, x="Dates", y="Overall Gross",
              title='Weekly Overall Gross in 2022 [USD]')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Overall Gross [USD]')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

c1, c2 = st.columns(2)
with c1:
    # Hollywood Industry total gross over course of years [USD]
    fig = px.bar(df2, x="Dates", y="Top 10 Gross",  color="Dates",
                 title='Weekly Top 10 Grosss in 2022 [USD]')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Weekly top 10 Gross [USD]')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

with c2:
    # Daily Number of Release in 2022
    fig = px.line(df2, x="Dates", y="%± LW",
                  title='Weekly Overall Gross Change Rate', log_y=False)
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Weekly Overall Gross Change Rate')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


######################################################

st.write(""" ### Number of Relaese """)
st.write(""" In the fall, there was a conflict between the number of films released and the overall box office; as we saw in the previous graph, the total box office fell precipitously after the summer, but the number of films released rose by 40%. This comparison demonstrates that more movies, regardless of their quality, do not increase market revenue.
""")
# Hollywood Industry total gross over course of years [USD]
fig = px.area(df2, x="Dates", y="Releases",
              title=' Weekly Number of Release in 2022')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title=' Weekly Release')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

#########################################################


############################################################
st.write(""" ### Top First Sold Movie each Week with Detalis Table """)

st.table(df3.head(20))
##########################################################################

st.text(" \n")

st.info(""" #### Summary: ####


* The highest top-10 grossing day in 2022 was only 99 million, falling short of 2021's record of 128 million
* In 2022, there were seven days with top 10 grossings of more than 50 million
* The amount of films released during the World Cup in Qatar decreased, but the overall box office didn't alter significantly 
* After the summer, overall gross fell sharply, from a peak of 334 million on July 8–14 to a low of 58.7 million on September 9–15
* The quantity of movies released and the overall box office conflicted in the fall

""")
