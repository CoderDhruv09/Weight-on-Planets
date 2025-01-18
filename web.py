
import streamlit as st
from PIL import Image

st.set_page_config(page_title="SpaceWeight", page_icon=":ringed_planet:", layout="wide")
def local_css(file_name) :
   with open(file_name) as f:
       st.markdown(f"<style>{f.read() }</style>", unsafe_allow_html=True)


local_css("style.css")

with st.container():
    st.subheader("Hi, I am Dhruv :wave:")
    st.title("A Student From India")
    st.write("I am passionate about learning tech and coding")
    st.write("This website will go beyond your imagination :exploding_head::exploding_head:")
    st.write("[My YT Channel >](http://www.youtube.com/@dhruv09.)")

#----What the website do for you----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About the Website")
        st.write("##")
        st.write(
            """
            This Website:
            - is about checking what will be your weight on other planets.
            - is made up using python.
            - is user friendly.
            - is hosted by 'Streamlit', special thanks to streamlit.
            """
        )
        st.write("My gmail: dhruvchaudhari468@gmail.com")
        with right_column:
            img = Image.open("coding.png")
            st.image(
            img ,
            width = 450
            )


def local_css(file_name) :
   with open(file_name) as f:
       st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
       local_css("style/style.css")



# Gravity values of planets relative to Earth
planet_gravity = {
    "Mercury": 0.38,
    "Venus": 0.91,
    "Earth": 1.00,
    "Mars": 0.38,
    "Jupiter": 2.34,
    "Saturn": 1.06,
    "Uranus": 0.92,
    "Neptune": 1.19,
    "Pluto": 0.06  # Including Pluto for fun
}

def weight_on_planet(weight_on_earth, planet):
    """Calculate weight on a specified planet."""
    if planet in planet_gravity:
        weight = weight_on_earth * planet_gravity[planet]
        return weight
    return None

# Streamlit interface
st.title("Check Your Weight on Other Planets")

# User input for weight on Earth
weight_on_earth = st.number_input("Enter your weight on Earth (kg):", min_value=0.0, step=0.1)

# User input for selecting planet
planet = st.selectbox("Select a Planet:", list(planet_gravity.keys()))

# Button to calculate weight
if st.button("Calculate"):
    if weight_on_earth > 0:
        weight = weight_on_planet(weight_on_earth, planet)
        st.write(f"Your weight on **{planet}** would be: **{weight:.2f} kg**")
    else:
        st.write("Please enter a valid weight greater than zero.")


with st. container():
    st.write(" --- ")
    st.header("Get In Touch With Me!!")
    st.write("##")
# Documention: https://formsubmit.co/ ||| CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/dhruvchaudhari468@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </ form>
    """
left_column, right_column = st.columns(2)
with left_column:
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    img = Image.open("2477772.png")
            st.image(
            img ,
            width = 450
            )
