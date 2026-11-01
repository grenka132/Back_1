from src.adapter.save import save_data, read_data
from src.schema.building import Building, BuildingUpdate

from fastapi import HTTPException, Query

from typing import Annotated
# Annotated[Building, Query()]
class BuildingService:
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
    async def saveupdate(ID: int, body: BuildingUpdate) -> str:
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
    async def savereadall() -> list[Building]:
        data = [{'id':key, **element} for key, element in read_data().items()]
        return data

    @staticmethod
    async def saveread(ID: int) -> Building:
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