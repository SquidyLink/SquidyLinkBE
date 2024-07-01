from sqlalchemy import Column, Integer, String

from squidlink.database.database import Base


class Facility(Base):
    """SQL data model for a Facility."""

    __tablename__ = "facilities"

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String)

    address_line_1 = Column(String)
    address_line_2 = Column(String)
    address_postcode = Column(String)
    address_city = Column(String)
    address_country = Column(String)

    bms = Column(String)
    sector = Column(String)

    floor_area_square_metres = Column(Integer)