import uuid

from pydantic import model_dump
from sqlalchemy import UUID, Float, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.adapter.session import Base
from src.schema.building import BuildingOutput


class Building(Base):
    __tablename__ = "building"

    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    space: Mapped[float] = mapped_column(Float)
    locate: Mapped[str] = mapped_column(String)

    animal_buildings = relationship(
        'AnimalBuilding',
        back_populates='building',
        lazy='raise',
        passive_deletes=True,
    )

    def serialize(self) -> BuildingOutput:
        data = model_dump(self, exclude={"_sa_instance_state"})
        return BuildingOutput(**data)
