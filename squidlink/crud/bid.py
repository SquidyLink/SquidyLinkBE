from pydantic import BaseModel

from squidlink.main import app
from squidlink.database.models.bid import (
    Bid as DbBid,
)


class Bid(BaseModel):
    id: int
    price: int
    duration: int
    site_inspection: bool
    estimated_savings: int


@app.get("/bid/{project_id}")
def read_bids(project_id: int):
    ...
    # TODO return JSON


@app.post("/bid/{project_id}")
def create_bid(project_id: int,  bid: Bid):
    # TODO sql insert
    created_bid = DbBid(
        ...
    )
