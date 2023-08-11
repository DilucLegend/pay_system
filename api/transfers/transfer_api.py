from main import app
from .transfer_models import P2PDent


# zapros na perevod deneg mejdu kartami
@app.post('/api/transfer-money')
async def money_transfer(transfer_data: P2PDent):
    # Funksiya perevoda deneg
    result = transfer_data
    print(result)

    # yesli kod uspeshniy, to status
    return {'status': 1, 'message': result}

# funktsiya polucheniya poslednix tranzaktviy polzovatelya
@app.get('/api/monitoring')
async def user_payments(user_id: int, card_id: int = 0):
    pass