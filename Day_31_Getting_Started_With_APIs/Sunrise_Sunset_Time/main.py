import requests
parameters = {
#according to Ahmedabad Gujarat
    "lat":23.022505,
    "lng":72.571365,
    "formatted":0,
    "tzid":"Indian/Chagos"
}
response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
sunrise = response.json()['results']['sunrise']
sunset = response.json()['results']['sunset']
print(sunrise)
print(sunset)
