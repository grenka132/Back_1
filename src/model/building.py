from sqlalchemy.orm import Mapped, mapped_column
from src.model.DBModel import DBModel

class Building(DBModel):
    __tablename__ = "building"

    name: Mapped[str] = mapped_column(index=True)
    description: Mapped[str] = mapped_column(index=True)
    space: Mapped[float] = mapped_column(index=True)
    locate: Mapped[str] = mapped_column(index=True)