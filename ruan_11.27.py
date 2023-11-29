import pandas as pd
import streamlit as st
import os

csv_file_path = (r"C:\Users\lamarwells\Documents\DockApps\Trailer_count-11.27-3.csv")


script_dir = os.path.dirname(os.path.abspath(csv_file_path))


file_path = os.path.join(script_dir, "Trailer_count-11.27-3.csv")

# Force Streamlit to rerun in "report mode"


st.title("Inbound From Ruan")



df = pd.read_csv(file_path)

st.write("## Trailer Count Wednesday 11-27-2023")
st.write(df)