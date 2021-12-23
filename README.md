# Ding team bot :robot:

This is a bot that will text your loved one a daily quote of love

---
## How it works :jigsaw:
---
This robot uses python, the twilio api, and aws lambda to send your loved one everyday at a consistent time.
Unfortunately, this bot requires a lot of setup, as a couple of api keys and accounts must be configured, and you must configure aws lambda to run this script every day.
---
## Setup :gear:
---
### Firstly, we need to give our bot texting capabilities.

follow [this twilio quick start guide] (https://www.twilio.com/docs/sms/quickstart/python#sign-up-for-or-sign-in-to-twilio).

Take note of your
- [ ]TWILIO_ACCOUNT_SID
- [ ]TWILIO_AUTH_TOKEN
- [ ]and Twilio phone number

Follow the quick start guide until you are able to recieve texts from your twilio phone to your desired target phone.
---
### Next, prepare the aws lambda deployment package.

1. Move [src](src) and [lambda_function.py](lambda_function.py) into [package](package)
2. Zip package.
3. Congrats, this is the package that we shall deploy to AWS Lambda.

---

### Next, sign up for a aws lambda account
