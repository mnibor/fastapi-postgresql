from sqlalchemy import Column, BigInteger, String
from sqlalchemy.orm import relationship
from src.db.base_class import Base
from src.models.post import post_tag

class Tag(Base):
  id = Column(BigInteger, primary_key=True, index=True)
  name = Column(String, unique=True, index=True)

  posts = relationship('Post', secondary=post_tag, back_populates='tags')
