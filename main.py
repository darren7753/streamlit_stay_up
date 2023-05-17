# Importing the required libraries
import pandas as pd
import time
from datetime import datetime
from selenium import webdriver

# Loading the data containing information about my Streamlit apps
df = pd.read_excel("streamlit_apps.xlsx")
df = df.sort_values("Name").reset_index(drop=True)

# Visiting each of my Streamlit app and noting the timestamp when visiting
driver = webdriver.Chrome()
timestamps = []

for i,j in zip(df["Name"], df["Link"]):
    current_timestamp = datetime.now()
    driver.get(j)
    time.sleep(10)
    timestamps.append(current_timestamp)

driver.quit()

# Converting the dataframe to Markdown format
markdown_df = df.copy()
markdown_df["Last Visited"] = timestamps
markdown_df["Last Visited"] += pd.Timedelta(hours=7)
markdown_df["Name"] = [f"[{i}]({j})" for i, j in zip(markdown_df["Name"], markdown_df["Link"])]
markdown_df = markdown_df.drop("Link", axis=1)

# Updating the README file
intro_text = '''# Streamlit Stay Up

This is a simple Python script automated by GitHub Actions to visit my Streamlit apps once every Monday and Friday to prevent them from going to sleep.

'''
with open("README.md", "w", encoding="utf-8") as f:
    f.write(intro_text)
with open("README.md", "a", encoding="utf-8") as f:
    f.write(markdown_df.to_markdown(index=False))