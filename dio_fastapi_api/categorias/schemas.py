from pydantic import UUID4, Field
from typing import Annotated
from dio_fastapi_api.contrib.schemas import BaseSchema


class CategoriaIn(BaseSchema):
    nome: Annotated[str, Field(description="Nome da categoria", example='Teens', max_length=10)]


class CategoriaOut(CategoriaIn):
    id: Annotated[UUID4, Field(description="ID da categoria")]