import streamlit as st
from PIL import Image
import pandas as pd

# Upload multiple CSV files
uploaded_csvs = st.file_uploader("Data", type=["csv"], accept_multiple_files=True)

# Upload multiple image files
uploaded_images = st.file_uploader("Results", type=["png", "jpg", "jpeg"], accept_multiple_files=True)

st.title('Stock Market Prediction')
# Display the uploaded CSV files
if uploaded_csvs:
    st.subheader('Data')
    for uploaded_csv in uploaded_csvs:
        st.write(f"File name: {uploaded_csv.name}")
        df = pd.read_csv(uploaded_csv)
        st.write(df)

# Display the uploaded images
if uploaded_images:
    st.subheader('Results')
    for uploaded_image in uploaded_images:
        image = Image.open(uploaded_image)
        st.image(image, caption=uploaded_image.name, use_column_width=True)
