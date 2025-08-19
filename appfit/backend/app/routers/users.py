from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..db.session import get_db
from ..models import User
from ..schemas.user import UserRead, UserCreate
from .auth import get_current_user

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", response_model=UserRead)
def read_me(current_user: User = Depends(get_current_user)):
    return current_user


@router.put("/me", response_model=UserRead)
def update_me(
    user_in: UserCreate,  # simplificado
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    current_user.name = user_in.name
    db.add(current_user)
    db.commit()
    db.refresh(current_user)
    return current_user


@router.delete("/me")
def delete_me(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db.delete(current_user)
    db.commit()
    return {"status": "deleted"}
