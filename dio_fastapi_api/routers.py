from fastapi import APIRouter
from dio_fastapi_api.atleta.routes import router as atleta
from dio_fastapi_api.categorias.routes import router as categorias
from dio_fastapi_api.centro_de_treinamento.routes import router as centro_treinamento

api_router = APIRouter()
api_router.include_router(atleta, prefix="/atletas", tags=["atletas"])
api_router.include_router(categorias, prefix="/categorias", tags=["categorias"])
api_router.include_router(centro_treinamento, prefix="/centros_treinamento", tags=["centros_treinamento"])