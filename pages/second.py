import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

rand = np.random.rand(20, 2)
#two option histogram and scatter
chart = st.selectbox("Select chart", ["Histogram", "Boxplot"])

if chart == "Histogram":
    st.plotly_chart(px.histogram(rand))
else:
    st.plotly_chart(px.box(rand))
