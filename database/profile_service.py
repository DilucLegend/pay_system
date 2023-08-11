from database.models import User, Card
from database import get_db

# Registratsiya

# Funksiya proverki nomera telefona i parolya

# Funksiya dobavleniya karti polzovatelya

# Funksiya polucheniya dannih polzovatelya po user_id

# poluchit vse ili opredelennuyu kartu
def get_all_or_exact_card(user_id, card_id):
    db = next(get_db())

    if card_id == 0:
        return db.query(Card).filter_by(id=card_id).all()

    return db.query(Card).filter_by(id=card_id, user_id=user_id).first()

