from pydantic import BaseModel, Field, ConfigDict


class Animal(BaseModel):
    
    name: str = Field(description='Имя животного')
    description: str = Field(description='Описание животного')


class AnimalCreate(Animal):
    pass


class AnimalUpdate(Animal):
    name: str | None = Field(default=None, description='Имя животного')
    description: str | None = Field(default=None, description='Описание животного')


class AnimalResponse(Animal):
    id: int = Field(description='ID животного')
    model_config = ConfigDict(from_attributes=True)
