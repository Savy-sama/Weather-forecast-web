import requests

api_key = "3938d0f2387066d10e7199be37fdf4d5"


def get_data(place, forecast_days):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    no_of_observations = 8 * forecast_days
    filtered_data = filtered_data[:no_of_observations]
    return filtered_data


if __name__ == "__main__":
    get_data(place="Kolkata", forecast_days=2)
