import streamlit as st

agree = st.checkbox('I agree')

if agree:
    st.write('Great!')


# image example
import streamlit as st
from PIL import Image

# Title
st.title("Display Image Example")

# Load image
image = Image.open("img.jpg")

# Display image
st.image(image, caption='Example Image', use_column_width=True)
