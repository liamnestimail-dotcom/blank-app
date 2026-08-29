import streamlit as st
import pandas as pd
st.title("welcome to🌱 my mini plant game 🌱a jump game with plants")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
plants_list=["standard","spike", "bomb","thunder"]
#st.write(plants_list)
#st.write("plant_list")
#st.write(plants_list[0])
#st.write(plants_list[1])
#st.write(plants_list[2])
#st.write(plants_list[3])
#selected_plant=st.selectbox("skin",plants_list)
#st.write("your plant is",selected_plant)
selected_plant=None
selected_plant=st.selectbox("your plant is",plants_list)
if selected_plant:
    st.write("your plant is",selected_plant)

images_list=["plant_images/standard.jpeg","plant_images/spike.jpeg","plant_images/bomb.jpeg","plant_images/thunder.jpeg"]
st.image(images_list[0])

choices_df=pd.DataFrame({"plants":plants_list,"plant_images":images_list3})
st.dataframe(choices_df)


