from datetime import date
import uuid

from pydantic import BaseModel, Field, computed_field


class Animal(BaseModel):
    name: str = Field(description='Имя животного')
    description: str = Field(description='Описание животного')
    birthday: date = Field(description='Дата рождения животного')


class AnimalFromDB(BaseModel):
    uid: uuid.UUID = Field(description='UID животного')
    name: str = Field(description='Имя животного')
    description: str = Field(description='Описание животного')
    birthday: date = Field(default_factory=date.today, description='Дата рождения животного')


class AminalFilter(BaseModel):
    limit: int = Field(default=10, ge=-1,description='Лимит')
    offset: int = Field(default=0, ge=0,description='Смещение')
    search_string: str | None = Field(default=None,description='Поиск по строке')
    birthday_from: date | None = Field(description='Дата рождения от')
    birthday_to: date | None = Field(description='Дата рождения до')
    order_by: str | None = Field(default=None, description='Сортировка по столбцу')
    order_desc: bool = Field(default=False, description='Сортировка по убыванию')


class AnimalUpdate(BaseModel):
    name: str | None = Field(default=None, description='Имя животного')
    description: str | None = Field(default=None, description='Описание животного')
    birthday: date | None = Field(default=None, description='Дата рождения животного')


class AmimalOutput(BaseModel):
    uid: uuid.UUID = Field(description='UID животного')
    name: str = Field(description='Имя животного')
    description: str = Field(description='Описание животного')
    birthday: date = Field(description='Дата рождения животного')

    @computed_field
    @property
    def age(self) -> int:
        return date.today().year - self.birthday.year


