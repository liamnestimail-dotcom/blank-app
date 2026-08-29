import streamlit as st
import pandas as pd
st.title("welcome to🌱 my mini plant game 🌱a jump game with plants")
st.write(
    "Let's start with choosing your plant" 
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


#selected_plant=None
#selected_plant=st.selectbox("your plant is",plants_list)
#if selected_plant:
#    st.write("your plant is",selected_plant)

images_list=["plant_images/standard.jpeg","plant_images/spike.jpeg","plant_images/bomb.jpeg","plant_images/thunder.jpeg"]
#st.image(images_list[0])

choices_df=pd.DataFrame({"plants":plants_list,"plant_images":images_list})
#st.dataframe(choices_df)

col1, col2 =st.columns(2)

with col1:
    new_choice=st.selectbox("Your plant is", choices_df["plants"])
    with st.expander("show table"):
        st.dataframe(choices_df)
with col2:
    image=choices_df[choices_df["plants"]==new_choice]["plant_images"].iloc[0]
    st.image(image,width=300)


st.balloons()