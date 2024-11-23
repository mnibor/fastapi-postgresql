from typing import Generator
from src.db.session import SessionLocal

def get_db() -> Generator:
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()