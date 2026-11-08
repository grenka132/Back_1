import uuid

from sqlalchemy import delete, desc, select, update, or_
from sqlalchemy.ext.asyncio import AsyncSession

from src.model.building import Building as Model
from src.schema.building import BuildingFilter, Building, BuildingUpdate

class BuildingService:
    model = Model

    @classmethod
    async def create(cls, body: Building,  db_session: AsyncSession):  
        model = cls.model(**body.model_dump())
        db_session.add(model)
        await db_session.commit()
        return model

    @classmethod
    async def get_list(cls,body: BuildingFilter, db_session: AsyncSession):
        query = select(cls.model)

        if body.limit > 0:
            query = query.limit(body.limit)
        if body.offset > 0:
            query = query.offset(body.offset)

        if body.search_string is not None:
            query = query.where(
                or_(
                    cls.model.name.ilike(f"%{body.search_string}%"),
                    cls.model.description.ilike(f"%{body.search_string}%")
                )
            )
        if body.order_by is not None:
            column = getattr(cls.model, body.order_by)
        else:
            column = None

        # Учитываем направление сортировки (если в фильтре есть order_desc)
        if column:
            if body.order_desc:
                query = query.order_by(desc(column))
            else:
                query = query.order_by(column)
        
        result = await db_session.execute(query)
        return result.scalars().all()


    @classmethod
    async def get_by_uid(cls, uid: uuid.UUID, db_session: AsyncSession):
        query = select(cls.model)
        query = query.where(cls.model.uid == uid)
        result = await db_session.execute(query)
        return result.scalar()

    @classmethod
    async def update(cls,uid: uuid.UUID, body: BuildingUpdate, db_session: AsyncSession):
        query = update(cls.model)
        query = query.where(cls.model.uid == uid)
        query = query.values(**body.model_dump())
        await db_session.execute(query)
        await db_session.commit()
        return cls.get_by_uid(uid)

    @classmethod
    async def delete(cls, uid: uuid.UUID, db_session: AsyncSession):
        query = delete(cls.model)
        query = query.where(cls.model.uid == uid)
        await db_session.execute(query)
        await db_session.commit()
        return "Success"