from twilio.rest import Client 
from config import account_sid, auth_token, phone_number
"""
GET QOD BY USING REST API
"""
def set_twilio_conection(account_sid,auth_token):
    client = Client(account_sid,auth_token) 
    return client

def send_whatsapp_text(client,quote):
    message = client.messages.create( 
                                  from_='whatsapp:+14155238886',  
                                  body='quote',
                                  to=phone_number
                              ) 
 
    return message.sid

client = set_twilio_conection(account_sid,auth_token)