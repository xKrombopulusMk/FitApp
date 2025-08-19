from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..db.session import get_db
from ..models import Measurement
from ..schemas.measurement import MeasurementCreate, MeasurementRead
from .auth import get_current_user

router = APIRouter(prefix="/measurements", tags=["measurements"])


@router.post("/", response_model=MeasurementRead)
def create_measurement(
    m_in: MeasurementCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    obj = Measurement(**m_in.dict(), user_id=user.id)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.get("/", response_model=list[MeasurementRead])
def list_measurements(
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    return db.query(Measurement).filter(Measurement.user_id == user.id).all()
