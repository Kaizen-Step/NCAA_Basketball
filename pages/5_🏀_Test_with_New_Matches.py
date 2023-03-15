# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

# Theme
theme_plotly = None  # None or streamlit

# Layout
st.set_page_config(page_title='Test with New Matches - NCAA_Basketball',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('🏀 Test with New Matches')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'Stuidis_Gross':
        return pd.read_csv('https://raw.githubusercontent.com/Kaizen-Step/Hollywood_Box_Office_Tragedy/main/Data/Studios/Studios.csv')
    elif query == 'Number_of_Release':
        return pd.read_csv('https://raw.githubusercontent.com/Kaizen-Step/Hollywood_Box_Office_Tragedy/main/Data/Studios/Studios2.csv')
    elif query == 'average_per_release':
        return pd.read_csv('https://raw.githubusercontent.com/Kaizen-Step/Hollywood_Box_Office_Tragedy/main/Data/Studios/Studios3.csv')
    return None


Stuidis_Gross = get_data('Stuidis_Gross')
Number_of_Release = get_data('Number_of_Release')
average_per_release = get_data('average_per_release')


df = Stuidis_Gross
df2 = Number_of_Release
df3 = average_per_release
#################################################################################################
st.write(""" ### Movie Production Companies (Studios) ##  """)

st.write("""
Major film studios are production and distribution companies that release a substantial number of films annually and consistently command a significant share of box office revenue in a given market. Since the dawn of filmmaking, the U.S. major film studios have dominated both American cinema and the global film industry U.S. studios have benefited from a strong first-mover advantage in that they were the first to industrialize filmmaking and master the art of mass-producing and distributing high-quality films with broad cross-cultural appeal.[[7]](https://en.wikipedia.org/wiki/Major_film_studios)       


   

  """)


st.info(""" ##### In This Studio Section you can find: ####

* Top 7 Studio Based on Total Gross
* Top 7 Studio Based on Number of Release
* Top 7 Studio Based on Average Gross per Release



""")


#################################################################################################
st.write(""" ## Top 7 Studio Based on Total Gross """)

st.write(""" The first-place studio in terms of overall gross revenue was "Marvel Comics," which beat the runner-up by a huge margin of \$10 billion. With a total revenue of \$7.02 billion, "Legendary Pictures," best known for its Jurassic Park franchise, came in second. It's good to know that since September 1, 2009, "Marvel Comics" has been a part of The Walt Disney Company. """)

c1, c2 = st.columns(2)

with c1:
    # Top new contracts based on weekly transactions
    fig = px.bar((df.head(7)), x="Brand", y="Total", color="Brand",
                 title='Top Studio Based on All time Total Gross ')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Total Gross [USD]')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

with c2:
    # Top new contracts based on weekly transactions
    fig = px.area(df.head(7), x="Brand", y="Releases",
                  title='Top Brand Number of Released Title')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Number of Title Released')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.table(df.head(7))

#####################################################
st.write(""" ## Top 7 Studio Based on Number of Release """)

st.write("""  "Marvel Comics" also led other studios in the number of films released, with 74 films grossing more than 17 billion dollars. "Stephen King," which is mostly known for horror movies, ranked 4th with 53 films. """)

c1, c2 = st.columns(2)

with c1:

    # Top new contracts based on weekly transactions
    fig = px.bar((df2.head(7)), x="Brand", y="Releases", color="Brand",
                 title='Top Studio Based on Total Gross ')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='All Time total Gross [USD]')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

with c2:
    # Top new contracts based on weekly transactions
    fig = px.area(df2.head(7), x="Brand", y="Total",
                  title='Top Studio Total Gross [USD]')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Total Gross [USD]')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.table(df2.head(7))


# ######################################################
st.write(""" ##  Top 7 Studio Based on Average Gross per Release """)

st.write(""" As expected, "Marvel Comics" took the top spot, followed by "Pixar" in second place with 28 films and an average gross of $217 million. With only 15 films, "Bad Robot" performed well, averaging 205 million dollar. """)

c1, c2 = st.columns(2)

with c1:
    # Top new contracts based on weekly transactions
    fig = px.bar((df3.head(7)), x="Brand", y="Average Gross Per Release", color="Brand",
                 title='Top Studio Based on Number of Movie Released ')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Average Gross per Release')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


with c2:
    # Top new contracts based on weekly transactions
    fig = px.area(df3.head(7), x="Brand", y="Releases",
                  title='Number of Released Top Genre Total Gross Revenue ')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Number of Release')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.table(df3.head(7))


##########################################################################

st.text(" \n")

st.info(""" #### Summary: ####


* In all three ranking lists, "Marvel Comics" came in first, well surpassing the runner-up
* With 53 films released, "Stephen King," which is best renowned for producing horror movies, came in fourth place among all studios in number of release
* With 28 films and an average revenue of $217 million, "Pixar" came in second on the list of highest average box office receipts per release
* "Bad Robot" did well, earning an average of 205 million dollars

""")
