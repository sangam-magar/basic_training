#creating  charts and table 
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
# df =sns.load_dataset("iris")
# setosa =df.loc[df["species"] =="setosa"]
# area =((["sepal_length"]*setosa["sepal_width"])+(setosa["petal_length"]*setosa["petal_widdth"]))
# avg_flower =area.mean()
# flower_list =["setosa",avg_flower]
# print(flower_list)



df = sns.load_dataset("tips")
st.title("Analyzing Tips Data")
st.subheader("Table 1")
st.write("Finding highest to lowest sales")
bill = df.groupby("day")["total_bill"].sum().sort_values(ascending=False)
st.dataframe(bill)
st.table(bill)
st.title("Chart Analysis")
st.subheader("Chart 1")
st.write("Bar chart of sales by day")
fig, ax = plt.subplots()
sns.barplot(x=bill.index, y=bill.values, ax=ax)
st.pyplot(fig)

#creating line chart 
df1 = sns.load_dataset("flights")
st.title("Analyzing Flights Data")
monthly_passengers = df1.groupby("month")["passengers"].sum()
st.subheader("Chart 2")
fig2, ax2 = plt.subplots()
sns.lineplot(x=monthly_passengers.index, y=monthly_passengers.values, ax=ax2)
st.pyplot(fig2)
st.subheader("Table 2")
chart = monthly_passengers.sort_values(ascending=False)
st.dataframe(chart)
st.table(chart)
