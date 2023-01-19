import requests
from twilio_connection import send_whatsapp_text,client


def get_quote_of_the_day(category):
    url = "https://quotes.rest/qod?language=en&category={}".format(category)
    res = requests.get(url=url)
    data = res.json()
    status = res.status_code
    match status:
        case 200:
            quote = data['contents']['quotes'][0]['quote']
        case 400:
            quote = data['error']['message']
        case _:
            quote = "Sorry, could not find"
    quote = (data['contents']['quotes'][0]['quote'])
    return quote
quote = get_quote_of_the_day(category="inspire")
send_whatsapp_text(client,quote)






