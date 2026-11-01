from sqlalchemy.orm import Mapped, mapped_column
from src.DB.session import Base

class Animal(Base):
    __tablename__ = "animals"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(index=True)
    description: Mapped[str] = mapped_column(index=True)