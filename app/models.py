from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import JSON


class Hotels(Base):
    __tablename__ = 'hotels'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    location: Mapped[str] = mapped_column(nullable=False)
    services: Mapped[JSON] = mapped_column(type_=JSON)
    rooms_quantity: Mapped[int] = mapped_column(nullable=False)
    image_id: Mapped[int]
