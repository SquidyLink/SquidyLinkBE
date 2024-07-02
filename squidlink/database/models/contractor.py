from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Table,
)
from sqlalchemy.orm import relationship

from squidlink.database.database import Base

contractors_skills_pivot = Table(
    'contractors_skills', Base.metadata,
    Column('contractor_id', Integer, ForeignKey('contractors.id'), primary_key=True),
    Column('skill_id', Integer, ForeignKey('skills.id'), primary_key=True)
)

projects_skills_pivot = Table(
    'projects_skills', Base.metadata,
    Column('project_id', Integer, ForeignKey('projects.id'), primary_key=True),
    Column('skill_id', Integer, ForeignKey('skills.id'), primary_key=True)
)

class Contractor(Base):
    """SQL data model for a Contractor."""
    __tablename__ = "contractors"

    id = Column(Integer, nullable=False, primary_key=True)

    skills = relationship("Skill", secondary=contractors_skills_pivot, back_populates='contractors')
    bids = relationship("Bid", back_populates='contractors')

    name = Column(String, nullable=False)
    address_line_1 = Column(String)
    address_line_2 = Column(String)
    address_postcode = Column(String)
    address_city = Column(String)
    address_country = Column(String)

class Skill(Base):
    """SQL data model for a Skill."""
    __tablename__ = "skills"

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String, nullable=False)

    contractors = relationship('Contractor', secondary=contractors_skills_pivot, back_populates='skills')
    projects = relationship('Project', secondary=projects_skills_pivot, back_populates='skills')
