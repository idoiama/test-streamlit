import datetime
import time
import pandas as pd
import streamlit as st
from PIL import Image


# Define a title
st.title("Data-rockstars :guitar:")
"""Streamlit-tutorial"""

# Define Header/Subheader
st.header("This is a header")
st.subheader("This is a subheader")

# Define a text
st.text("Text: Hi data-rockstars!")

# Define a Markdown
st.markdown("# This is markdown h1 \n ## This is h2 \n ### This is h3")

st.header("Tex colors and error meassgaes")

st.success("Successful")
st.info("Information!")
st.warning("warning")


# WIDGETS
st.header("Widgets:")
st.subheader("Checkbox")

# Checkbox
if st.checkbox("Show/Hide"):
    st.text("Show or hide Widget")

# SelectBox
st.subheader("SelectBox")
occupation = st.selectbox(
    "Your occupation", ["DS", "DA", "Rockstar", "Enterpreur"]
)
st.write("Selected option:", occupation)

# MultiSelect
st.subheader("MultiSelect")
location = st.multiselect(
    "Work place",
    ("Barcelona","Nepal", "London", "Berlin"),
)
st.write("You've selected:", len(location), "location")

# Slider
st.subheader("Slider")
level = st.slider("Which is your python level?", 1, 5)
st.write("Level:", level)

# Input text
firstname = st.text_input("Which is your first name?:")
if st.button("Accept"):
    result = firstname.title()
    st.success(result)
	
# Date Input
st.subheader("Date input")
today = st.date_input("Today is", datetime.datetime.now())
st.text(f"{today}")

# Time
st.subheader("Time input")
the_time = st.time_input("Right now is ", datetime.time())
st.text(f"{the_time}")


# Images
st.subheader("Image file")
#img = Image.open("example.jpg")
#st.image(img, width=300, caption="Simple Imagen")

# Writing code
st.subheader("Pure code")
st.code("import pandas as np")