
import pandas as pd
import streamlit as st
st.write("welcome to AVD 2025 for Data Engineering now we are learning azure pyspark here")
data = {
    "Task":["Extract","Transform","Load"],
    "Status":["Completed","Inprogess","Pending"]
}
df = pd.DataFrame(data)
st.write("ETL Pipeline Status",df)


