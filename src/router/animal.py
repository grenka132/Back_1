from fastapi import APIRouter

from src.schema.animal import Animal

router = APIRouter()

@router.get('/hry')
def hry() -> str:
    return 'Хрю-хрю'

@router.post('/hry')
def create_hry(body: Animal) -> Animal:
    return body

@router.post('/save')
def save_hry(body: Animal) -> str:
    savefile = "save.json"
    with open(savefile, mode="a") as f:
        f.writelines(body.model_dump_json())
        return "1"
        



