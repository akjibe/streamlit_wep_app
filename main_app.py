import streamlit as st
from PIL import Image

st.title('アプリ')
st.caption('テストアプリ！')
# 11
image = Image.open("./data/15puzzle.png")
st.image(image, width=200)