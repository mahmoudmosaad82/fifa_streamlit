import streamlit as st 
import pandas as pd 
import numpy as np
import plotly.express as px
st.title("Fifa EDA")
st.image("s.jpeg")
st.write("lorem ipsum dolor sit amet consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem.") 
fifa = pd.read_csv("fifa_eda.csv")

# #showing the top 5 valued players 
# st.markdown("## Top 5 Valued Players")
# st.write(fifa.nlargest(5, 'Value')[['Name', 'Value']])

col1,col2 = st.columns(2)
with col1:
#showing the top 5 valued players in points 
    st.subheader("Top 5 Valued Players ")
    # space line 
    
    top_player_dict = fifa.nlargest(5, 'Value')[['Name', 'Value']].set_index('Name').to_dict()
    for name,value in top_player_dict['Value'].items():
        st.markdown(f"* {name} : {value}")
with col2:
    # draw a graph by plotly 
    st.plotly_chart(px.bar(fifa.nlargest(5, 'Value'), x='Name', y='Value'))
        

    
# players_avr_values= fifa.groupby('Nationality').mean()['Value']

#show unique values in nationality
col1,col2 = st.columns(2)
nationality =fifa.Nationality.unique().tolist()
country_choice= st.selectbox("choose Country", nationality)

st.write(fifa[fifa.Nationality == country_choice]["Value"].mean())

num_cols= fifa.select_dtypes(include=["int64", "float64"]).columns.tolist()
num_feature_choice= st.selectbox("Choose a feature", num_cols)
plot_type= st.selectbox("Choose a plot type", ["Histogram", "Boxplot","Scatter","Violin"])

if plot_type == "Histogram":
    st.write(px.histogram(fifa,x=num_feature_choice,title= num_feature_choice))
elif plot_type == "Boxplot":
    st.write(px.box(fifa,x=num_feature_choice,title= num_feature_choice))
elif plot_type == "Scatter":
    st.write(px.scatter(fifa,x=num_feature_choice,title= num_feature_choice))
else: 
    st.write(px.violin(fifa,x=num_feature_choice,title= num_feature_choice))
    
