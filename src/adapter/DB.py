from fastapi import Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.model.DBModel import DBModel

async def DBFind(model_type: type[DBModel],model_id: int, db: AsyncSession):
    result = await db.execute(select(model_type).where(model_type.id == model_id))
    model = result.scalar_one_or_none()
    if not model:
        raise HTTPException(status_code=404, detail="Object not found")
    return model

async def DBRefresh(model: DBModel, db: AsyncSession):
    await db.commit()
    await db.refresh(model)
    return model