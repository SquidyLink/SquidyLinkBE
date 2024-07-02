"""Main module for the SquidLink API."""

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from squidlink.database.database import get_db
from squidlink.database.models.project import Project as DbProject, get_projects
from squidlink.database.models.facility import Facility as DbFacility
from squidlink.database.models.contractor import Contractor as DbContractor, Skill as DbSkill
from squidlink.database.models.bid import Bid as DbBid
from squidlink.models.project import ReadProject
from squidlink.models.facility import ReadFacility, WriteFacility
from squidlink.models.contractor import ReadContractor, WriteContractor, ReadSkill
from squidlink.models.bid import ReadBid, WriteBid

app = FastAPI()


@app.get("/")
def test():
    """Test endpoint."""
    return {"Hello": "World"}


@app.get("/projects")
def read_projects(db: Session = Depends(get_db)) -> list[ReadProject]:
    """Retrieve all projects."""
    return get_projects(db)


@app.get("/facility/{facility_id}")
def read_facility(facility_id: int, db: Session = Depends(get_db)) -> ReadFacility:
    """Retrieve a facility by ID."""
    ...
    # TODO return JSON


@app.post("/facility")
def create_facility(facility: ReadFacility, db: Session = Depends(get_db)) -> ReadFacility:
    """Create a new facility."""
    # TODO sql insert
    facility = db_models.facility.Facility(
        ...
    )


@app.get("/contractor/{contractor_id}")
def read_contractor(contractor_id: int, db: Session = Depends(get_db)) -> ReadContractor:
    """Retrieve a contractor by ID."""
    ...
    # TODO return JSON


@app.post("/contractor")
def create_contractor(contractor: WriteContractor, db: Session = Depends(get_db)) -> ReadContractor:
    """Create a new contractor."""
    # TODO sql insert
    contractor = db_models.contractor.Contractor(
        ...
    )


@app.get("/bid/{project_id}")
def read_bids(project_id: int, db: Session = Depends(get_db)) -> ReadBid:
    """Retrieve all bids for a project."""
    ...
    # TODO return JSON


@app.post("/bid/{project_id}")
def create_bid(project_id: int,  bid: WriteBid, db: Session = Depends(get_db)) -> ReadBid:
    """Create a new bid for a project."""
    # TODO sql insert
    created_bid = db_models.bid.Bid(
        ...
    )
