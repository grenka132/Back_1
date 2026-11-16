import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.adapter.session import get_session
from src.schema.building import Building, BuildingFilter, BuildingOutput, BuildingUpdate
from src.service.building import BuildingService

router = APIRouter()

service = BuildingService()


@router.post('/', tags=['create'], response_model=BuildingOutput, status_code=status.HTTP_201_CREATED)
async def create(
    body: Building, db_session: Annotated[AsyncSession, Depends(get_session)]) -> BuildingOutput:
    return await service.create(body, db_session)


@router.get('/list', tags = ['read'], response_model = list[BuildingOutput])
async def get_list(
    db_session: Annotated[AsyncSession, Depends(get_session)],
    body: Annotated[BuildingFilter, Query(...)]
) -> BuildingOutput:
    return await service.get_list(body, db_session)


@router.get('/', tags = ['read'])
async def get_by_uid(uid: uuid.UUID, db_session: Annotated[AsyncSession, Depends(get_session)],) -> BuildingOutput:
    return await service.get_by_uid(uid, db_session)


@router.put('/', tags = ['update'], responses={404: {"description": "Failed to send email"}})
async def update(
    uid: uuid.UUID,
    body: BuildingUpdate,
    db_session: Annotated[AsyncSession, Depends(get_session)]
) -> BuildingOutput:
    return await service.update(uid, body, db_session)


@router.delete('/', tags = ['delete'], status_code = status.HTTP_204_NO_CONTENT)
async def delete(uid: uuid.UUID, db_session: Annotated[AsyncSession, Depends(get_session)]):
    return await service.delete(uid, db_session)
