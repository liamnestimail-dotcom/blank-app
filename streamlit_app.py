import streamlit as st

st.title("welcome to🌱 my mini plant game 🌱a jump game with plants")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
plants_list=["standert","spike","bomb","thunder","block"]
#st.write(plants_list)
#st.write("plant_list")
#st.write(plants_list[0])
#st.write(plants_list[1])
#st.write(plants_list[2])
#st.write(plants_list[3])
#st.write(plants_list[4])
#selected_plant=st.selectbox("skin",plants_list)
#st.write("your plant is",selected_plant)
selected_plant=None
selected_plant=st.selectbox("your plant is",plants_list)
if selected_plant:
    st.write("your plant is",selected_plant)