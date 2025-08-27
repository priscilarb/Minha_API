from fastapi import FastAPI
from dio_fastapi_api.routers import api_router
from fastapi_pagination import add_pagination

app = FastAPI(title='MinhaApi')
app.include_router(api_router)
add_pagination(app)
