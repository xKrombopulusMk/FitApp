from .db.session import SessionLocal
from .models import User
from .core.security import get_password_hash


def run():
    db = SessionLocal()
    if not db.query(User).filter(User.email == "demo@appfit.io").first():
        user = User(
            email="demo@appfit.io",
            password_hash=get_password_hash("demo123"),
            name="Demo",
        )
        db.add(user)
        db.commit()
    db.close()


if __name__ == "__main__":
    run()
