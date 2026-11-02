from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.DB.session import get_async_session
from src.schema.building import BuildingCreate, BuildingResponse, BuildingUpdate
from src.service.building import BuildingService


router = APIRouter()


@router.post('/DBCreate', tags = ['create'], response_model = BuildingResponse, status_code = status.HTTP_201_CREATED)
async def create_building(building_in: BuildingCreate, db: AsyncSession = Depends(get_async_session)):  
    return await BuildingService.create(building_in, db)

@router.get('/DBReadSort', tags = ['read'], response_model = list[BuildingResponse])
async def read_sort(name: str | None = None, sort_by: str = "id", db: AsyncSession = Depends(get_async_session)):
    return await BuildingService.read_sort(name, sort_by, db)

@router.get('/DBReadOne', tags = ['read'], response_model = BuildingResponse)
async def read_one(building_id: int, db: AsyncSession = Depends(get_async_session)):
    return await BuildingService.read_one(building_id, db)

@router.put('/DBUpdate', tags = ['update'], response_model = BuildingResponse) 
async def update(building_id: int, building_in: BuildingUpdate, db: AsyncSession = Depends(get_async_session)):
    return await BuildingService.update(building_id, building_in, db)

@router.delete('/DBDelete', tags = ['delete'], status_code = status.HTTP_204_NO_CONTENT)
async def delete(building_id: int, db: AsyncSession = Depends(get_async_session)):
    return await BuildingService.delete(building_id, db)