from sqlalchemy.orm import Session

from squidlink.database import models


def get_projects(db: Session):
    """Retrieve all projects."""
    return db.query(models.Project).all()
