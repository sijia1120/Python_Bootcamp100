# Day 33 Project 2: Sunrise, sunset and ISS Notifier project
import requests
from datetime import datetime
import time
import smtplib
LANTITUDE = 51.509865
LONGITUDE = -0.118092

# TODO 4. CHECK IF WE ARE AT NIGHT
def day_night(sunrise,sunset,now):
    if int(now) < int(sunrise) or int(now)> int(sunset):
        print("Night")
        return True
    elif int(now) > int(sunrise) and int(now) < int(sunset):
        print("Day")
        return False

# TODO 5. CHECK IF ISS IN OUR LOCATION
def iss_loca(iss_lon,iss_lat):
    global LANTITUDE,LONGITUDE
    lan = float(LANTITUDE) - float(iss_lat)
    lon = float(LONGITUDE) - float(iss_lon)
    if (lan<0 and lan>-5) or (lan>0 and lan<5):
        if (lon<0 and lon>-5) or (lon>0 and lon<5):
            print("ISS is here")
            return True
    else:
        print("ISS is not here")
        return False


# TODO 6. Send email
def send_email():
    print("ISS is at our top")
 #   with smtplib.SMTP("smtp.gmail.com") as connection:
 #       connection.starttls()
 #       connection.login(user="sijia1120@gmail.com",password="Yanyalun19861120")
 #       connection.sendmail(from_addr="sijia1120@gmail.com",
 #                           to_addrs="sijia1120@gmail.com",
 #                           msg="Subject:Look up.\t\tThe ISS is at our top")


# TODO 1. EXTRACT THE SUNRISE AND SUNSET HOURS
sun_time_API = "https://api.sunrise-sunset.org/json"
sun_parameters = {
    "lat":LANTITUDE,
    "lng":LONGITUDE,
    "formatted":0
}
sun = requests.get(url=sun_time_API,params=sun_parameters)
sun.raise_for_status()
sun_data = sun.json()
print(sun_data)
sunrise = sun_data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = sun_data["results"]["sunset"].split("T")[1].split(":")[0]
print(f"The sunrise time of London is {sunrise}.")
print(f"The sunset time of London is {sunset}.")

# TODO 2. GET THE CURRENT TIME
now_hour = datetime.now().hour
print(f"The current hour is {now_hour}.")

day_night_check =day_night(sunrise=sunrise, sunset=sunset,now=now_hour)

# TODO 3. GET THE ISSS LOCATION
iss = requests.get(url="http://api.open-notify.org/iss-now.json")
iss.raise_for_status()
iss_data = iss.json()
iss_lon=iss_data["iss_position"]["longitude"]
iss_lat=iss_data["iss_position"]["latitude"]
print(f"The iss longitude is {iss_lon} and the latitude is {iss_lat}.")

iss_location = iss_loca(iss_lon=iss_lon, iss_lat=iss_lat)

while True:
    time.sleep(120)
    if iss_location and day_night_check:
        send_email()
    else:
        print("ISS is not here or not at night.")
