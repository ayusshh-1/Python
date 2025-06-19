import requests
from twilio.rest import Client
account_sid = 'your twilio account sid'
auth_token = 'your twilio auth token'
twilio_number = ''  # Your Twilio trial number
to_number = ''   # Verified recipient number (e.g., your personal number)
api_key = "your open weather api key"
api_parameters = {
    'lat':23.014509,##this is according to Ahmedabad Gujarat
    'lon':72.591759,
    'appid':api_key,
    'cnt':4
}
#api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
response  = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=api_parameters)
weather = response.json()
weather_set=False
for i in range(0,4):
    weather_id = weather['list'][i]['weather'][0]['id']
    if weather_id<700:
        weather_set = True
        print(weather_id)
if weather_set:
    client = Client(account_sid, auth_token)
    # Send SMS
    message = client.messages.create(
        body="It is going to be rain ⛈️ dont forget to bring Umbrella☂️",
        from_=twilio_number,
        to=to_number
    )
    print(message.status)
