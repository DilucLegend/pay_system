from database.models import Transactions, Card
from database import get_db

# Perevod deneg
def money_transfer_db(card_from, card_to, amount, transaction_date):
    db = next(get_db())

    card_from_db = db.query(Card).filter_by(card_from).first()
    card_to_db = db.query(Card).filter_by(card_from).first()

    # proverka yest li eti karti
    if card_from_db and card_to_db:
        # proverka dostatochno li deneg
        if card_from_db.card_balance >= amount:
            card_from_db.card_balance -= amount
            card_to_db.card_balance += amount

            new_transaction = Transactions(card_from=card_from,
                                           card_to=card_to,
                                           amount=amount,
                                           transaction_date=transaction_date)

            db.add(new_transaction)
            db.commit()
            return True
        return 'Недостаточно денег'
# Monitoring po card_id
def get_history_of_transactions():
    pass