from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.DB.session import get_async_session
from src.model.building import Building
from src.schema.building import BuildingCreate, BuildingUpdate
from src.adapter.DB import DBFind, DBRefresh

class BuildingService:
    @staticmethod
    async def create(building_in: BuildingCreate, db: AsyncSession = Depends(get_async_session)):  
        building = Building(**building_in.model_dump())
        db.add(building)
        return await DBRefresh(building, db)

    @staticmethod
    async def read_sort(name: str | None = None, sort_by: str = "id", db: AsyncSession = Depends(get_async_session)):
        query = select(Building)
        if name:
            query = query.where(Building.name.ilike(f"%{name}%"))
        if sort_by == "name":
            query = query.order_by(Building.name)
        else:
            query = query.order_by(Building.id)
        result = await db.execute(query)
        return result.scalars().all()

    @staticmethod
    async def read_one(building_id: int, db: AsyncSession = Depends(get_async_session)):
        return await DBFind(Building, building_id, db)

    @staticmethod
    async def update(building_id: int, building_in: BuildingUpdate, db: AsyncSession = Depends(get_async_session)):
        building = await DBFind(Building, building_id, db)
        update_data = building_in.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(building, key, value)           
        return await DBRefresh(building, db)

    @staticmethod
    async def delete(building_id: int, db: AsyncSession = Depends(get_async_session)):
        building = await DBFind(Building, building_id, db)
        await db.delete(building)
        await db.commit()
        return "Success"