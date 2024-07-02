from pydantic import BaseModel

from squidlink.models.bid import ReadBid


class ReadSkill(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class ReadContractor(BaseModel):
    id: int
    name: str

    address_line_1: str | None
    address_line_2: str | None
    address_postcode: str | None
    address_city: str | None
    address_country: str | None

    skills: list[ReadSkill]
    bids: list[ReadBid]

    class Config:
        orm_mode = True


class WriteContractor(BaseModel):
    name: str
    address_line_1: str | None
    address_line_2: str | None
    address_postcode: str | None
    address_city: str | None
    address_country: str | None

    class Config:
        orm_mode = True
