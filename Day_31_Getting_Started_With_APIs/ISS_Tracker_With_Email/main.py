import requests,datetime,smtplib
#-------------------------------------------------sunrise and sunset------------------------------------------
#according to Ahmedabad Gujarat
my_lat = 23.022505
my_lng = 72.571365
my_email = ""
my_password = ""
parameters = {
    "lat":my_lat,
    "lng":my_lng,
    "formatted":0,
    "tzid":"Indian/Chagos"
}
response_my = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
sunrise = int(response_my.json()['results']['sunrise'].split("T")[1].split(":")[0])
sunset = int(response_my.json()['results']['sunset'].split("T")[1].split(":")[0])
#---------------------------------------------------My Time-------------------------------------------------------
now = datetime.datetime.now()
my_time= now.hour
#------------------------------------------------Stetellite checking---------------------------------------------
reponse_st = requests.get(url="http://api.open-notify.org/iss-now.json")
st_lat = float(reponse_st.json()['iss_position']['latitude'])
st_lng = float(reponse_st.json()['iss_position']['longitude'])
#-------------------------------------------------Notify me ------------------------------------------------------
if (my_lat-5<=st_lat<=my_lat+5) and (my_lng-5<=st_lng<=my_lng+5):
    if my_time >= sunset or my_time <= sunrise:
        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(user=my_email,password=my_password)
            connection.sendmail(from_addr = my_email,
                                to_addrs="receiver_email",
                                msg="Subject:Satellite Above \n\n Look Above")