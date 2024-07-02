from enum import Enum

from sqlalchemy import (
    Column,
    DateTime,
    Float,
    Integer,
    ForeignKey
)
from sqlalchemy.orm import relationship, mapped_column

from squidlink.database.database import Base
from squidlink.database.models.facility import Facility


class MeterReadingType(Enum):
    """Available meter reading types."""
    ELECTRICITY = "Electricity"
    GAS = "Gas"


class MeterReadingUnit(Enum):
    """Available meter reading units."""
    KWH = "kWh"


class MeterReadingDataSource(Enum):
    """Available meter reading data sources."""
    OCTOPUS_API = "Octopus API"


class MeterReading(Base):
    """SQL data model for a meter reading."""
    __tablename__ = "meter_readings"

    id = Column(Integer, nullable=False, primary_key=True)

    facility_id = ForeignKey("facilities.id", ondelete="CASCADE", nullable=False)
    facility = relationship(Facility, back_populates="meter_readings")

    type = Column(Enum(MeterReadingType, nullable=False))
    consumption = Column(Float, nullable=False)
    unit = Column(Enum(MeterReadingUnit, nullable=False))

    interval_start = Column(DateTime, nullable=False)
    interval_end = Column(DateTime, nullable=False)
