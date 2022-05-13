# Automated birthday wisher
########################################
import pandas as pd
import datetime as dt
import smtplib

# TODO 3. Update the happy birthday email text
def generate_text():
    with open("letter_1.txt", mode="r") as letter:
        cele = letter.read()
        new_letter = cele.replace("[NAME]",name)
        print(new_letter)
    return new_letter

# TODO 4. Send email
def send_email(content):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        provider = "sijia1120@gmail.com"
        password = "Yanyalun19861120"
        contents = f"Subject:Happy Birthday\n\n{content}"
        connection.login(user=provider, password=password)
        connection.sendmail(from_addr=provider, to_addrs=recepient_email, msg=contents)

# TODO 1. Read csv file and save the information in a dictionary
with open("birthdays.csv") as file:
    info = pd.read_csv(file)
    info_dict = info.to_dict("records")
    # to_dict() function: "records": list like [{column -> value}]
    print(info_dict)
    print(info)

# TODO 2. Check today's date and if there are corresponding birthday.
now = dt.datetime.now()
now_month = now.month
now_day =now.day
print(f"Today is {now_month} month, {now_day} day")

for item in info_dict:
    name = item["name"]
    month = item["month"]
    day = item["day"]
    recepient_email = item["email"]
    if int(month) == int(now_month) and int(day) == int(now_day):
        print(f"Today is {name}'s birthday")
        content = generate_text()
        send_email(content=content)
    else:
        print(f" {name} has no birthday today")



