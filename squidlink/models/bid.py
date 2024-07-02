"""Pydantic models for Bids."""

from pydantic import BaseModel


class ReadBid(BaseModel):
    """Pydantic model for reading a Bid."""
    id: int

    contractor_id: int
    project_id: int

    price: int
    duration: int
    site_inspection: bool
    estimated_savings: int | None

    class Config:
        orm_mode = True


class WriteBid(BaseModel):
    """Pydantic model for writing a Bid."""
    contractor_id: int
    project_id: int

    price: int
    duration: int
    site_inspection: bool
    estimated_savings: int | None

    class Config:
        orm_mode = True
