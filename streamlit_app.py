import requests
import streamlit as st
import streamlit_lottie as st_lottie
from PIL import Image


#def load_lottieurl(url):
   # r = requests.get(url)
    #if r.status_code != 200:
     #   return None
    #return r.json()

#---ASSETS
#weightlifting = load_lottieurl("https://lottie.host/2fd942eb-36b2-4503-a389-690e3c636ae5/ztnNZi7pxo.json")
driscoll = Image.open("images/driscoll.png")

st.set_page_config(page_title="Seth Roberts", page_icon=":victory_hand:", layout="wide")

#HEADER SECTION
#with st.container():
   # left_column, right_column = st.columns(2)
    #with left_column:
st.subheader("Hi, I am Seth :wave:")
st.title("I work in Literature Ministries for the Michigan Conference")
st.write("I'm passionate about using literature evangelism to change the lives of young people around the world.")
st.write("[Learn More >](https://www.miyouthrush.org)")
    
    #with right_column:
      #  st.write("Test")
        #st_lottie(weightlifting, height=300, key="weight-lifting")


# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Writing")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(driscoll)
    with text_column:
        st.subheader("How to Fix a Broken Church: Mars Hill, 3rd John, and Why We Need Church Accountability")
        st.write(
            """
            Back in 2018, a charismatic megachurch pastor named Mark Driscoll was riding high. 
            18 years ago, he had started a church plant in inner-city Seattle 
            called Mars Hill with a handful of Christians...
            """
        )
        st.markdown("[Read Full Article on Substack](https://sethroberts.substack.com/p/how-to-fix-a-broken-church)")