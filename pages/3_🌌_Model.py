# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

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
#################################################################################################
st.write(""" ### Genre Concept ##  """)

st.write("""
A film genre is a stylistic or thematic category for motion pictures based on similarities either in the narrative elements, aesthetic approach, or the emotional response to the film. Drawing heavily from the theories of literary-genre criticism, film genres are usually delineated by "conventions, iconography, settings, narratives, characters and actors.With the proliferation of particular genres, film subgenres can also emerge: the legal drama, for example, is a sub-genre of drama that includes courtroom- and trial-focused movies.   [[6]](https://en.wikipedia.org/wiki/Film_genre)       

The genres used in this dashboard are mostly detailed sub-genres that have recently been used in the film industry, different from the seven common genres that were used in art.

   

  """)


st.info(""" ##### In This Genre Section you can find: ####

* Top 7 Genre Based on All time Total Gross
* Top 7 Genre Based on Number of Release
* Top 7 Genre Based on Average Gross per Release



""")


#################################################################################################
st.write(""" ## Top 7 Genre Based on All time Total Gross """)

st.write("""With 74 billion dollars in gross sales, the Adoption genre (a pre-existing work that has been transformed into a movie) is the most profitable of all time. The recent Marvel franchises had a big role in this outstanding results. The movie in this category with the biggest box office takings is "Avengers: Endgame." IMAX and 3D, with respective release numbers of 374 and 396, are honourable mentions in this ranking. """)

c1, c2 = st.columns(2)
with c1:

    # Top new contracts based on weekly transactions
    fig = px.bar((df.head(7)), x="Genre", y="Total", color="Genre",
                 title='Top Genre Based on All time Total Gross ')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Total Gross [USD]')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:
    # Top new contracts based on weekly transactions
    fig = px.area(df.head(7), x="Genre", y="Titles",
                  title='Top Genre Number of Released Title')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Number of Title Released')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.table(df.head(7))

#####################################################
st.write(""" ## Top 7 Genre Based on Number of Release """)

st.write("""  The genres with the most releases were foreign language and documentary, although their overall revenue at the box office were so much lower than Adoption, which came in third.	 """)


c1, c2 = st.columns(2)
with c1:
    # Top new contracts based on weekly transactions
    fig = px.bar((df2.head(7)), x="Genre", y="Titles", color="Genre",
                 title='Top Genre Based on Number of Release ')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Number of Release')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

with c2:
    # Top new contracts based on weekly transactions
    fig = px.area(df2.head(7), x="Genre", y="Total",
                  title='Top Genre Total Gross')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Total Gross [USD]')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.table(df2.head(7))


# ######################################################
st.write(""" ##  Top 7 Genre Based on Average Gross per Release """)

st.write(""" Due to the small number of releases in some genres, the average gross per release was not useful enough. but, with a total of 374 movies released and 57 billion dollars in gross sales, IMAX (a proprietary system of very large screens with a tall aspect ratio, high-resolution cameras, film formats, film projectors, and theatres) deserves an honourable mention here. """)

c1, c2 = st.columns(2)
with c1:
    # Top new contracts based on weekly transactions
    fig = px.bar((df3.head(7)), x="Genre", y="Average Per Release", color="Genre",
                 title='Top Genre Based on Number of Movie Released ')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Average Gross per Release')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

with c2:
    # Top new contracts based on weekly transactions
    fig = px.area(df3.head(7), x="Genre", y="Titles",
                  title='Number of Released Top Genre Total Gross Revenue ')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Number of Release')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.table(df3.head(7))


##########################################################################

st.text(" \n")

st.info(""" #### Summary: ####


* The adoption genre is currently the most profitable of all time, with gross sales of 74 billion dollars
* Foreign language and documentaries were the categories with the most number of releases
* The category deserving of attention is IMAX, with 153 million in average box office receipts per movie
* The average gross per release was insufficient because there weren't many releases in some genres
  

""")
