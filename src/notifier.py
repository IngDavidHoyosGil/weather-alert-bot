import time
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
PRIVATE_NUMBER = os.getenv("PRIVATE_NUMBER")


def send_message(message_string):
    time.sleep(2)
    
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    
    message = client.messages \
                    .create(
                        body = message_string,
                       from_ = "whatsapp:+14155238886",
                        to = 'whatsapp:'+ PRIVATE_NUMBER
                    )

    print('Message acknowledged ' + message.sid)
    print(message.status)