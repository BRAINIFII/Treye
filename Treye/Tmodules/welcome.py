import os
from twilio.rest import Client

def welcome():
    client = Client()
    from_whatsapp_number='whatsapp:+14155238886'
    to_whatsapp_number="whatsapp:" + os.environ['MY_PHONE_NUMBER']
    print(to_whatsapp_number)
    client.messages.create(body='_*TREYE*_\nThankyou for choosing Treye as your Amazon price tracker.\n\nLets Hope for the best.🤩\n\n💁🏻‍♂For any help contact us on www.github.com/BRAINIFII/Treye',from_=from_whatsapp_number,to = to_whatsapp_number)