import streamlit as st
import plotly.express as px
from backend import get_data

# Adding Title, Input, Slider, selectbox and subheader
st.title("Weather forcast for Next Days")

place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of days to be forecasted")
option = st.selectbox("Select the data to view", ("Temperature",
                                                  "Weather Condition"))

st.subheader(f"{option} for the next {days} in {place}")

if place:
    # Getting the data for temperature/weather condition
    filtered_data = get_data(place, days)

    if option == "Temperature":
        # Creating a Temperature plot
        temp = [dict["main"]["temp"] for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=dates, y=temp, labels={"x:" "Dates",
                                                  "y:" "Temperature(C)"})
        st.plotly_chart(figure)

    elif option == "Weather Condition":
        condition = [dict["weather"][0]["main"] for dict in filtered_data]
        images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                  "Rain": "images/rain.png", "Snow": "images/snow.png"}
        image_path = [images[sky] for sky in condition]
        st.image(image_path, width=100)
