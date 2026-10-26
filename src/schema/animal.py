from pydantic import BaseModel, Field


class AnimalCreate(BaseModel):
    name: str = Field(description='Имя животного')
    description: str = Field(description='Описание животного')


class Animal(BaseModel):
    id: int = Field(description='ID животного')
    name: str = Field(description='Имя животного')
    description: str = Field(description='Описание животного')


class AnimalUpdate(BaseModel):
    name: str | None = Field(default=None, description='Имя животного')
    description: str | None = Field(default=None, description='Описание животного')
