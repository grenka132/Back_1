import uuid

from sqlalchemy import String, UUID, Date
from datetime import date

from sqlalchemy.orm import Mapped, mapped_column
from src.adapter.session import Base

class Animal(Base):
    __tablename__ = "animals"

    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    birthday: Mapped[date] = mapped_column(Date)