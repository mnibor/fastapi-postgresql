from sqlalchemy import Column, BigInteger, String
from sqlalchemy.orm import relationship
from src.db.base_class import Base

class Author(Base):
  id = Column(BigInteger, primary_key=True, index=True)
  name = Column(String)
  email = Column(String, unique=True, index=True)

  posts = relationship('Post', back_populates='author')
