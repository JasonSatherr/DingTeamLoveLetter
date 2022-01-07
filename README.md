# Ding team bot :robot:

This is a bot that will text your loved one a daily quote of love

![video of bot](./ReadmeMedia/loveBotInAction.gif)

---
## How it works :jigsaw:
---

This robot uses python, the twilio api, and aws lambda to send your loved one everyday at a consistent time.

Unfortunately, this bot requires a lot of setup, as a couple of api keys and accounts must be configured, and you must configure aws lambda to run this script every day.

---
## Setup :gear:
---

1. ### Firstly, we need to give our bot texting capabilities.

  Follow [this twilio quick start guide] (https://www.twilio.com/docs/sms/quickstart/python#sign-up-for-or-sign-in-to-twilio).

  Take note of your
  - [ ]TWILIO_ACCOUNT_SID
  - [ ]TWILIO_AUTH_TOKEN
  - [ ]and Twilio phone number

  Follow the quick start guide until you are able to recieve texts from your twilio phone to your desired target phone.

  ---

2.  ### Next, prepare the aws lambda deployment package.
  This is the code that will automatically be run
  
  1. Move [src](src) and [lambda_function.py](lambda_function.py) into [package](package)
  2. Zip package.
  3. Congrats, this is the package that we shall deploy to AWS Lambda.

  ---

3.  ### Next, sign up for a aws account  
4.  ### Navigate to the aws lambda console, and create a new function.
5.  ### Upload the zipped aws lambda deployment package we created in step 2.
6.  ### Under runtime settings, set Handler to lambda_function.lambda_handler
7.  ### Add a EventBridge (cloudwatch) trigger that runs when you want it to.
    - I have my schedule expression to be cron(00 16 * * ? *)
8. ### Finally, add these env variables
![picture of env vars](./ReadmeMedia/env_vars.PNG)

# :partying_face: YAY, YOU NOW HAVE A BOT TO TEXT THE LOVE OF YOUR LIFE EVERYDAY!!
