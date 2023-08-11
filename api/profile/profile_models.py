from pydantic import BaseModel
from datetime import datetime


# Model vhodnix dannix polzovatelya
class UserDent(BaseModel):
    profile_photo: str
    name: str
    surname: str
    phone_number: int
    email: str
    city: str
    reg_date: datetime
    password:str

# Model dlya karti polzovatelya
class CardDent(BaseModel):
    user_id: int
    card_number: int
    cardholder: str
    exp_date: str
    card_balance: float
    card_name: str