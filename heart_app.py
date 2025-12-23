import os
import pandas as pd
import seaborn as sns
import streamlit as st 
import plotly.express as px
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("Heart Disease Dataset Visualisation")

heart_df = pd.read_csv(os.path.join("heart.csv"))

# 1. Matplotlib- Age Distribution
st.subheader("1. Age Distrbution")


container1 = st.container(width="stretch")
with container1:
    fig1, ax1 = plt.subplots()
    ax1.hist(heart_df['Age'], bins=20, color="steelblue", edgecolor="black")
    ax1.set_xlabel("Age")
    ax1.set_ylabel("Count")
    ax1.set_title("Age Distribution")
    st.pyplot(fig1)

    #2. Seaborn - heart disease by Gender
    st.subheader("2. Heart Disease by Gender")
    fig2, ax2 = plt.subplots()
    sns.countplot(data=heart_df, x="Sex", hue="HeartDisease", palette="icefire", ax=ax2)
    ax2.legend(title="Heart Disease", labels=["No", "Yes"])
    st.pyplot(fig2, use_container_width=True)
# 3. Plotly - Cholesterol vs Max HR
st.subheader("3. Cholesterol vs Max Heart Rate (Plotly)")
fig3 = px.scatter(heart_df, x='Cholesterol', y='MaxHR', color='HeartDisease', color_continuous_scale='RdYlGn_r')
st.plotly_chart(fig3, use_container_width=True)
# 4. Seaborn - Correlation Heatmap
st.subheader("4. Correlation Heatmap (Seaborn)")
fig4, ax4 = plt.subplots(figsize=(10, 6))
numeric_df = heart_df.select_dtypes(include='number')
sns.heatmap(numeric_df.corr(), annot=True, fmt='.2f', cmap='coolwarm', ax=ax4)
st.pyplot(fig4)
# 5. Plotly - Chest Pain Type Distribution
st.subheader("5. Chest Pain Type by Heart Disease (Plotly)")
fig5 = px.histogram(heart_df, x='ChestPainType', color='HeartDisease', barmode='group',
                    color_discrete_sequence=['#2ecc71', '#e74c3c'])
st.plotly_chart(fig5, use_container_width=True)