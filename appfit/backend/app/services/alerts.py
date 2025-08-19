from ..models import Alert


def generate_alert(db, user_id: int, level: str, code: str, message: str):
    alert = Alert(user_id=user_id, level=level, code=code, message=message)
    db.add(alert)
    db.commit()
    return alert
