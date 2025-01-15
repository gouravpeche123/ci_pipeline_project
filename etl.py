
import pandas as pd
import streamlit as st
st.write("welcome to AVD")
data = {
    "Task":["Extract","Transform","Load"],
    "Status":["Completed","Inprogess","Pending"]
}
df = pd.DataFrame(data)
st.write("ETL Pipeline Status",df)


