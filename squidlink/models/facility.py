from pydantic import BaseModel

from squidlink.database.models.facility import FacilitySector


class ReadFacility(BaseModel):
    id: int
    name: str

    address_line_1: str | None
    address_line_2: str | None
    address_postcode: str | None
    address_city: str | None
    address_country: str | None

    bms: str | None
    sector: FacilitySector
    floor_area_square_metres: int | None

    class Config:
        orm_mode = True


class WriteFacility(BaseModel):
    name: str

    address_line_1: str | None
    address_line_2: str | None
    address_postcode: str | None
    address_city: str | None
    address_country: str | None

    bms: str | None
    sector: FacilitySector
    floor_area_square_metres: int | None

    class Config:
        orm_mode = True
