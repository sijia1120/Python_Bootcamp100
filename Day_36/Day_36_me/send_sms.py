import requests
import os
from twilio.rest import Client

account_sid ="AC6957718c6e35b4c639b20f9df53cec6c"
auth_token ="*********************"
from_num ="+************"
to_num ="+***********"

class SendSMS:
    def __init__(self,content):
        self.body = content
        self.client = Client(account_sid, auth_token)
        self.message = self.client.messages \
            .create(
            body=self.body,
            from_=from_num,
            to=to_num,
     )
