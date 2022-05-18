import requests
import os
from twilio.rest import Client

account_sid ="AC6957718c6e35b4c639b20f9df53cec6c"
auth_token ="3efc35a2b5c405a5c5206c3faaaad977"
from_num ="+19282499040"
to_num ="+4407410499352"

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