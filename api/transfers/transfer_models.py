from datetime import datetime
from pydantic import BaseModel


# Model perevoda s karti na kartu
class P2PDent(BaseModel):
    card_from: int
    amount: float
    card_to: int
    transfer_time: datetime
