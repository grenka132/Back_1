from pydantic import BaseModel, Field


class Animal(BaseModel):
    name: str = Field(description='Имя животного')
    description: str = Field(description='Описание животного')

    # def __str__(self):
    #     return