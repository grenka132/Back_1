import uuid

from sqlalchemy import String, UUID, Float

from sqlalchemy.orm import Mapped, mapped_column
from src.adapter.session import Base


class Building(Base):
    __tablename__ = "building"

    uid: uuid.UUID = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    space: Mapped[float] = mapped_column(Float)
    locate: Mapped[str] = mapped_column(String)