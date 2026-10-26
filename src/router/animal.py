from fastapi import APIRouter, HTTPException

from src.adapter.save import save_data, read_data
import src.schema.animal as animal

from src.service.animal import AnimalService


router = APIRouter()


@router.get('/hry')
async def hry() -> str:
    return await AnimalService.hry()


@router.post('/hry')
async def create_hry(body: animal.AnimalCreate) -> animal.Animal:
    return await AnimalService.create_hry({'id':0,**body.model_dump()})


@router.post('/SaveCreate', tags = ['create'])
async def savecreate(body: animal.AnimalCreate) -> str:
    return await AnimalService.savecreate(body)
    
        
@router.get('/SaveRead', tags = ['read'])
async def saveread(ID: int) -> animal.Animal:
    return await AnimalService.saveread(ID)


@router.get('/SaveReadAll', tags = ['read'])
async def savereadall() -> list[animal.Animal]:
    return await AnimalService.savereadall()


@router.put('/SaveUpdate', tags = ['update'])
async def saveupdate(ID: int, body: animal.AnimalUpdate) -> str:
    return await AnimalService.saveupdate(ID, body)


@router.delete('/SaveDelete', tags = ['delete'])
async def savedelete(ID: int) -> str:
    return await AnimalService.savedelete(ID)
