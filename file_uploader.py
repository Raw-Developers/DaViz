import streamlit as st
import os

def file_catcher():
    image_file = st.file_uploader("Upload An Image",type=['csv'])
    if image_file is not None:
        file_details = {"FileName":image_file.name,"FileType":image_file.type}
        st.write(file_details)
        with open("/home/kirti/Desktop/Streamlit/data1.csv","wb") as f: 
            f.write(image_file.getbuffer())
            st.success("Saved File")
