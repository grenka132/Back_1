from pydantic import BaseModel, Field


class BuildingCreate(BaseModel):
    name: str = Field(description='Имя постройки')
    description: str = Field(description='Описание постройки')
    space: float = Field(description='Площадь в квадратных метрах')
    locate: str = Field(description='Адрес постройки')


class Building(BaseModel):
    id: int = Field(description='ID постройки')
    name: str = Field(description='Имя постройки')
    description: str = Field(description='Описание постройки')
    space: float = Field(description='Площадь в квадратных метрах')
    locate: str = Field(description='Адрес постройки')


class BuildingUpdate(BaseModel):
    name: str | None = Field(default=None, description='Имя постройки')
    description: str | None = Field(default=None, description='Описание постройки')
    space: float | None = Field(default=None, description='Площадь в квадратных метрах')
    locate: str | None = Field(default=None, description='Адрес постройки')