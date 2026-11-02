from sqlalchemy.orm import Mapped, mapped_column
from src.model.DBModel import DBModel

class Animal(DBModel):
    __tablename__ = "animals"

    name: Mapped[str] = mapped_column(index=True)
    description: Mapped[str] = mapped_column(index=True)