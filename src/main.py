from fastapi import FastAPI, APIRouter

import fastapi_swagger_dark as fsd

import uvicorn

from src.config import settings as setting

from src.router.animal import router as animal_router

from src.router.building import router as building_router


app = FastAPI(
    docs_url=f'{setting.BASE_ROUTE_PATH}/docs',
    openapi_url=f'{setting.BASE_ROUTE_PATH}/openapi.json'
)

app.openapi_tags = [
    {
        'name': 'create'
    },
    {
        'name': 'read'
    },
    {
        'name': 'update'
    },
    {
        'name': 'delete'
    }
]

router = APIRouter(prefix=setting.BASE_ROUTE_PATH)

router.include_router(animal_router)
router.include_router(building_router, prefix='/building', tags=['Building'])

fsd.install(router, path="/dark-docs")

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(
        'src.main:app',
        host='localhost',
        port=8000,
        reload=True
    )
