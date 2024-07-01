from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from squidlink.database.database import Base

# Association table for the many-to-many relationship between contractors and skills
contractor_skills_association = Table(
    'contractor_skills', Base.metadata,
    Column('contractor_id', Integer, ForeignKey('contractors.id'), primary_key=True),
    Column('skill_id', Integer, ForeignKey('skills.id'), primary_key=True)
)

class Contractor(Base):
    """SQL data model for a Contractor."""
    __tablename__ = "contractors"

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String)
    address_line_1 = Column(String)
    address_line_2 = Column(String)
    address_postcode = Column(String)
    address_city = Column(String)
    address_country = Column(String)

    skills = relationship('Skill', secondary=contractor_skills_association, back_populates='contractors')

class Skill(Base):
    """SQL data model for a Skill."""
    __tablename__ = "skills"

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String, nullable=False)

    # Define the relationship to contractors
    contractors = relationship('Contractor', secondary=contractor_skills_association, back_populates='skills')
