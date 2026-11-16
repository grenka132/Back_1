import uuid
from datetime import date

from pydantic import model_dump
from sqlalchemy import UUID, Date, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.adapter.session import Base
from src.schema.animal import AnimalOutput


class Animal(Base):
    __tablename__ = "animals"

    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    birthday: Mapped[date] = mapped_column(Date)

    animal_buildings = relationship(
        'AnimalBuilding',
        back_populates='animal',
        lazy='raise',
        passive_deletes=True,
    )

    def serialize(self) -> AnimalOutput:
        data = model_dump(self, exclude={"_sa_instance_state"})
        return AnimalOutput(**data)
