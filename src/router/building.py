from fastapi import APIRouter, HTTPException

from src.adapter.save import save_data, read_data
import src.schema.building as building

from src.service.building import BuildingService


router = APIRouter()



@router.post('/SaveCreate', tags = ['create'])
async def savecreate(body: building.BuildingCreate) -> str:
    return await BuildingService.savecreate(body)
    
        
@router.get('/SaveRead', tags = ['read'])
async def saveread(ID: int) -> building.Building:
    return await BuildingService.saveread(ID)


@router.get('/SaveReadAll', tags = ['read'])
async def savereadall() -> list[building.Building]:
    return await BuildingService.savereadall()


@router.get('/SaveReadSort', tags = ['read'])
async def savereadsort() -> list[building.Building]: # вернуться позже вернуться позже вернуться позже вернуться позже вернуться позже вернуться позже
    return await BuildingService.savereadall()


@router.put('/SaveUpdate', tags = ['update'])
async def saveupdate(ID: int, body: building.BuildingUpdate) -> str:
    return await BuildingService.saveupdate(ID, body)


@router.delete('/SaveDelete', tags = ['delete'])
async def savedelete(ID: int) -> str:
    return await BuildingService.savedelete(ID)
