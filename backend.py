import requests

api_key = "3938d0f2387066d10e7199be37fdf4d5"


def get_data(place, forcast_days, kind):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    get_data(place="Kolkata")
