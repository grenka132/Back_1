from sqlalchemy.orm import Mapped, mapped_column
from src.DB.session import Base

class DBModel(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, index=True)