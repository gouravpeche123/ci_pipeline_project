
import pandas as pd
import streamlit as st
st.write("welcome to avd to learn bigdata during data engineering course 2025")
st.write("here we are learning data engineering course completely within the 3 months")
data = {
    "Task":["Extract","Transform","Load"],
    "Status":["Completed","Inprogess","Pending"]
}
df = pd.DataFrame(data)
st.write("ETL Pipeline Status",df)
st.write("thank you")

