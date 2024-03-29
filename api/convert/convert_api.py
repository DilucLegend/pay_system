import requests
from main import app


# Poluchit kurs ЦБ i nashego servera
@app.get('/api/get-currency')
async def currency_rate():
    # podklyuchenie k api ЦБ
    cb_api = requests.get('https://cbu.uz/ru/arkhiv-kursov-valyut/json/').json()

    # Poluchayem kurs neobhodimix valyut
    usd_rate = cb_api[0]['Rate']
    eur_rate = cb_api[1]['Rate']
    rub_rate = cb_api[2]['Rate']

    # Vidayom otvet
    return {'status': 1, 'rates':{'USD': usd_rate,
                                  'EUR': eur_rate,
                                  'RUB': rub_rate}}