from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.api.deps import get_db
from src.crud import author as author_crud
from src.schemas import author as author_schemas

router = APIRouter()

@router.get('/', response_model=List[author_schemas.Author])
def get_authors(db: Session = Depends(get_db)):
    return author_crud.get_authors(db=db)

@router.get("/{author_id}", response_model=author_schemas.Author)
def get_author_by_id(author_id: int, db: Session = Depends(get_db)):
    db_author = author_crud.get_author_by_id(db, author_id=author_id)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Autor no encontrado")
    return db_author

@router.get("/search/name/{name}", response_model=List[author_schemas.Author])
def search_author_by_name(name: str, db: Session = Depends(get_db)):
    authors = author_crud.get_author_by_name(db, name=name)
    if not authors:
        raise HTTPException(status_code=404, detail="No se encontraron autores con ese nombre")
    return authors

@router.get("/search/email/{email}", response_model=author_schemas.Author)
def search_author_by_email(email: str, db: Session = Depends(get_db)):
    db_author = author_crud.get_author_by_email(db, email=email)
    if db_author is None:
        raise HTTPException(status_code=404, detail="No se encontró autor con ese email")
    return db_author

@router.post("/", response_model=author_schemas.Author)
def create_author(author: author_schemas.AuthorCreate, db: Session = Depends(get_db)):
    return author_crud.create_author(db=db, author=author)

@router.put("/{author_id}", response_model=author_schemas.Author)
def update_author(
    author_id: int,
    author: author_schemas.AuthorCreate,
    db: Session = Depends(get_db)
):
    return author_crud.update_author(db=db, author_id=author_id, author=author)

@router.delete("/{author_id}", response_model=author_schemas.Author)
def delete_author(author_id: int, db: Session = Depends(get_db)):
    return author_crud.delete_author(db=db, author_id=author_id)
