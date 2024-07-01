from pydantic import BaseModel

from squidlink.main import app
from squidlink.database.models.project import Project as DbProject
from squidlink.database.models.contractor import Skill as DbSkill
from squidlink.crud.contractor import Skill


class Project(BaseModel):
    id: int

    facility_id: int
    skills: list[Skill]


@app.get("/projects")
def read_projects():
    ...
    # TODO return JSON
