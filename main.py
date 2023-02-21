import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather forcast for Next Days")

place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of days to be forecasted")
option = st.selectbox("Select the data to view", ("Temperature",
                                                  "Weather Condition"))

st.subheader(f"{option} for the next {days} in {place}")

get_data(place, days, option)

dates = []
temperature = []
figure = px.line(x=dates, y=temperature, labels={"x:" "Dates",
                                                 "y:" "Temperature(C)"})
st.plotly_chart(figure)
