from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from squidlink.database.database import Base

# Association table for the many-to-many relationship between projects and skills
project_skills_association = Table(
    'project_skills', Base.metadata,
    Column('project_id', Integer, ForeignKey('projects.id'), primary_key=True),
    Column('skill_id', Integer, ForeignKey('skills.id'), primary_key=True)
)

class Project(Base):
    """SQL data model for a Project."""
    __tablename__ = "projects"

    id = Column(Integer, nullable=False, primary_key=True)
    skills = relationship('Skill', secondary=project_skills_association, back_populates='projects')

class Skill(Base):
    """SQL data model for a Skill."""
    __tablename__ = "skills"

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String, nullable=False)

    # Define the relationship to projects
    projects = relationship('Project', secondary=project_skills_association, back_populates='skills')
