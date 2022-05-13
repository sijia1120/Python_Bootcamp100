# Requirement of this project.
# Objective: send a motivational quoe via email on the current weekday (you can change it to Monday after)
import random
import datetime as dt
import smtplib

# TODO 1. Read the file and get the quotes
with open("quotes.txt", mode="r") as file:
    # read the file line-by-line and put lines into list
    lines = file.readlines()
    list = [line.strip() for line in lines]
quote = random.choice(list)
quote_list = quote.split("-")
quote=quote_list[0].strip('"')
content = f'{quote_list[1]}:\n\t{quote}'
print(content)

# TODO 3. Send email functions
def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        provider = "sijia1120@gmail.com"
        pw = "yanyalun"
        recipent ="839674258@qq.com"
        content = f"Subject:Happy new Week\n\n{quote} :)"
        connection.login(user=provider, password=pw)
        connection.sendmail(from_addr=provider, to_addrs=recipent,msg=content)

# TODO 2. Check wether the current date is Mondy
now = dt.datetime.now()
# return is the <class 'datetime.datetime'>
print(now)
#
if now.weekday() == 0:
    print(f"today is {now.weekday()}")
    send_email()
else:
    print("today is not monday")
    print(f"Today is {now.weekday()}")

##########################################
## From course learning

# year = now.year
# month =now.month
# day = now.day
# day_of_week = now.weekday()
# print(year, type(year))
# print(day_of_week)

# < class 'int'>
# date_of_birth = dt.datetime(year=1998, month=9,day=5,hour=7)
# print(date_of_birth)
