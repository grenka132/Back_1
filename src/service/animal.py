from src.adapter.save import save_data, read_data
from src.schema.animal import Animal, AnimalUpdate

from fastapi import HTTPException


class AnimalService:
    @staticmethod
    async def savedelete(ID: int) -> str:
        data = read_data()
        if str(ID) in data.keys():
            del data[str(ID)]
        else:
            raise HTTPException(404,"ID not in save file")
        save_data(data)
        return "Success"

    @staticmethod
    async def saveupdate(ID: int, body: AnimalUpdate) -> str:
        data = read_data()
        if data.keys():
            if body.name is not None:
                data[str(ID)]['name'] = body.name
            if body.description is not None:
                data[str(ID)]['description'] = body.description
        else:
            raise HTTPException(404,"ID not in save file")
        save_data(data)
        return "Success"

    @staticmethod
    async def savereadall() -> list[Animal]:
        data = [{'id':key, **element} for key, element in read_data().items()]
        return data

    @staticmethod
    async def saveread(ID: int) -> Animal:
        ID = str(ID)
        data = read_data()
        if data.keys():
            return {'id': ID, **data[ID]}
        else:
            raise HTTPException(404,"ID not in save file")

    @staticmethod
    async def savecreate(body) -> str:
        data = read_data()
        if data.keys():
            ID = max(int(k) for k in data.keys())+1
        else:
            ID = 0
        data[ID] = body.model_dump()
        save_data(data)
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