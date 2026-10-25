from fastapi import APIRouter

from schema.animal import Animal

import json

router = APIRouter()

@router.get('/hry')
def hry() -> str:
    return 'Хрю-хрю'

@router.post('/hry')
def create_hry(body: Animal) -> Animal:
    return body

@router.post('/SaveCreate')
def savecreate(body: Animal) -> str:
    savefile = "saves/save.json"
    with open(savefile, mode="r") as f:
        data = json.load(f)
        if data.keys():
            ID = max(int(k) for k in data.keys())+1
        else:
            ID = 0
        data[ID] = body.model_dump()
    with open(savefile, mode="w") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return "Success"
        
@router.post('/SaveRead')
def saveread(ID: int) -> str:
    ID = str(ID)
    savefile = "saves/save.json"
    with open(savefile, mode="r") as f:
        data = json.load(f)
        if data.keys():
            return f"{data[ID]}"
        else:
            return "ID not in save file"

@router.post('/SaveReadAll')
def savereadall() -> dict:
    savefile = "saves/save.json"
    with open(savefile, mode="r") as f:
        data = json.load(f)
    return data

@router.post('/SaveUpdate')
def saveupdate(ID: int, body: Animal) -> str:
    savefile = "saves/save.json"
    with open(savefile, mode="r") as f:
        data = json.load(f)
        if data.keys():
            data[str(ID)] = body.model_dump()
        else:
            return "ID not in save file"
    with open(savefile, mode="w") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return "Success"

@router.post('/SaveDelete')
def savedelete(ID: int) -> str:
    savefile = "saves/save.json"
    with open(savefile, mode="r") as f:
        data = json.load(f)
        if str(ID) in data.keys():
            del data[str(ID)]
        else:
            return "ID not in save file"
    with open(savefile, mode="w") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return "Success"