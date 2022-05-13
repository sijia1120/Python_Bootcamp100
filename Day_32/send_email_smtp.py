import smtplib
GMAIL_PROVIDER = "smtp.gmail.com"
# Yahoo email provider "smtp.mail.yahoo.com"
##########################################
##### Here is an example of my own personal email based on Gmail provider
##########################################

# Input your email content
content = "Subject:Hello\n\nThis is the body of my email."

######################## MAIN BODY (NO NOT CHANGE) ###################
provider_email = "sijia1120@gmail.com"
provider_password = "yanyalun"
send_to = "839674258@qq.com"


#connetion = smtplib.SMTP(GMAIL_PROVIDER)
#connetion.starttls()
#connetion.login(user=provider_email, password=provider_password)
#connetion.sendmail(from_addr=provider_email,to_addrs=send_to,msg=content)
#connetion.close()


# Second way of using smtplib:
with smtplib.SMTP(GMAIL_PROVIDER) as connection:
    connetion.starttls()
    connetion.login(user=provider_email, password=provider_password)
    connetion.sendmail(from_addr=provider_email,
                       to_addrs=send_to,
                       msg=content)
