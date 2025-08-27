from typing import Annotated, Optional
from pydantic import Field, PositiveFloat, UUID4
from datetime import date
from dio_fastapi_api.categorias.schemas import CategoriaIn
from dio_fastapi_api.centro_de_treinamento.schemas import CentroTreinamentoAtleta

from dio_fastapi_api.contrib.schemas import BaseSchema, OutMixin

from dio_fastapi_api.categorias.schemas import CategoriaOut
from dio_fastapi_api.centro_de_treinamento.schemas import CentroTreinamentoOut


class Atleta(BaseSchema):
    nome: Annotated[str, Field(description="Nome do atleta", example="Pedro", max_length=50)]
    cpf: Annotated[str, Field(description="CPF do atleta", example='12345678900', max_length=11)]
    data_nascimento: Annotated[date, Field(description="Data de nascimento do atleta", example="1990-01-01")]
    peso: Annotated[PositiveFloat, Field(description="Peso do atleta", example=60.5)]
    altura: Annotated[PositiveFloat, Field(description="Altura do atleta", example=1.90)]
    sexo: Annotated[str, Field(description="Sexo do atleta", example="M", max_length=1)]
    categoria: Annotated[CategoriaIn, Field(description="Categoria do atleta")]
    centro_treinamento: Annotated[CentroTreinamentoAtleta, Field(description="Centro de treinamento do atleta")]


class AtletaIn(Atleta):
    pass


class AtletaOut(Atleta, OutMixin):
    id: UUID4
    nome: str
    cpf: str
    data_nascimento: date
    peso: float
    altura: float
    sexo: str
    categoria: CategoriaOut
    centro_treinamento: CentroTreinamentoOut

    class Config:
        orm_mode = True

class AtletaUpdate(BaseSchema):
    nome: Annotated[Optional[str], Field(None, description="Nome do atleta", example="Pedro", max_length=50)]
    data_nascimento: Annotated[Optional[date], Field(None, description="Data de nascimento do atleta", example="1990-01-01")]

