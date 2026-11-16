import uuid

from pydantic import model_dump
from sqlalchemy import UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.adapter.session import Base
from src.schema.animalbuilding import AnimalBuildingOutput


class AnimalBuilding(Base):
    __tablename__ = "animal_buildings"

    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    uid_animal: Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey('animals.uid'), nullable=False)
    uid_building: Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey('building.uid'), nullable=False)

    animal = relationship(
        'Animal',
        back_populates='animal_buildings',
        lazy='raise',
        passive_deletes=True,
    )

    building = relationship(
        'Building',
        back_populates='animal_buildings',
        lazy='raise',
        passive_deletes=True,
    )

    def serialize(self) -> AnimalBuildingOutput:
        data = model_dump(self, exclude={"_sa_instance_state"})
        return AnimalBuildingOutput(**data)
