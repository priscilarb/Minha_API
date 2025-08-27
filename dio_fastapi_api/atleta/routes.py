from datetime import datetime
from uuid import uuid4
from fastapi import APIRouter,Body, HTTPException, status, Depends, Query
from pydantic import UUID4

from dio_fastapi_api.atleta.schemas import AtletaIn, AtletaOut, AtletaUpdate
from dio_fastapi_api.atleta.models import AtletaModel
from dio_fastapi_api.categorias.models import CategoriaModel
from dio_fastapi_api.centro_de_treinamento.models import CentroTreinamentoModel

from dio_fastapi_api.contrib.dependencies import DatabaseDependency
from sqlalchemy.future import select

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from typing import List, Optional

from fastapi_pagination import Page, paginate

router = APIRouter()

@router.post("/", summary="Criar um novo atleta", status_code=status.HTTP_201_CREATED, response_model=AtletaOut)

async def post(db_session = DatabaseDependency, atleta_in: AtletaIn = Body(...) ):
    nome_da_categoria = atleta_in.categoria.nome
    nome_centro_treinamento = atleta_in.centro_treinamento.nome

    categoria = (await db_session.execute(
        select(CategoriaModel).filter_by(nome=nome_da_categoria))
    ).scalars().first()
    
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"A categoria {nome_da_categoria} não foi encontrada.")
    
    centro_treinamento = (await db_session.execute(
        select(CentroTreinamentoModel).filter_by(nome=nome_centro_treinamento))
    ).scalars().first()
    
    if not centro_treinamento:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
        detail=f"O centro de treinamento {nome_centro_treinamento} não foi encontrado.")
    
    try:
        atleta_out = AtletaOut(id=uuid4(), created_at=datetime.utcnow(), **atleta_in.model_dump())
        atleta_model = AtletaModel(**atleta_out.model_dump(exclude={'categoria', 'centro_treinamento'}))

        atleta_model.categoria_id = categoria.pk_id
        atleta_model.centro_treinamento_id = centro_treinamento.pk_id

        db_session.add(atleta_model)
        await db_session.commit()
        
    except IntegrityError as e:
        await db_session.rollback()
        if "cpf" in str(e.orig):
            raise HTTPException(
        status_code=status.HTTP_303_SEE_OTHER,
        detail=f"Já existe um atleta cadastrado com o cpf: {atleta_in.cpf}")
    
        raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Ocorreu um erro ao inserir os dados no banco")


    return atleta_out


@router.get("/", summary="Consultar todos os atletas",
    status_code=status.HTTP_200_OK,
    response_model=Page[AtletaOut],)

async def query(db_session: DatabaseDependency,
                nome: Optional[str] =  Query(None),
                cpf: Optional[int] = Query(None)) -> Page[AtletaOut]:
    query = select(AtletaModel)

    if nome:
        query = query.filter(AtletaModel.nome.ilike(f"%{nome}%"))
    if cpf:
        query = query.filter(AtletaModel.cpf == cpf)

    atletas = (await db_session.execute(query)).scalars().all()
    
    return paginate ([AtletaOut.model_validate(atleta) for atleta in atletas])


@router.get("/{id}", 
    summary="Consultar um atleta pelo id",
    status_code=status.HTTP_200_OK,
    response_model=AtletaOut,)

async def get(id: UUID4, db_session: DatabaseDependency) -> AtletaOut:
    atleta: AtletaOut = (await db_session.execute(select(AtletaModel).filter_by(id=id))
    ).scalars().first()

    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Atleta não encontrado no id: {id}")
    
    return atleta


@router.patch("/{id}", 
    summary="Editar um Atleta pelo id",
    status_code=status.HTTP_200_OK,
    response_model=AtletaOut,)

async def patch(id: UUID4, db_session: DatabaseDependency, atleta_up: AtletaUpdate = Body(...)) -> AtletaOut:
    atleta: AtletaOut = (await db_session.execute(select(AtletaModel).filter_by(id=id))
    ).scalars().first()

    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Atleta não encontrado no id: {id}")
    
    atleta_update = atleta_up.model_dump(exclude_unset=True)
    for key, value in atleta_update.items():
        setattr(atleta, key, value)

    await db_session.commit()
    await db_session.refresh(atleta)

    return atleta


@router.delete("/{id}", 
    summary="Deletar um Atleta pelo id",
    status_code=status.HTTP_204_NO_CONTENT)

async def delete(id: UUID4, db_session: DatabaseDependency) -> None:
    atleta: AtletaOut = (await db_session.execute(select(AtletaModel).filter_by(id=id))
    ).scalars().first()

    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Atleta não encontrado no id: {id}")
    
    await db_session.delete(atleta)
    await db_session.commit()
