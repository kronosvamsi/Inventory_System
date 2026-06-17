from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.settings import settings

engine = create_engine(url = settings.DATABASE_URL,echo= True)
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

""" Db connection check """
# with engine.connect() as conn:
#     print("Db connected successfully!")