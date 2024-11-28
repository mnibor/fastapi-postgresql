from sqlite3.dbapi2 import version
from fastapi import FastAPI
from src.core.config import settings
from src.api.routes import authors, posts, tags

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

app.include_router(tags.router, prefix='/tags', tags=['Etiquetas (tags)'])
app.include_router(authors.router, prefix='/authors', tags=['Autores (authors)'])
