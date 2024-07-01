from pydantic import BaseModel

from squidlink.main import app
from squidlink.database.models.contractor import (
    Contractor as DbContractor,
    Skill as DbSkill,
    FacilitySector
)


class Skill(BaseModel):
    id: int
    name: str


class Contractor(BaseModel):
    id: int
    name: str

    address_line_1: str | None
    address_line_2: str | None
    address_postcode: str | None
    address_city: str | None
    address_country: str | None

    skills: list[Skill]


@app.get("/contractor/{contractor_id}")
def read_contractor(contractor_id: int):
    ...
    # TODO return JSON


@app.post("/contractor")
def create_contractor(contractor: Contractor):
    # TODO sql insert
    contractor = DbContractor(
        ...
    )
