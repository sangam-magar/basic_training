#displaying charts and table using streamlit
import streamlit as st 
import seaborn  as sns 
import matplotlib.pyplot as plt
df =sns.load_dataset("tips")
st.title("scatter plot of tips data table")
st.header("header")
fig, ax =plt.subplots()
sns.scatterplot(data=df, x="day", y ="total_bill", ax=ax)
st.pyplot(fig)
st.header("table")
dftable =df[["day", "total_bill"]]
st.dataframe(dftable)
st.table(dftable)
