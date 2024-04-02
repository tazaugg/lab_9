import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data from GitHub repo
url = "https://github.com/esnt/Data/raw/main/Names/popular_names.csv"
df = pd.read_csv(url)

# Sidebar - Year selection
year_range = st.sidebar.slider("Select Year", min_value=df["year"].min(), max_value=df["year"].max())

# Filter data based on selected year
filtered_df = df[df["year"] == year_range]

# Group by name and sum the counts
top_names = filtered_df.groupby("name")["n"].sum().sort_values(ascending=False).head(10)

# Plot bar chart
st.bar_chart(top_names)

# Show selected year
st.write(f"Top 10 Names for the Year {year_range}")

selected_name = st.sidebar.selectbox("Select Name", df["name"].unique())

# Filter data for selected name
name_data = df[df["name"] == selected_name]

# Group by year and sum the counts
name_counts_over_time = name_data.groupby("year")["n"].sum()

# Plot line chart
st.line_chart(name_counts_over_time)

# Show selected name
st.write(f"Frequency of Name '{selected_name}' Over Time")