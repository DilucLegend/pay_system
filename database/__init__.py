from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://postgres:Admin@localhost/pay_system')
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# generator soyedeneniy
def get_db():
    db = SessionLocal()

    try:
        yield db
    except:
        db.rollback()
    finally:
        db.close()

from database import models