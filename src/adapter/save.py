import json

from src.config import setting

def save_data(data):
    with open(setting.SAVE_FILE, mode="w") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def read_data():
    with open(setting.SAVE_FILE, mode="r") as f:
        return json.load(f)