import requests
from twilio.rest import Client

api_key = "aaaaaaaaaaaaaaaaaaaaaa"
account_sid = "aaaaaaaaaaaaaaaaaaaaaaa"
auth_token = "aaaaaaaaaaaaaaaaaaaaaaaa"
parameter = {
    "lat": 35.65,
    "lon": 139.83,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameter)
response.raise_for_status()
weather_data = response.json()

for num in range(len(weather_data["list"])):
    condition_code = weather_data["list"][num]["weather"][0]["id"]
    if int(condition_code) < 700:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="☔️☔️☔️",
            from_="+1234455667",
            to="+344556777",
        )
        print(message.status)
        break


