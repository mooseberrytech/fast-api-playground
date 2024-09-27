from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import exc
from sqlalchemy.orm import Session

from ..database import get_db
from ..models.tutorial import Tutorial
from ..schemas.tutorial import TutorialCreate, Error

router = APIRouter()


@router.post("/tutorials/", responses={409: {"model": Error}})
def create_tutorial(tutorial_data: TutorialCreate, db: Session = Depends(get_db)):
    try:
        tutorial = Tutorial(**tutorial_data.dict())
        db.add(tutorial)
        db.commit()
    except exc.IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="A tutorial with this topic already exists",
        )
