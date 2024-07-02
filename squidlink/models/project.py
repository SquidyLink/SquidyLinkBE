"""Pydantic model for projects."""

from pydantic import BaseModel

from squidlink.models.contractor import ReadSkill
from squidlink.models.bid import ReadBid


class ReadProject(BaseModel):
    """Pydantic model for reading a Project."""
    id: int

    facility_id: int
    skills: list[ReadSkill]
    bids: list[ReadBid]

    class Config:
        orm_mode = True
