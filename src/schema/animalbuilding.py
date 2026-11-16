import uuid
from datetime import date

from pydantic import BaseModel, Field


class AnimalBuilding(BaseModel):
    uid_animal: uuid.UUID = Field(description='UID животного')
    uid_building: uuid.UUID = Field(description='UID здания')


class AnimalBuildingFromDB(BaseModel):
    uid: uuid.UUID = Field(description='UID связи')
    uid_animal: uuid.UUID = Field(description='UID животного')
    uid_building: uuid.UUID = Field(description='UID здания')


class AnimalBuildingFilter(BaseModel):
    limit: int = Field(default=10, ge=-1,description='Лимит')
    offset: int = Field(default=0, ge=0,description='Смещение')
    search_string: str | None = Field(default=None,description='Поиск по строке')
    birthday_from: date | None = Field(description='Дата рождения от')
    birthday_to: date | None = Field(description='Дата рождения до')
    order_by: str | None = Field(default=None, description='Сортировка по столбцу')
    order_desc: bool = Field(default=False, description='Сортировка по убыванию')


class AnimalBuildingUpdate(BaseModel):
    uid_animal: uuid.UUID = Field(description='UID животного')
    uid_building: uuid.UUID = Field(description='UID здания')


class AnimalBuildingOutput(BaseModel):
    uid: uuid.UUID = Field(description='UID связи')
    uid_animal: uuid.UUID = Field(description='UID животного')
    uid_building: uuid.UUID = Field(description='UID здания')

