from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import Session, relationship, mapped_column

from squidlink.database.database import Base
from squidlink.database.models.facility import Facility
from squidlink.database.models.contractor import projects_skills_pivot


class Project(Base):
    """SQL data model for a Project."""
    __tablename__ = "projects"

    id = Column(Integer, nullable=False, primary_key=True)

    facility_id = mapped_column(ForeignKey("facilities.id", ondelete="CASCADE"), nullable=False)
    facility = relationship(Facility, back_populates="projects")

    skills = relationship("Skill", secondary=projects_skills_pivot, back_populates="projects")
    bids = relationship("Bid", back_populates="projects")

    name = Column(String, nullable=False)


def get_projects(db: Session):
    """Retrieve all projects."""
    return db.query(Project).all()
