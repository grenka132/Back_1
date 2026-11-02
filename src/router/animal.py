from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.DB.session import get_async_session
from src.schema.animal import AnimalCreate, AnimalResponse, AnimalUpdate, Animal
from src.service.animal import AnimalService

router = APIRouter()


@router.get('/hry')
async def hry() -> str:
    return await AnimalService.hry()


@router.post('/hry')
async def create_hry(body: AnimalCreate) -> Animal:
    return await AnimalService.create_hry({'id':0,**body.model_dump()})


@router.post('/DBCreate', tags = ['create'], response_model = AnimalResponse, status_code = status.HTTP_201_CREATED)
async def create_building(animal_in: AnimalCreate, db: AsyncSession = Depends(get_async_session)):  
    return await AnimalService.create(animal_in, db)

@router.get('/DBReadSort', tags = ['read'], response_model = list[AnimalResponse])
async def read_sort(name: str | None = None, sort_by: str = "id", db: AsyncSession = Depends(get_async_session)):
    return await AnimalService.read_sort(name, sort_by, db)

@router.get('/DBReadOne', tags = ['read'], response_model = list[AnimalResponse])
async def read_one(animal_id: int, db: AsyncSession = Depends(get_async_session)):
    return await AnimalService.read_one(animal_id, db)

@router.put('/DBUpdate', tags = ['update'], response_model = AnimalResponse) 
async def update(animal_id: int, animal_in: AnimalUpdate, db: AsyncSession = Depends(get_async_session)):
    return await AnimalService.update(animal_id, animal_in, db)

@router.delete('/DBDelete', tags = ['delete'], status_code = status.HTTP_204_NO_CONTENT)
async def delete(animal_id: int, db: AsyncSession = Depends(get_async_session)):
    return await AnimalService.delete(animal_id, db)
