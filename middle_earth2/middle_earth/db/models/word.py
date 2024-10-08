from sqlalchemy import Column, text, DateTime
from sqlalchemy.dialects.postgresql import INTEGER, TEXT, TIMESTAMP, UUID, BYTEA
from sqlalchemy.sql import func

from middle_earth.db import Base

# Base = Base()
class Word(Base):
    __tablename__ = "word"

    id = Column(
        INTEGER,
        primary_key=True,
        autoincrement=True,
        server_default=func.gen_random_uuid(),
        unique=True,
        doc="Unique word id",
    )
    russian = Column(
        TEXT,
        nullable=False,
        unique=True,
        doc="Russian word",
    )
    english = Column(
        TEXT,
        nullable=False,
        unique=True,
        doc="English word"
    )

    def __repr__(self):
        columns = {column.name: getattr(self, column.name) for column in self.__table__.columns}
        return f'<{self.__tablename__}: {", ".join(map(lambda x: f"{x[0]}={x[1]}", columns.items()))}>'
