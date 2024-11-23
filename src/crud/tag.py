from sqlalchemy.orm import Session
from src.models.tag import Tag
from src.schemas.tag import TagCreate

# Obtenemos todos los tags
def get_tags(db: Session):
  return db.query(Tag).all()

# Obtener un tag por el ID
def get_tag_by_id(db: Session, tag_id: int):
  return db.query(Tag).filter(Tag.id == tag_id).first()

# Obtener un tag por el name
def get_tag_by_name(db: Session, name: str):
  return db.query(Tag).filter(Tag.name == name).first()

# Crear un tag
def create_tag(db: Session, tag: TagCreate):
  db_tag = Tag(name=tag.name)
  db.add(db_tag)
  db.commit()
  db.refresh(db_tag)
  return db_tag

# Update de un tag
def update_tag(db: Session, tag_id: int, tag: TagCreate):
  db_tag = db.query(Tag).filter(Tag.id == tag_id).first()
  db_tag.name = tag.name
  db.commit()
  db.refresh(db_tag)
  return db_tag

# Eliminar un tag
def delete_tag(db: Session, tag_id: int):
  db_tag = db.query(Tag).filter(Tag.id == tag_id).first()
  db.delete(db_tag)
  db.commit()
  return db_tag