from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session

from ..db.session import get_db
from ..models import User
from ..schemas.user import UserCreate
from ..schemas.auth import Token
from ..core.security import (
    verify_password,
    get_password_hash,
    create_access_token,
    create_refresh_token,
    decode_token,
)

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=Token)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user_in.email).first():
        raise HTTPException(status_code=400, detail="Email já registrado")
    user = User(email=user_in.email, password_hash=get_password_hash(user_in.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return Token(
        access_token=create_access_token(str(user.id)),
        refresh_token=create_refresh_token(str(user.id)),
    )


@router.post("/login", response_model=Token)
def login(user_in: UserCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_in.email).first()
    if not user or not verify_password(user_in.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Credenciais inválidas")
    return Token(
        access_token=create_access_token(str(user.id)),
        refresh_token=create_refresh_token(str(user.id)),
    )


@router.post("/refresh", response_model=Token)
def refresh(token: Token):
    sub = decode_token(token.refresh_token)
    if not sub:
        raise HTTPException(status_code=401, detail="Token inválido")
    return Token(
        access_token=create_access_token(sub),
        refresh_token=create_refresh_token(sub),
    )


def _token_from_header(request: Request) -> str:
    auth = request.headers.get("Authorization")
    if auth and auth.startswith("Bearer "):
        return auth.split(" ")[1]
    raise HTTPException(status_code=401, detail="Sem credenciais")


def get_current_user(
    token: str = Depends(_token_from_header), db: Session = Depends(get_db)
) -> User:
    sub = decode_token(token)
    if not sub:
        raise HTTPException(status_code=401, detail="Token inválido")
    user = db.get(User, int(sub))
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user
