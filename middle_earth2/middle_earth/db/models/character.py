from sqlalchemy import Column, text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import INTEGER, TEXT, TIMESTAMP, UUID, BYTEA
from sqlalchemy.sql import func

from middle_earth.db import Base

# Base = Base()
class Character(Base):
    __tablename__ = "character"

    id = Column(
        INTEGER,
        primary_key=True,
        autoincrement=True,
        unique=True,
        doc="Unique card id",
    )
    name = Column(
        TEXT,
        unique=True,
    )
    content = Column(
        TEXT,
    )
    # photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    # time_create = models.DateField(auto_now_add=True)
    # time_update = models.DateTimeField(auto_now=True)
    # is_published = models.BooleanField(default=True)
    # cat = models.ForeignKey('Category', on_delete = models.PROTECT, null=True)
    dt_created = Column(
        TIMESTAMP(timezone=True), # pylint: disable=not-callable
        nullable=False,
        doc="Date and time when string in table was created",
    )
    dt_updated = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        doc="",
    )
