import pandas as pd
import streamlit as st

# Force Streamlit to rerun in "report mode"


st.title("Inbound From Ruan")



df = pd.read_csv('C:\\Users\\lamarwells\\OneDrive - Doosan\\GWN_APPS\\DockApps\\Trailer_count-11.27-3.csv')

st.write("## Trailer Count Wednesday 11-27-2023")
st.write(df)