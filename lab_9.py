import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data from GitHub repo
url = "https://github.com/esnt/Data/raw/main/Names/popular_names.csv"
df = pd.read_csv(url)

year_range = st.slider("Select Year", min_value=df["year"].min(), max_value=df["year"].max())

# Sidebar - Gender/sex selection
selected_sex = st.radio("Select Gender", options=["Both", "Male", "Female"])

# Filter data based on selected year and gender/sex
if selected_sex == "Both":
    filtered_df = df[df["year"] == year_range]
elif selected_sex == "Male":
    filtered_df = df[(df["year"] == year_range) & (df["sex"] == "M")]
else:
    filtered_df = df[(df["year"] == year_range) & (df["sex"] == "F")]

# Interactive element - Slider to select number of top names
num_top_names = st.slider("Select Number of Top Names", min_value=1, max_value=20, value=10)

# Group by name and sum the counts to get top names
top_names = filtered_df.groupby("name")["n"].sum().sort_values(ascending=False).head(num_top_names)

# Plot bar chart for top names
st.bar_chart(top_names)

# Show selected year and gender/sex
st.write(f"Top {num_top_names} {'Male' if selected_sex == 'Male' else 'Female' if selected_sex == 'Female' else 'Gender-Neutral'} Names for the Year {year_range}")

selected_name = st.selectbox("Select Name", df["name"].unique())

# Filter data for selected name
name_data = df[df["name"] == selected_name]

# Group by year and sum the counts
name_counts_over_time = name_data.groupby("year")["n"].sum()

# Plot line chart
st.line_chart(name_counts_over_time)

# Show selected name
st.write(f"Frequency of Name '{selected_name}' Over Time")