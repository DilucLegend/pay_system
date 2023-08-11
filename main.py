from fastapi import FastAPI

app = FastAPI(docs_url='/')

# import vsex komponentov
from api.profile import profile_api
from api.convert import convert_api
from api.transfers import transfer_api
