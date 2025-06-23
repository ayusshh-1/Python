import requests
import datetime
import os
from dotenv import load_dotenv

load_dotenv()  # add this explicitly
API_ID = os.environ["API_ID"]
API_KEY = os.environ['API_KEY']
exercise_text = input("Tell which exercise you did")
GENDER = "Male"
WEIGHT_KG = 62
HEIGHT_CM = 178
AGE = 20
endpoint_exercise = "https://trackapi.nutritionix.com/v2/natural/exercise"
today = datetime.datetime.now()
now = datetime.datetime.now()
hour = now.time().hour
min = now.time().minute
sec = now.time().second
headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}
query_ex = {
     "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response = requests.post(endpoint_exercise, headers=headers, json=query_ex)
duration = response.json()['exercises'][0]['duration_min']
calorie = response.json()['exercises'][0]['nf_calories']
exercise = (response.json()['exercises'][0]['name']).title()
 # This will give you the nutrition info

sheet_endpoint = os.environ['SHEET_ENDPOINT']

headers = {
    "Authorization": os.environ['TOKEN'],
}
SHEET_NAME = os.environ['SHEET_NAME']
new_workout = {
    SHEET_NAME: {
        "date": today.strftime("%d/%m/%Y"),
        "time": f"{hour}:{min}:{sec}",
        "exercise": exercise,
        "duration": duration,
        "calorie": calorie
    }
}

response = requests.post(url=sheet_endpoint, json=new_workout, headers=headers)

