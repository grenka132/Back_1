from pydantic import BaseModel, Field
import uuid


class Building(BaseModel):
    name: str = Field(description='Имя постройки')
    description: str = Field(description='Описание постройки')
    space: float = Field(description='Площадь в квадратных метрах')
    locate: str = Field(description='Адрес постройки')


class BuildingFromDB(BaseModel):
    uid: uuid.UUID = Field(description='UID животного')
    name: str = Field(description='Имя постройки')
    description: str = Field(description='Описание постройки')
    space: float = Field(description='Площадь в квадратных метрах')
    locate: str = Field(description='Адрес постройки')


class BuildingFilter(BaseModel):
    limit: int = Field(default=10, ge=-1,description='Лимит')
    offset: int = Field(default=0, ge=0,description='Смещение')
    search_string: str | None = Field(default=None,description='Поиск по строке')
    order_by: str | None = Field(default=None, description='Сортировка по столбцу')
    order_desc: bool = Field(default=False, description='Сортировка по убыванию')


class BuildingUpdate(BaseModel):
    name: str | None = Field(default=None, description='Имя постройки')
    description: str | None = Field(default=None, description='Описание постройки')
    space: float | None = Field(default=None, description='Площадь в квадратных метрах')
    locate: str | None = Field(default=None, description='Адрес постройки')


class BuildingOutput(BaseModel):
    name: str = Field(description='Имя постройки')
    description: str = Field(description='Описание постройки')
    space: float = Field(description='Площадь в квадратных метрах')
    locate: str = Field(description='Адрес постройки')