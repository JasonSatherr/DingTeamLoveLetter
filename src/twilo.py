from twilio.rest import Client
# from decouple import config
import os

class TwiloAPI:
    def __init__(self) -> None:
        #account_sid = config('TWILIO_ACCOUNT_SID')
        account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
        auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
        self.from_ = os.environ.get('TWILO_PHONE_NUMBER')
        self.to_ = os.environ.get('SEND_TO_PHONE')
        # auth_token = config('TWILIO_AUTH_TOKEN')
        # self.from_ = config('TWILO_PHONE_NUMBER')
        # self.to_ = config('SEND_TO_PHONE')
        self.client = Client(account_sid, auth_token)


    def sendMessage(self, message: str = "Good day"):
        message = self.client.messages \
                .create(
                     body=message,
                     from_= self.from_,
                     to=self.to_
                 )
        # print(message.sid)



