
from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.models.author import Author
from src.schemas.author import AuthorCreate

def get_authors(db: Session) -> List[Author]:
    return db.query(Author).all()

def get_author_by_id(db: Session, author_id: int):
    return db.query(Author).filter(Author.id == author_id).first()

def get_author_by_name(db: Session, name: str) -> List[Author]:
    return db.query(Author).filter(Author.name.ilike(f"%{name}%")).all()

def get_author_by_email(db: Session, email: str):
    return db.query(Author).filter(Author.email == email).first()

def create_author(db: Session, author: AuthorCreate) -> Author:
    # Verificar si ya existe un autor con el mismo email
    existing_author = get_author_by_email(db, email=author.email)
    if existing_author:
        raise HTTPException(
            status_code=400,
            detail="Ya existe un autor con este correo electrónico"
        )

    db_author = Author(**author.model_dump())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def update_author(db: Session, author_id: int, author: AuthorCreate) -> Author:
    db_author = get_author_by_id(db, author_id)
    if not db_author:
        raise HTTPException(status_code=404, detail="Autor no encontrado")

    db_author.name = author.name
    db_author.email = author.email
    db.commit()
    db.refresh(db_author)
    return db_author

def delete_author(db: Session, author_id: int) -> Author:
    db_author = get_author_by_id(db, author_id)
    if not db_author:
        raise HTTPException(status_code=404, detail="Autor no encontrado")

    db.delete(db_author)
    db.commit()
    return db_author
