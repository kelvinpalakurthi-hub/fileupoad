import streamlit as st
import pandas as pd
st.title("File Upload & Visualization")
file=st.file_uploader("Upload CSV file",type="csv")
if file:
    df=pd.read_csv(file)
    df=df[["TV Ad Budget ($)","Sales ($)"]]
    st.write("Data Preview")
    st.dataframe(df)
    st.write("Line Chart")
    st.line_chart(df)
    st.write("BAR CHART")
    st.bar_chart(df)


