import streamlit as st
import pandas as pd
import time 
from datetime import datetime

# Get current date and time
ts = time.time()
date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
timestamp = datetime.fromtimestamp(ts).strftime("%H:%M-%S")

# Import st_autorefresh from streamlit_autorefresh
from streamlit_autorefresh import st_autorefresh

# Set up autorefresh
count = st_autorefresh(interval=2000, limit=100, key="fizzbuzzcounter")

# Display FizzBuzz logic based on the count
if count == 0:
    st.write("Count is zero")
elif count % 3 == 0 and count % 5 == 0:
    st.write("FizzBuzz")
elif count % 3 == 0:
    st.write("Fizz")
elif count % 5 == 0:
    st.write("Buzz")
else:
    st.write(f"Count: {count}")

# Read the CSV file and display it in a dataframe
csv_file_path = f"Attendance/Attendance_{date}.csv"
try:
    df = pd.read_csv(csv_file_path)
    st.dataframe(df.style.highlight_max(axis=0))
except FileNotFoundError:
    st.error(f"File {csv_file_path} not found.")
