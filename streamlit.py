
import streamlit as st
import pandas as pd
import altair as alt
from file_uploader import *
import string


file_catcher()
df = pd.read_csv("/home/kirti/Desktop/Streamlit/data1.csv")
df.columns = df.columns.str.replace(' ', '_')
df.columns = df.columns.str.replace('\n', '_')
df.columns = df.columns.str.replace('\t', '_')
cols = st.multiselect("Choose columns", list(df.columns))

if not cols:
    st.error("Please select any two columns.")

else:
    plots = ['Area','Bar','Circle','Geoshape','Image','Line','Point','Rectangle','Rule','Square','Text','Tick']
    selplot = st.selectbox("Select the type of plot", plots)
    if selplot=='Area':
        chart=alt.Chart(df).mark_area(filled=True).encode(alt.X(cols[0]), alt.Y(cols[1]))
    elif selplot=='Bar':
        chart=alt.Chart(df).mark_bar(filled=True).encode(alt.X(cols[0]), alt.Y(cols[1]))
    elif selplot=='Circle':
        chart=alt.Chart(df).mark_circle(filled=True).encode(alt.X(cols[0]), alt.Y(cols[1]))
    elif selplot=='Geoshape':
        chart=alt.Chart(df).mark_geoshape(filled=True).encode(alt.X(cols[0]), alt.Y(cols[1]))
    elif selplot=='Image':
        chart=alt.Chart(df).mark_image(filled=True).encode(alt.X(cols[0]), alt.Y(cols[1]))
    elif selplot=='Line':
        chart=alt.Chart(df).mark_line(filled=True).encode(alt.X(cols[0]), alt.Y(cols[1]))
    elif selplot=='Point':
        chart=alt.Chart(df).mark_point(filled=True).encode(alt.X(cols[0]), alt.Y(cols[1]))
    elif selplot=='Rectangle':
        chart=alt.Chart(df).mark_rect(filled=True).encode(alt.X(cols[0]), alt.Y(cols[1]))
    elif selplot=='Rule':
        chart=alt.Chart(df).mark_rule(filled=True).encode(alt.X(cols[0]), alt.Y(cols[1]))
    elif selplot=='Square':
        chart=alt.Chart(df).mark_square(filled=True).encode(alt.X(cols[0]), alt.Y(cols[1]))
    elif selplot=='Text':
        chart=alt.Chart(df).mark_text(filled=True).encode(alt.X(cols[0]), alt.Y(cols[1]))
    elif selplot=='Tick':
        chart=alt.Chart(df).mark_tick(filled=True).encode(alt.X(cols[0]), alt.Y(cols[1]))

    st.altair_chart(chart, use_container_width=True)
