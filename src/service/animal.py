from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.DB.session import get_async_session
from src.model.animal import Animal
from src.schema.animal import AnimalCreate, AnimalUpdate
from src.adapter.DB import DBFind, DBRefresh

class AnimalService:
    @staticmethod
    async def create(animal_in: AnimalCreate, db: AsyncSession = Depends(get_async_session)):  
        animal = Animal(**animal_in.model_dump())
        db.add(animal)
        return await DBRefresh(animal, db)

    @staticmethod
    async def read_sort(name: str | None = None, sort_by: str = "id", db: AsyncSession = Depends(get_async_session)):
        query = select(Animal)
        if name:
            query = query.where(Animal.name.ilike(f"%{name}%"))
        if sort_by == "name":
            query = query.order_by(Animal.name)
        else:
            query = query.order_by(Animal.id)
        result = await db.execute(query)
        return result.scalars().all()

    @staticmethod
    async def read_one(animal_id: int, db: AsyncSession = Depends(get_async_session)):
        return await DBFind(Animal, animal_id, db)

    @staticmethod
    async def update(animal_id: int, animal_in: AnimalUpdate, db: AsyncSession = Depends(get_async_session)):
        animal = await DBFind(Animal, animal_id, db)
        update_data = animal_in.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(animal, key, value)           
        return await DBRefresh(animal, db)

    @staticmethod
    async def delete(animal_id: int, db: AsyncSession = Depends(get_async_session)):
        animal = await DBFind(Animal, animal_id, db)
        await db.delete(animal)
        await db.commit()
        return "Success"

    @staticmethod
    async def create_hry(body) -> Animal:
        return body

    @staticmethod
    async def hry() -> str:
        return 'Хрю-хрю'


# В отдельных сервисах - роутерах схемах создать файлы для отдельной сущности. (Желательно иметь множество столбцов для сущности)
# Реализовать схожую функционал (CRUD) но через базу данных + фильрация
# +++ можно разобраться как превтратить pydantic-модель в query запрос fastapi 
# Понять и простить уроки с 5 по 8