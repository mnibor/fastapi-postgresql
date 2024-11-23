from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.api.deps import get_db
from src.crud import tag as tag_crud
from src.schemas import tag as tag_schema

router = APIRouter()

@router.get('/', response_model=List[tag_schema.Tag])
def read_tags(db: Session = Depends(get_db)):
  return tag_crud.get_tags(db)

@router.get('/{tag_id}', response_model=tag_schema.Tag)
def read_tag_by_id(tag_id: int, db: Session = Depends(get_db)):
  db_tag = tag_crud.get_tag_by_id(db, tag_id=tag_id)
  if db_tag is None:
    raise HTTPException(status_code=404, detail='Tag not found')
  return db_tag

@router.get('/name/{name}', response_model=tag_schema.Tag)
def read_tag_by_name(name: str, db: Session = Depends(get_db)):
  db_tag = tag_crud.get_tag_by_name(db, name=name)
  if db_tag is None:
    raise HTTPException(status_code=404, detail='Tag not found')
  return db_tag

@router.post('/create', response_model=tag_schema.Tag)
def create_tag(tag: tag_schema.TagCreate, db: Session = Depends(get_db)):
  db_tag = tag_crud.get_tag_by_name(db, name=tag.name)
  if db_tag:
    raise HTTPException(status_code=400, detail='Tag already registered')
  return tag_crud.create_tag(db=db, tag=tag)

@router.put('/update/{tag_id}', response_model=tag_schema.Tag)
def update_tag(tag_id: int, tag: tag_schema.TagCreate, db: Session = Depends(get_db)):
  db_tag = tag_crud.get_tag_by_id(db, tag_id=tag_id)
  if db_tag is None:
    raise HTTPException(status_code=404, detail='Tag not found')
  return tag_crud.update_tag(db=db, tag_id=tag_id, tag=tag)

@router.delete('/delete/{tag_id}', response_model=tag_schema.Tag)
def delete_tag(tag_id: int, db: Session = Depends(get_db)):
  db_tag = tag_crud.get_tag_by_id(db, tag_id=tag_id)
  if db_tag is None:
    raise HTTPException(status_code=404, detail='Tag not found')
  return tag_crud.delete_tag(db=db, tag_id=tag_id)