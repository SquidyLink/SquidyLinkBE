from sqlalchemy import Column, Integer, String, Boolean

from squidlink.database.database import Base


class Bid(Base):
    """SQL data model for a Facility."""

    __tablename__ = "bids"

    id = Column(Integer, nullable=False, primary_key=True)
    price = Column(Integer)
    duration = Column(Integer)
    site_inspection = Column(Boolean)
    estimated_savings = Column(Integer)


