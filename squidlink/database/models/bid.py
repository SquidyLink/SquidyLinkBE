"""SQL data model for a Bid."""

from sqlalchemy.orm import relationship, mapped_column
from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    ForeignKey
)

from squidlink.database.database import Base
from squidlink.database.models.contractor import Contractor
from squidlink.database.models.project import Project


class Bid(Base):
    """SQL data model for a Bid."""
    __tablename__ = "bids"

    id = Column(Integer, nullable=False, primary_key=True)

    contractor_id = mapped_column(ForeignKey("contractors.id", ondelete="CASCADE"), nullable=False)
    contractor = relationship(Contractor, back_populates="bids")

    project_id = mapped_column(ForeignKey("projects.id", ondelete="CASCADE"), nullable=False)
    project = relationship(Project, back_populates="bids")

    price = Column(Integer, nullable=False)
    duration = Column(Integer, nullable=False)
    site_inspection = Column(Boolean, nullable=False)
    estimated_savings = Column(Integer)
