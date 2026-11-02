from pydantic import BaseModel, Field, ConfigDict


class Building(BaseModel):
    name: str = Field(description='Имя постройки')
    description: str = Field(description='Описание постройки')
    space: float = Field(description='Площадь в квадратных метрах')
    locate: str = Field(description='Адрес постройки')


class BuildingCreate(Building):
    pass


class BuildingUpdate(Building):
    name: str | None = Field(default=None, description='Имя постройки')
    description: str | None = Field(default=None, description='Описание постройки')
    space: float | None = Field(default=None, description='Площадь в квадратных метрах')
    locate: str | None = Field(default=None, description='Адрес постройки')

class BuildingResponse(Building):
    id: int = Field(description='ID постройки')
    model_config = ConfigDict(from_attributes=True)