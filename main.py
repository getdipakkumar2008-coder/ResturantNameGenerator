import streamlit as st
import langchain_helper

st.title("Restirant Name Generator")
cuisine =st.sidebar.selectbox("Pick a Cuisine", ("Indian","Chinese","Mexican"))


if cuisine:
    response =langchain_helper.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'])
    menu_items = response['menu_items'].strip().split(",")

    for item in menu_items:
        st.write("-",item)

