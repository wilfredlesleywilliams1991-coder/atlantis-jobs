import os
from twilio.rest import Client

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_TOKEN = os.getenv("TWILIO_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")

client = Client(TWILIO_SID,TWILIO_TOKEN)

def send_job_alert(phone, job_title, match_score):
    message = f"Atlantis Jobs: {job_title} matched {match_score}% to your CV!"
    client.messages.create(body=message,from_=TWILIO_WHATSAPP_NUMBER,to=f"whatsapp:{phone}")
    print(f"WhatsApp sent to {phone}: {message}")
