from pydantic import BaseModel

from squidlink.main import app
from squidlink.database.models.facility import Facility as DbFacility, FacilitySector


class Facility(BaseModel):
    id: int
    name: str

    address_line_1: str | None
    address_line_2: str | None
    address_postcode: str | None
    address_city: str | None
    address_country: str | None

    bms: str | None
    sector: FacilitySector | None
    floor_area_square_metres: int | None


@app.get("/facility/{facility_id}")
def read_facility(facility_id: int):
    ...
    # TODO return JSON


@app.post("/facility")
def create_facility(facility: Facility):
    # TODO sql insert
    facility = DbFacility(
        ...
    )
