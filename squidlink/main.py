"""Main module for the SquidLink API."""

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from squidlink import models
from squidlink.database.database import get_db
from squidlink.database import models as db_models
from squidlink.database import queries

app = FastAPI()


@app.get("/")
def test():
    """Test endpoint."""
    return {"Hello": "World"}


@app.get("/projects")
def read_projects(db: Session = Depends(get_db)) -> list[models.ReadProject]:
    """Retrieve all projects."""
    return queries.get_projects(db)


@app.get("/facility/{facility_id}")
def read_facility(facility_id: int, db: Session = Depends(get_db)) -> models.ReadFacility:
    """Retrieve a facility by ID."""
    ...
    # TODO return JSON


@app.post("/facility")
def create_facility(facility: models.WriteFacility, db: Session = Depends(get_db)) -> models.ReadFacility:
    """Create a new facility."""
    # TODO sql insert
    facility = db_models.facility.Facility(
        ...
    )


@app.get("/contractor/{contractor_id}")
def read_contractor(contractor_id: int, db: Session = Depends(get_db)) -> models.ReadContractor:
    """Retrieve a contractor by ID."""
    ...
    # TODO return JSON


@app.post("/contractor")
def create_contractor(contractor: models.WriteContractor, db: Session = Depends(get_db)) -> models.ReadContractor:
    """Create a new contractor."""
    # TODO sql insert
    contractor = db_models.contractor.Contractor(
        ...
    )


@app.get("/bid/{project_id}")
def read_bids(project_id: int, db: Session = Depends(get_db)) -> models.ReadBid:
    """Retrieve all bids for a project."""
    ...
    # TODO return JSON


@app.post("/bid/{project_id}")
def create_bid(project_id: int,  bid: models.WriteBid, db: Session = Depends(get_db)) -> models.ReadBid:
    """Create a new bid for a project."""
    # TODO sql insert
    created_bid = db_models.bid.Bid(
        ...
    )
