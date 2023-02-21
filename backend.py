import requests

api_key = "3938d0f2387066d10e7199be37fdf4d5"


def get_data(place, forecast_days, kind):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    no_of_observations = 8 * forecast_days
    filtered_data = filtered_data[:no_of_observations]

    if kind == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    elif kind == "Weather Condition":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]

    return filtered_data


if __name__ == "__main__":
    get_data(place="Kolkata", forecast_days=2, kind="Weather Condition")
