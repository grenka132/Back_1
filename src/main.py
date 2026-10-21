from fastapi import FastAPI, APIRouter

import fastapi_swagger_dark as fsd

import uvicorn

from src.config import setting

from src.router.animal import router as animal_router



app = FastAPI(
    docs_url=f'{setting.BASE_ROUTE_PATH}/docs',
    openapi_url=f'{setting.BASE_ROUTE_PATH}/openapi.json'
)

router = APIRouter(prefix=setting.BASE_ROUTE_PATH)

router.include_router(animal_router, prefix='/animal', tags=['Animal'])



fsd.install(router, path="/dark-docs")

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(
        'src.main:app',
        host='localhost',
        port=8000,
        reload=True
    )

# Сделать системку для сохранения данных о животных и выдаче их по id (полный CRUD)
# либо в оперативке до перезапуска сервера
# либо в файлик
