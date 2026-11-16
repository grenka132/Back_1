import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.adapter.session import get_session
from src.schema.animal import AmimalOutput, AminalFilter, Animal, AnimalUpdate
from src.service.animal import AnimalService

router = APIRouter(prefix='/animal', tags=['Animal'])


@router.get('/hry')
async def hry() -> str:
    return await AnimalService.hry()


@router.post('/hry')
async def create_hry(body: Animal) -> Animal:
    return await AnimalService.create_hry({'id':0,**body.model_dump()})


@router.post(
    '/',
    tags=['create'],
    response_model=AmimalOutput,
    status_code=status.HTTP_201_CREATED
)
async def create(
    body: Animal,
    db_session: Annotated[AsyncSession, Depends(get_session)]
) -> AmimalOutput:
    return await AnimalService.create(body, db_session)


@router.get('/list', tags = ['read'], response_model = list[AmimalOutput])
async def get_list(
    db_session: Annotated[AsyncSession, Depends(get_session)],
    body: Annotated[AminalFilter,Query(...)]
) -> AmimalOutput:
    return await AnimalService.get_list(body, db_session)


@router.get('/', tags = ['read'])
async def get_by_uid(
    uid: uuid.UUID,
    db_session: Annotated[AsyncSession, Depends(get_session)]
) -> AmimalOutput:
    return await AnimalService.get_by_uid(uid, db_session)


@router.put('/', tags = ['update'])
async def update(
    uid: uuid.UUID,
    body: AnimalUpdate,
    db_session: Annotated[AsyncSession, Depends(get_session)]
) -> AmimalOutput:
    return await AnimalService.update(uid, body, db_session)


@router.delete('/', tags = ['delete'], status_code = status.HTTP_204_NO_CONTENT)
async def delete(uid: uuid.UUID, db_session: Annotated[AsyncSession, Depends(get_session)]):
    return await AnimalService.delete(uid, db_session)

# get / - найти по uid|id|field
# post / - создать
# put / - обновить по uid
# delete / - удалить по uid
