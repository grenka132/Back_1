from sqlalchemy.orm import Mapped, mapped_column
from src.DB.session import Base

class Building(Base):
    __tablename__ = "building"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(index=True)
    description: Mapped[str] = mapped_column(index=True)
    space: Mapped[float] = mapped_column(index=True)
    locate: Mapped[str] = mapped_column(index=True)