import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

user = "root"
password = "root"
host = "localhost"
port = 3306
database = "deptemp"

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")

st.title("MARKS Distribution")

def load_data():
    df = pd.read_sql("select * from stms;", engine)
    return df

if st.button("Show Data"):
    df = load_data()
    st.dataframe(df)

if st.button("Show Graph"):
    df = load_data()
    plt.bar(df['name'], df['marks'])
    plt.xlabel('NAME')
    plt.ylabel('MARKS')
    plt.title('MARKS Distribution')
    st.pyplot(plt.gcf())