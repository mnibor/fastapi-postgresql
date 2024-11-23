from sqlalchemy import Column, BigInteger, String
from sqlalchemy.orm import relationship
from src.db.base_class import Base
from src.models.associations import post_tag

class Tag(Base):
  __tablename__ = 'tags'
  id = Column(BigInteger, primary_key=True, index=True)
  name = Column(String, unique=True, index=True)

  posts = relationship('Post', secondary=post_tag, back_populates='tags')
