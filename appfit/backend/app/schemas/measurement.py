from datetime import date
from pydantic import BaseModel


class MeasurementBase(BaseModel):
    date: date
    steps: int | None = None
    hr_avg: int | None = None
    hr_rest: int | None = None
    vo2max_est: float | None = None
    calories_burned: int | None = None


class MeasurementCreate(MeasurementBase):
    pass


class MeasurementRead(MeasurementBase):
    id: int

    class Config:
        from_attributes = True
