from fastapi import Body

from main import app
from .profile_models import UserDent, CardDent


# registratsiya polzovatelya
@app.post('/api/registration-user')
async def user_registration():
    print(UserDent)

    # posle registratsii vidat aydi polzovatelya
    return {'status': 1, 'message': 'Registration completed'}


# Vhod v akkaunt
@app.post('/api/login')
async def login_user(phone_number: int = Body(), password: str = Body()):
    print(phone_number, password)
    # proverka dannix
    checker = None

    # yesli dannie verni, otpravlyayem yuzer aydi i dannie polzovatelya
    return {'status': 1, 'message': 'logged_in'}

# dobavlenie karti v bazu
@app.post('/api/add-card')
async def add_user_card(card_data: CardDent):
    # Vizov funktsii iz bd dlya dobavleniya karti v bazu
    result = card_data
    print(card_data)

    # yesli uspeshno dobavlena karta, to status 1
    return {'result': 1, 'message': result}

# Vivod dannix o polzovatele
@app.get('/api/user_data')
async def get_user_data(user_id: int):
    pass

# vivod vsex ili opredelennih kart polzovatelya
@app.get('/api/user_cards')
async def get_user_cards(user_id: int, card_id: int = 0):
    pass