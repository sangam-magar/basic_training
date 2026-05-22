#displaying  chart and table using streamit and seaborn 
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

st.title("Tips Dataset Analysis Dashboard")

# 1. Average Bill & Tip per Day
st.header("1. Average Bill & Tip per Day")

daily_avg = df.groupby("day")[["total_bill", "tip"]].mean().reset_index()

fig1, ax1 = plt.subplots()
ax1.bar(daily_avg["day"], daily_avg["total_bill"], label="Avg Total Bill")
ax1.bar(daily_avg["day"], daily_avg["tip"], label="Avg Tip")

ax1.set_title("Average Bill & Tip by Day")
ax1.set_ylabel("Amount")
ax1.legend()
st.pyplot(fig1)

st.dataframe(daily_avg)


# =========================
# 2. Tip distribution by Time
# =========================
st.header("2. Tip Distribution by Time (Lunch vs Dinner)")

fig2, ax2 = plt.subplots()
sns.boxplot(data=df, x="time", y="tip", ax=ax2)

ax2.set_title("Tip Distribution by Time")

st.pyplot(fig2)

time_summary = df.groupby("time")[["tip"]].describe()
st.dataframe(time_summary)


# =========================
# 3. Group Size vs Tip
# =========================
st.header("3. Group Size vs Tip Relationship")

fig3, ax3 = plt.subplots()
sns.scatterplot(data=df, x="size", y="tip", ax=ax3)

ax3.set_title("Tip vs Group Size")

st.pyplot(fig3)

size_summary = df.groupby("size")[["tip", "total_bill"]].mean().reset_index()
st.dataframe(size_summary)